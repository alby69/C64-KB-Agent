---
id: src-ab21-print-string-from-utility-pointer
type: source
title: 'Source Summary: print string from utility pointer'
aliases:
- print string from utility pointer
- ab21-print-string-from-utility-pointer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab21-print-string-from-utility-pointer.md
  sha256: b6f7b274f36fce1329ae60f2818af3e23ca30417b2e3bd5ea98f16b020b60cc0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print string from utility pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ab21-print-string-from-utility-pointer.md`
**SHA256**: `b6f7b274f36fce1329ae60f2818af3e23ca30417b2e3bd5ea98f16b020b60cc0`

## Summary



# $AB21 — print string from utility pointer

## Disassemblatura
```assembly
.AB21  20 A6 B6 JSR $B6A6   ; pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.AB24  AA       TAX   ; copy length
.AB25  A0 00    LDY #$00   ; clear index
.AB27  E8       INX   ; increment length, for pre decrement loop
.AB28  CA       DEX   ; decrement length
.AB29  F0 BC    BEQ $AAE7   ; exit if done
.AB2B  B1 22    LDA ($22),Y   ; get ...
