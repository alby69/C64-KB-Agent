import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cleaners.text_cleaner import advanced_clean, clean_file, clean_text


class TestTextCleaner:
    def test_basic_cleaning(self):
        text = "  Hello   World!  \n\n  This is   a test.  "
        expected = "Hello World!\nThis is a test."
        assert clean_text(text) == expected

    def test_advanced_cleaning(self):
        text = "Some text with \x00 null bytes and \x08 backspaces."
        expected = "Some text with null bytes and backspaces."
        assert advanced_clean(text) == expected

    def test_unprintable_characters(self):
        text = "Line 1\x01\x02\nLine 2\x03\x04"
        expected = "Line 1\nLine 2"
        assert clean_text(text) == expected

    def test_file_cleaning(self):
        content = "  Dirty   file   content.  \n\n\n  More dirty   content.  "
        expected = "Dirty file content.\nMore dirty content."

        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, encoding="utf-8"
        ) as temp_in:
            temp_in.write(content)
            temp_in_path = temp_in.name

        temp_out_path = temp_in_path + ".out"

        try:
            clean_file(temp_in_path, temp_out_path)
            with open(temp_out_path, encoding="utf-8") as f:
                result = f.read()
            assert result == expected
        finally:
            if os.path.exists(temp_in_path):
                os.remove(temp_in_path)
            if os.path.exists(temp_out_path):
                os.remove(temp_out_path)

    def test_deduplicate_lines(self):
        text = "Line 1\nLine 2\nLine 1\nLine 3\nLine 2"
        result = clean_text(text, deduplicate=True)
        lines = result.split("\n")
        assert len(lines) <= 4  # duplicate removed
        assert "Line 1" in lines
        assert "Line 2" in lines
        assert "Line 3" in lines

    def test_deduplicate_disabled_by_default(self):
        text = "Line 1\nLine 1"
        result = clean_text(text)
        assert result.count("Line 1") == 2
