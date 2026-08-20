"""Test del processo di deduplicazione (H4).

Il text_cleaner supporta la rimozione di righe duplicate (deduplicate=True):
verifica che il processo produca output privi di duplicati senza perdere
l'ordine delle righe originali.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cleaners.text_cleaner import clean_text


class TestDeduplication:
    def test_deduplicate_removes_duplicate_lines(self):
        raw = "alpha\nbeta\nalpha\ngamma\nbeta\n"
        result = clean_text(raw, deduplicate=True)
        lines = [l for l in result.split("\n") if l.strip()]
        assert len(lines) == 3
        assert lines == ["alpha", "beta", "gamma"]

    def test_deduplicate_preserves_first_occurrence_order(self):
        raw = "one\ntwo\none\nthree\ntwo\n"
        result = clean_text(raw, deduplicate=True)
        lines = [l for l in result.split("\n") if l.strip()]
        assert lines == ["one", "two", "three"]

    def test_deduplicate_false_keeps_duplicates(self):
        raw = "same\nsame\n"
        result = clean_text(raw, deduplicate=False)
        assert result.count("same") == 2

    def test_deduplicate_empty_input(self):
        assert clean_text("", deduplicate=True) == ""
