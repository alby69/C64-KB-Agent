---
id: src-e691-insert-uppercasegraphic-character
type: source
title: 'Source Summary: insert uppercase/graphic character'
aliases:
- insert uppercase/graphic character
- e691-insert-uppercasegraphic-character.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e691-insert-uppercasegraphic-character.md
  sha256: 31c2a9a7548d217752da4858211d22167bd6ef14df61d32f97e32f0eb89c6e0f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: insert uppercase/graphic character

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e691-insert-uppercasegraphic-character.md`
**SHA256**: `31c2a9a7548d217752da4858211d22167bd6ef14df61d32f97e32f0eb89c6e0f`

## Summary



# $E691 — insert uppercase/graphic character

## Disassemblatura
```assembly
.E691  09 40    ORA #$40   ; change to uppercase/graphic
.E693  A6 C7    LDX $C7   ; get the reverse flag
.E695  F0 02    BEQ $E699   ; branch if not reverse else .. insert reversed character
.E697  09 80    ORA #$80   ; reverse character
.E699  A6 D8    LDX $D8   ; get the insert count
.E69B  F0 02    BEQ $E69F   ; branch if none
.E69D  C6 D8    DEC $D8   ; else decrement the insert count
.E69F  AE 86 02 LDX $0286   ...
