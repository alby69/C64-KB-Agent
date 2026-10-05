---
id: src-making-a-counter
type: source
title: 'Source Summary: base:making_a_counter [Codebase64 wiki]'
aliases:
- base:making_a_counter [Codebase64 wiki]
- making_a_counter.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/making_a_counter.md
  sha256: 20f75eba752ca9699b18389c7b5c28e55d234ae58e5d3225c58b0a1260f2d457
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:making_a_counter [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/making_a_counter.md`
**SHA256**: `20f75eba752ca9699b18389c7b5c28e55d234ae58e5d3225c58b0a1260f2d457`

## Summary



# base:making_a_counter [Codebase64 wiki]

base:making_a_counter

                A quite nifty example of how to make an increasing decimal counter with a flexible amount of digits. It's possible to create a counter with up to 255 digits.

Useful for counting scores in games, for example.

```
; Counter code
; [c]2007 Scout/Silicon Ltd.
numdigits = 6
      *=$c000
      ldx #0
      txa         ; A=X=0
-
      sta tellertabel,x   ; erase the countertable
      inx
      cpx #numdigits      ; ...
