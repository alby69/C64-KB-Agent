"""Test suite for data/manifest.json generation and validation."""

from jsonschema import validate

import kbvalidate
from scripts.generate_manifest import generate_manifest


def test_generate_manifest_validation():
    manifest_data = generate_manifest()
    manifest_schema = kbvalidate.load_schema("manifest.schema.json")
    validate(instance=manifest_data, schema=manifest_schema)

    assert manifest_data["schema_version"] == 1
    assert "generated_at" in manifest_data
    assert manifest_data["documents"]["total"] > 0
    assert "dataset_files" in manifest_data
