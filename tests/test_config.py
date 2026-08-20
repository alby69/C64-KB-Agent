"""Tests for c64_kb_agent/config.py and utils/logging.py."""

from c64_kb_agent.config import Settings
from c64_kb_agent.utils.logging import setup_logging


def test_settings_defaults():
    s = Settings()
    assert s.log_level in ["INFO", "DEBUG", "WARN", "ERROR"]
    assert s.docs_dir.exists()
    assert s.schemas_dir.exists()


def test_logging_setup():
    logger = setup_logging("DEBUG")
    assert logger is not None
