---
id: src-bdcd-print-xa-as-unsigned-integer
type: source
title: 'Source Summary: print XA as unsigned integer'
aliases:
- print XA as unsigned integer
- bdcd-print-xa-as-unsigned-integer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bdcd-print-xa-as-unsigned-integer.md
  sha256: d246bd0bf212a9fb4a547d1360cb6614ebd893c1ff71c07c5e2b4f5c94566930
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print XA as unsigned integer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bdcd-print-xa-as-unsigned-integer.md`
**SHA256**: `d246bd0bf212a9fb4a547d1360cb6614ebd893c1ff71c07c5e2b4f5c94566930`

## Summary



# $BDCD — print XA as unsigned integer

## Disassemblatura
```assembly
.BDCD  85 62    STA $62   ; save high byte as FAC1 mantissa1
.BDCF  86 63    STX $63   ; save low byte as FAC1 mantissa2
.BDD1  A2 90    LDX #$90   ; set exponent to 16d bits
.BDD3  38       SEC   ; set integer is +ve flag
.BDD4  20 49 BC JSR $BC49   ; set exponent = X, clear mantissa 4 and 3 and normalise FAC1
.BDD7  20 DF BD JSR $BDDF   ; convert FAC1 to string
.BDDA  4C 1E AB JMP $AB1E   ; print null terminated string
``...
