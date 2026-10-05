---
id: src-b91d-postshift
type: source
title: 'Source Summary: postshift'
aliases:
- postshift
- b91d-postshift.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b91d-postshift.md
  sha256: efe1d8eefe1caec8947d61ccee5e81f2210bff3b9e23bbdff707729fa8a138ba
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: postshift

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b91d-postshift.md`
**SHA256**: `efe1d8eefe1caec8947d61ccee5e81f2210bff3b9e23bbdff707729fa8a138ba`

## Summary



# $B91D — postshift

## Disassemblatura
```assembly
.B91D  69 01    ADC #$01
.B91F  06 70    ASL $70
.B921  26 65    ROL $65
.B923  26 64    ROL $64
.B925  26 63    ROL $63
.B927  26 62    ROL $62
.B929  10 F2    BPL $B91D
.B92B  38       SEC
.B92C  E5 61    SBC $61
.B92E  B0 C7    BCS $B8F7
.B930  49 FF    EOR #$FF
.B932  69 01    ADC #$01
.B934  85 61    STA $61
.B936  90 0E    BCC $B946
.B938  E6 61    INC $61
.B93A  F0 42    BEQ $B97E
.B93C  66 62    ROR $62
.B93E  66 63    ROR $63
.B940  ...
