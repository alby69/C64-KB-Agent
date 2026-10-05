---
id: src-generating-random-numbers
type: source
title: 'Source Summary: Generating random numbers'
aliases:
- Generating random numbers
- generating_random_numbers.md
tags:
- basic
- assembly
- memory management
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/generating_random_numbers.md
  sha256: a063041fc195d5dbd3de5269f53eb124e50e3708fb5aebaf43e1d1d1f125cf33
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Generating random numbers

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/generating_random_numbers.md`
**SHA256**: `a063041fc195d5dbd3de5269f53eb124e50e3708fb5aebaf43e1d1d1f125cf33`

## Summary



# Generating random numbers

## The algorithm behind Elite's random number generation routines

Games like Elite need a steady stream of random numbers. They are used all over the place to add an element of chance to gameplay, whether it's in the main flight loop when deciding whether or not to spawn an angry Thargoid in the depths of space, or on arrival in a new system where the market prices have a random element mixed into the procedural generation, so they are never exactly the same.

Ran...
