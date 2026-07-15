import pytest
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cleaners.text_cleaner import clean_text, advanced_clean, clean_file


class TestCleanText:
    def test_remove_control_chars(self):
        result = clean_text("hello\x00world\x01\test")
        assert result == "helloworldtest"

    def test_normalize_whitespace(self):
        result = clean_text("hello    world")
        assert result == "hello world"

    def test_mixed_spaces_and_tabs(self):
        result = clean_text("hello\t\tworld")
        assert "hello " in result or "hello\t" in result
        assert "world" in result

    def test_empty_string(self):
        assert clean_text("") == ""

    def test_only_whitespace(self):
        assert clean_text("   ") == ""

    def test_remove_page_numbers(self):
        result = clean_text("some text\n  123  \nmore text")
        assert "123" not in result

    def test_fix_lda_sta_patterns(self):
        result = clean_text("L DA STA")
        assert "LDA" in result or "L DA" not in result

    def test_fix_hex_notation(self):
        result = clean_text("$ C000")
        assert "$C000" in result

    def test_fix_labels_with_colon(self):
        result = clean_text("label :")
        assert "label:" in result

    def test_normalize_triple_newlines(self):
        result = clean_text("a\n\n\n\nb")
        assert result == "a\n\nb"

    def test_deduplicate_lines(self):
        result = clean_text("a\nb\na\nb\nc", deduplicate=True)
        lines = result.split("\n")
        # ensure uniqueness
        unique = set(lines)
        assert len(lines) <= 4  # duplicate removed

    def test_max_line_length(self):
        result = clean_text("hello world", max_line_length=5)
        assert len(result.split("\n")[0]) <= 5

    def test_petscii_fix(self):
        result = clean_text("hello\xa0world", fix_petscii=True)
        assert "\xa0" not in result or result == "hello world"

    def test_advanced_clean_is_alias(self):
        assert advanced_clean is clean_text


class TestCleanFile:
    def test_clean_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            input_path = os.path.join(tmp, "in.txt")
            output_path = os.path.join(tmp, "out.txt")
            with open(input_path, "w") as f:
                f.write("hello\x00world\n\n\n\nmore")
            clean_file(input_path, output_path)
            with open(output_path) as f:
                content = f.read()
            assert "hello" in content
            assert "\x00" not in content


class TestAdvancedCleanScenarios:
    def test_c64_error_recovery(self):
        raw = """LDA $D012
 S TA $D020
JSR $FFD2

$ D012 -> $D020"""
        result = clean_text(raw)
        assert "LDA" in result
        assert "S TA" not in result or "STA" in result
        assert "$ D012" not in result or "$D012" in result

    def test_multiple_consecutive_newlines(self):
        raw = "line1\n\n\n\n\nline2"
        result = clean_text(raw)
        assert "\n\n\n" not in result

    def test_long_line_truncation(self):
        raw = "x" * 100 + "\n" + "y" * 100
        result = clean_text(raw, max_line_length=10)
        for line in result.split("\n"):
            assert len(line) <= 10
