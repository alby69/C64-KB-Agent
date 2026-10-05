---
id: src-ad9e-evaluate-expression
type: source
title: 'Source Summary: evaluate expression'
aliases:
- evaluate expression
- ad9e-evaluate-expression.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ad9e-evaluate-expression.md
  sha256: fdb71378763ed4b0dc317f1cbdaf44b3f436e360f84e5bafea5c0ad961a44e5b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: evaluate expression

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ad9e-evaluate-expression.md`
**SHA256**: `fdb71378763ed4b0dc317f1cbdaf44b3f436e360f84e5bafea5c0ad961a44e5b`

## Summary



# $AD9E — evaluate expression

## Disassemblatura
```assembly
.AD9E  A6 7A    LDX $7A   ; get BASIC execute pointer low byte
.ADA0  D0 02    BNE $ADA4   ; skip next if not zero
.ADA2  C6 7B    DEC $7B   ; else decrement BASIC execute pointer high byte
.ADA4  C6 7A    DEC $7A   ; decrement BASIC execute pointer low byte
.ADA6  A2 00    LDX #$00   ; set null precedence, flag done
.ADA8  24       .BYTE $24   ; makes next line BIT $48
.ADA9  48       PHA   ; push compare evaluation byte if branch ...
