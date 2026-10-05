---
id: src-bae2-multiply-fac1-by-10
type: source
title: 'Source Summary: multiply FAC1 by 10'
aliases:
- multiply FAC1 by 10
- bae2-multiply-fac1-by-10.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bae2-multiply-fac1-by-10.md
  sha256: e76c46076a143b2b39d8b34d8471b197548941af85f8f096facd70a9eeb4a541
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: multiply FAC1 by 10

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bae2-multiply-fac1-by-10.md`
**SHA256**: `e76c46076a143b2b39d8b34d8471b197548941af85f8f096facd70a9eeb4a541`

## Summary



# $BAE2 — multiply FAC1 by 10

## Disassemblatura
```assembly
.BAE2  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.BAE5  AA       TAX   ; copy exponent (set the flags)
.BAE6  F0 10    BEQ $BAF8   ; exit if zero
.BAE8  18       CLC   ; clear carry for add
.BAE9  69 02    ADC #$02   ; add two to exponent (*4)
.BAEB  B0 F2    BCS $BADF   ; do overflow error if > $FF FAC1 = (FAC1 + FAC2) * 2
.BAED  A2 00    LDX #$00   ; clear byte
.BAEF  86 6F    STX $6F   ; clear sign compare (FAC1 EOR FAC2...
