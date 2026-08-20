import unittest

from cleaners.text_cleaner import clean_text


class TestDeduplication(unittest.TestCase):
    def test_deduplicate_exact_duplicates(self):
        raw = "alpha\nbeta\nalpha\ngamma\nbeta\n"
        result = clean_text(raw, deduplicate=True)
        lines = [line for line in result.split("\n") if line.strip()]
        assert len(lines) == 3
        assert lines == ["alpha", "beta", "gamma"]

    def test_deduplicate_preserves_order(self):
        raw = "one\ntwo\none\nthree\ntwo\n"
        result = clean_text(raw, deduplicate=True)
        lines = [line for line in result.split("\n") if line.strip()]
        assert lines == ["one", "two", "three"]

    def test_deduplicate_off_by_default(self):
        raw = "alpha\nalpha\n"
        result = clean_text(raw)
        assert result.count("alpha") == 2

    def test_deduplicate_empty_input(self):
        assert clean_text("", deduplicate=True) == ""
