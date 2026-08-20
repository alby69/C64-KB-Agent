"""Configuration settings for C64-KB-Agent using Pydantic Settings."""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base repo root path (c64_kb_agent/.. -> repo root)
_REPO_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    model_config = SettingsConfigDict(
        env_prefix="C64KB_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    base_dir: Path = Field(default_factory=lambda: _REPO_ROOT)
    docs_dir: Path = Field(default_factory=lambda: _REPO_ROOT / "data" / "docs")
    dataset_dir: Path = Field(default_factory=lambda: _REPO_ROOT / "data" / "dataset")
    schemas_dir: Path = Field(default_factory=lambda: _REPO_ROOT / "schemas")
    db_path: Path = Field(
        default_factory=lambda: _REPO_ROOT / "data" / "dataset" / "search_index.db"
    )
    manifest_path: Path = Field(default_factory=lambda: _REPO_ROOT / "data" / "manifest.json")

    log_level: str = "INFO"
    api_host: str = "127.0.0.1"
    api_port: int = 8001


settings = Settings()
