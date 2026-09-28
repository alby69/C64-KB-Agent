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


def test_cli_wiki_lint_json(capsys):
    ret = main(["wiki", "lint", "--format", "json"])
    assert ret in [0, 1]
    captured = capsys.readouterr().out
    data = json.loads(captured)
    assert "total_pages_scanned" in data
    assert "invalid_schema" in data


def test_cli_wiki_subcommands_format_options(capsys):
    assert main(["wiki", "link", "--format", "json"]) == 0
    captured = capsys.readouterr().out
    assert "pages_processed" in captured

    assert main(["wiki", "synthesize", "--format", "json"]) == 0
    captured = capsys.readouterr().out
    assert "index_path" in captured

    assert main(["wiki", "rebuild-index", "--format", "json"]) == 0
    captured = capsys.readouterr().out
    assert "total_indexed" in captured

    assert main(["wiki", "query", "sprite", "--format", "json"]) == 0
    captured = capsys.readouterr().out
    data = json.loads(captured)
    assert isinstance(data, dict)
    assert "results" in data
