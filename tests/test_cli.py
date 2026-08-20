"""Tests for c64_kb_agent/cli.py and c64_kb_agent/cli_handlers.py."""

import json

from c64_kb_agent.cli import main
from c64_kb_agent.cli_handlers import (
    cmd_quality_report,
    cmd_rebuild_index,
    cmd_search,
    cmd_status,
)


def test_cli_status(capsys):
    ret = main(["status", "--format", "json"])
    assert ret == 0
    captured = capsys.readouterr().out
    data = json.loads(captured)
    assert "documents" in data


def test_cli_search(capsys):
    ret = main(["search", "sprite", "--format", "json"])
    assert ret == 0
    captured = capsys.readouterr().out
    data = json.loads(captured)
    assert "results" in data


def test_cli_quality_report(capsys):
    ret = main(["quality-report", "--format", "json"])
    assert ret == 0
    captured = capsys.readouterr().out
    data = json.loads(captured)
    assert "total_documents" in data


def test_cli_validate(capsys):
    ret = main(["validate", "--format", "json"])
    assert ret in [0, 1]
    captured = capsys.readouterr().out
    data = json.loads(captured)
    assert "passed" in data


def test_cli_handlers_text_output(capsys):
    assert cmd_status(output_format="text") == 0
    assert cmd_rebuild_index(output_format="text") == 0
    assert cmd_search("sprite", output_format="text") == 0
    assert cmd_quality_report(output_format="text") == 0
