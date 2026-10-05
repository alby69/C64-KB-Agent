---
id: src-shift-and-add-multiplication
type: source
title: 'Source Summary: Shift-and-add multiplication'
aliases:
- Shift-and-add multiplication
- shift-and-add_multiplication.md
tags:
- basic
- assembly
- memory management
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/shift-and-add_multiplication.md
  sha256: 67dcd39cd80e1e85585d6792cb1f124cb3c97beb74a750e4dc62e3732cd70e57
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Shift-and-add multiplication

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/shift-and-add_multiplication.md`
**SHA256**: `67dcd39cd80e1e85585d6792cb1f124cb3c97beb74a750e4dc62e3732cd70e57`

## Summary



# Shift-and-add multiplication

## The main algorithm behind Elite's many multiplication routines

Elite implements multiplication using the shift-and-add algorithm. One such example is the [MULT1](https://elite.bbcelite.com/cassette/main/subroutine/mult1.html) routine, which multiplies two 8-bit numbers to give a 16-bit result). Let's take a look at how it does it, as this same technique is used in lots of different multiplication routines throughout the game code (such as [FMLTU](https://eli...
