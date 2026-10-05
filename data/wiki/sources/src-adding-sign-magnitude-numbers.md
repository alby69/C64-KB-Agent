---
id: src-adding-sign-magnitude-numbers
type: source
title: 'Source Summary: Adding sign-magnitude numbers'
aliases:
- Adding sign-magnitude numbers
- adding_sign-magnitude_numbers.md
tags:
- basic
- assembly
- memory management
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/adding_sign-magnitude_numbers.md
  sha256: a47194bc332243f772e40f58a1e085391d2183426b49f0d21435417fbcf62372
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Adding sign-magnitude numbers

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/adding_sign-magnitude_numbers.md`
**SHA256**: `a47194bc332243f772e40f58a1e085391d2183426b49f0d21435417fbcf62372`

## Summary



# Adding sign-magnitude numbers

## Doing basic arithmetic with sign-magnitude numbers

Elite uses a lot of sign-magnitude numbers, where the sign bit is stored separately from an unsigned magnitude. The classic examples are the ship coordinates at INWK, which are stored in 24 bits as (x_sign x_hi x_lo), where bit 7 of x_sign is the sign, and (x_hi x_lo) is the coordinate value.

This means that when we come to do arithmetic on sign-magnitude numbers, we have to write our own routines for ever...
