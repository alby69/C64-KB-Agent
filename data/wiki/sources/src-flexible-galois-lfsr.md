---
id: src-flexible-galois-lfsr
type: source
title: 'Source Summary: base:flexible_galois_lfsr [Codebase64 wiki]'
aliases:
- base:flexible_galois_lfsr [Codebase64 wiki]
- flexible_galois_lfsr.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/flexible_galois_lfsr.md
  sha256: 344c2f9a6fa355175d4567a202f1a0370e81148988bd3a2d0a2f8aebcf99712c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:flexible_galois_lfsr [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/flexible_galois_lfsr.md`
**SHA256**: `344c2f9a6fa355175d4567a202f1a0370e81148988bd3a2d0a2f8aebcf99712c`

## Summary



# base:flexible_galois_lfsr [Codebase64 wiki]

base:flexible_galois_lfsr

                This is a very simple yet flexible PRNG. It can be configured for 2..16 bits of randomness. Thanks to Zed Yago for providing the proper tap sequences. They are taken from “Graphics Gems”.

Tap Sequences

LFSR Term -> Period
-------------------
$03 -> 1..$03
$06 -> 1..$07
$0c -> 1..$0f
$14 -> 1..$1f
$30 -> 1..$3f
$60 -> 1..$7f
$b8 -> 1..$ff
$0110 -> 1..$01ff
$0240 -> 1..$03ff
$0500 -> 1..$07ff
$0ca0 -> 1.....
