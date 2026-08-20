"""Tests for FastAPI REST API endpoints in c64_kb_agent/server/api.py."""

from fastapi.testclient import TestClient

from c64_kb_agent.config import settings
from c64_kb_agent.server.api import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"


def test_kb_status_endpoint():
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    data = response.json()
    assert "documents" in data
    assert "dataset_files" in data
    assert "search_index" in data


def test_validate_endpoint():
    response = client.post("/api/v1/validate")
    assert response.status_code == 200
    data = response.json()
    assert "passed" in data
    assert "documents" in data


def test_rebuild_and_search_endpoints():
    rebuild_res = client.post("/api/v1/index/rebuild")
    assert rebuild_res.status_code == 200
    rdata = rebuild_res.json()
    assert rdata["status"] == "success"
    assert rdata["indexed_documents"] > 0

    search_res = client.get("/api/v1/search?query=sprite&limit=5")
    assert search_res.status_code == 200
    sdata = search_res.json()
    assert sdata["query"] == "sprite"
    assert "results" in sdata
    assert len(sdata["results"]) > 0


def test_documents_list_and_detail_endpoints():
    response = client.get("/api/v1/documents?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "documents" in data
    assert len(data["documents"]) <= 5

    if data["documents"]:
        first_id = data["documents"][0]["id"]
        detail_res = client.get(f"/api/v1/documents/{first_id}")
        assert detail_res.status_code == 200
        detail_data = detail_res.json()
        assert detail_data["id"] == first_id
        assert "frontmatter" in detail_data
        assert "body" in detail_data


def test_dataset_and_manifest_endpoints():
    ds_res = client.get("/api/v1/dataset")
    assert ds_res.status_code == 200
    assert "scraped_dataset.jsonl" in ds_res.json()

    man_res = client.get("/api/v1/manifest")
    assert man_res.status_code == 200
    assert "schema_version" in man_res.json()


def test_knowledge_graph_endpoint():
    res = client.get("/api/v1/knowledge-graph")
    if (settings.dataset_dir / "knowledge_graph.json").is_file():
        assert res.status_code == 200
        assert "nodes" in res.json()
    else:
        assert res.status_code == 404
