"""FastAPI REST API application for C64-KB-Agent."""

import json
from typing import Any, cast

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from c64_kb_agent.config import settings
from c64_kb_agent.db import DatabaseDAO
from c64_kb_agent.search.fts5 import FTSSearchEngine
from c64_kb_agent.validators.dataset import validate_dataset_jsonl
from c64_kb_agent.validators.document import (
    get_all_documents,
    parse_frontmatter,
    validate_all_documents,
)
from c64_kb_agent.validators.graph_and_api import (
    validate_api_index,
    validate_cross_references,
    validate_knowledge_graph,
)
from c64_kb_agent.validators.manifest import validate_manifest

app = FastAPI(
    title="C64-KB-Agent REST API",
    description=(
        "REST API for Commodore 64 Knowledge Base — "
        "document retrieval, validation, FTS5 search, and dataset access."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


class HealthResponse(BaseModel):
    status: str = Field(..., description="Server status")
    version: str = Field("1.0.0", description="API version")


class SearchResultItem(BaseModel):
    id: str
    filepath: str
    title: str
    source_url: str
    category: str
    difficulty: str
    language: str
    hardware: str
    topics: list[str]
    rank: float
    snippet: str


class SearchResponse(BaseModel):
    query: str
    total: int
    limit: int
    offset: int
    results: list[SearchResultItem]


class DocumentItem(BaseModel):
    id: str
    filepath: str
    title: str
    category: str
    difficulty: str
    language: str
    hardware: Any
    topics: list[str]


class DocumentDetail(DocumentItem):
    frontmatter: dict[str, Any]
    body: str


class RebuildResponse(BaseModel):
    status: str
    indexed_documents: int
    indexed_routines: int
    db_path: str


@app.get("/health", tags=["System"], response_model=HealthResponse)
def get_health() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy", version="1.0.0")


@app.get("/api/v1/status", tags=["Knowledge Base"])
def get_kb_status() -> dict[str, Any]:
    """Returns status summary of documents, datasets, and search index."""
    dao = DatabaseDAO()
    db_status = dao.get_status()

    doc_paths = get_all_documents(settings.docs_dir)
    by_source: dict[str, int] = {}
    for doc in doc_paths:
        rel = doc.relative_to(settings.docs_dir)
        src = rel.parts[0] if len(rel.parts) > 1 else "root"
        by_source[src] = by_source.get(src, 0) + 1

    dataset_files_info = {}
    target_files = [
        "scraped_dataset.jsonl",
        "api_index.json",
        "knowledge_graph.json",
        "manifest.json",
    ]
    for fname in target_files:
        fpath = settings.dataset_dir / fname if fname != "manifest.json" else settings.manifest_path
        if fpath.exists():
            stat = fpath.stat()
            dataset_files_info[fname] = {
                "exists": True,
                "size_mb": round(stat.st_size / (1024 * 1024), 2),
            }
        else:
            dataset_files_info[fname] = {"exists": False}

    return {
        "documents": {
            "total": len(doc_paths),
            "by_source": by_source,
        },
        "dataset_files": dataset_files_info,
        "search_index": db_status,
    }


@app.post("/api/v1/validate", tags=["Validation"])
def validate_kb() -> dict[str, Any]:
    """Validates all KB documents, dataset files, manifest, and cross-references."""
    doc_count, doc_errors = validate_all_documents(settings.docs_dir)
    jsonl_count, jsonl_errors = validate_dataset_jsonl(
        settings.dataset_dir / "scraped_dataset.jsonl"
    )
    manifest_ok, manifest_errors = validate_manifest(settings.manifest_path)
    kg_ok, kg_errors = validate_knowledge_graph(settings.dataset_dir / "knowledge_graph.json")
    api_ok, api_errors = validate_api_index(settings.dataset_dir / "api_index.json")
    cross_errors = validate_cross_references(settings.docs_dir, settings.dataset_dir)

    all_ok = not (
        doc_errors or jsonl_errors or manifest_errors or kg_errors or api_errors or cross_errors
    )

    return {
        "passed": all_ok,
        "documents": {"checked": doc_count, "errors": doc_errors},
        "dataset_jsonl": {"checked": jsonl_count, "errors": jsonl_errors},
        "manifest": {"valid": manifest_ok, "errors": manifest_errors},
        "knowledge_graph": {"valid": kg_ok, "errors": kg_errors},
        "api_index": {"valid": api_ok, "errors": api_errors},
        "cross_references": {"errors": cross_errors},
    }


@app.post("/api/v1/index/rebuild", tags=["Index"], response_model=RebuildResponse)
def rebuild_search_index() -> RebuildResponse:
    """Rebuilds the SQLite FTS5 search index."""
    dao = DatabaseDAO()
    indexed_docs, indexed_routines = dao.rebuild_index(settings.docs_dir)
    return RebuildResponse(
        status="success",
        indexed_documents=indexed_docs,
        indexed_routines=indexed_routines,
        db_path=str(settings.db_path),
    )


@app.get("/api/v1/search", tags=["Search"])
def search_kb(
    query: str = Query(..., description="Full-text search query"),
    category: str | None = Query(None, description="Category filter"),
    difficulty: str | None = Query(None, description="Difficulty filter"),
    language: str | None = Query(None, description="Language filter"),
    hardware: str | None = Query(None, description="Hardware filter"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
) -> dict[str, Any]:
    """Performs BM25 FTS5 search against the Knowledge Base."""
    engine = FTSSearchEngine()
    return engine.search(
        query=query,
        category=category,
        difficulty=difficulty,
        language=language,
        hardware=hardware,
        limit=limit,
        offset=offset,
    )


@app.get("/api/v1/documents", tags=["Documents"])
def list_documents(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    category: str | None = Query(None, description="Category filter"),
) -> dict[str, Any]:
    """Lists documents with pagination and optional category filtering."""
    doc_paths = get_all_documents(settings.docs_dir)
    items = []

    for p in doc_paths:
        try:
            fm, _ = parse_frontmatter(p)
            cat = fm.get("category", "")
            if category and cat != category:
                continue

            rel = str(p.relative_to(settings.docs_dir))
            doc_id = fm.get("id") or rel
            hw = fm.get("hardware", [])
            tp = fm.get("topics", fm.get("tags", []))

            items.append(
                {
                    "id": doc_id,
                    "filepath": rel,
                    "title": fm.get("title", ""),
                    "category": cat,
                    "difficulty": fm.get("difficulty", ""),
                    "language": fm.get("language", ""),
                    "hardware": hw,
                    "topics": tp if isinstance(tp, list) else [tp],
                }
            )
        except Exception:
            continue

    total = len(items)
    paginated = items[offset : offset + limit]

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "documents": paginated,
    }


@app.get("/api/v1/documents/{doc_id:path}", tags=["Documents"])
def get_document(doc_id: str) -> dict[str, Any]:
    """Returns detail for a single document by ID or relative path."""
    doc_paths = get_all_documents(settings.docs_dir)

    for p in doc_paths:
        rel = str(p.relative_to(settings.docs_dir))
        try:
            fm, body = parse_frontmatter(p)
            current_id = fm.get("id") or rel
            if current_id == doc_id or rel == doc_id:
                hw = fm.get("hardware", [])
                tp = fm.get("topics", fm.get("tags", []))
                return {
                    "id": current_id,
                    "filepath": rel,
                    "title": fm.get("title", ""),
                    "category": fm.get("category", ""),
                    "difficulty": fm.get("difficulty", ""),
                    "language": fm.get("language", ""),
                    "hardware": hw,
                    "topics": tp if isinstance(tp, list) else [tp],
                    "frontmatter": fm,
                    "body": body.strip(),
                }
        except Exception:
            continue

    raise HTTPException(status_code=404, detail=f"Document with id/path '{doc_id}' not found.")


@app.get("/api/v1/dataset", tags=["Dataset"])
def get_dataset_info() -> dict[str, Any]:
    """Returns dataset info and file statistics."""
    info = {}
    for fname in ["scraped_dataset.jsonl", "api_index.json", "knowledge_graph.json"]:
        fpath = settings.dataset_dir / fname
        if fpath.is_file():
            stat = fpath.stat()
            info[fname] = {
                "exists": True,
                "size_bytes": stat.st_size,
                "size_mb": round(stat.st_size / (1024 * 1024), 2),
            }
        else:
            info[fname] = {"exists": False}
    return info


@app.get("/api/v1/manifest", tags=["Manifest"])
def get_manifest() -> dict[str, Any]:
    """Returns the current data/manifest.json contents."""
    if not settings.manifest_path.is_file():
        raise HTTPException(status_code=404, detail="Manifest file not found.")
    try:
        data = json.loads(settings.manifest_path.read_text(encoding="utf-8"))
        return cast(dict[str, Any], data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading manifest: {e}") from e


@app.get("/api/v1/knowledge-graph", tags=["Knowledge Graph"])
def get_knowledge_graph() -> dict[str, Any]:
    """Returns the knowledge graph JSON if available."""
    kg_path = settings.dataset_dir / "knowledge_graph.json"
    if not kg_path.is_file():
        raise HTTPException(status_code=404, detail="Knowledge graph file not found.")
    try:
        data = json.loads(kg_path.read_text(encoding="utf-8"))
        return cast(dict[str, Any], data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading knowledge graph: {e}") from e
