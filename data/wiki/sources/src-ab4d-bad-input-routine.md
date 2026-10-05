---
id: src-ab4d-bad-input-routine
type: source
title: 'Source Summary: bad input routine'
aliases:
- bad input routine
- ab4d-bad-input-routine.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab4d-bad-input-routine.md
  sha256: 052f48fef9d637b3745248566312b492212774154c6a82a60c32d558b6810c25
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: bad input routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ab4d-bad-input-routine.md`
**SHA256**: `052f48fef9d637b3745248566312b492212774154c6a82a60c32d558b6810c25`

## Summary



# $AB4D — bad input routine

## Disassemblatura
```assembly
.AB4D  A5 11    LDA $11   ; get INPUT mode flag, $00 = INPUT, $40 = GET, $98 = READ
.AB4F  F0 11    BEQ $AB62   ; branch if INPUT
.AB51  30 04    BMI $AB57   ; branch if READ else was GET
.AB53  A0 FF    LDY #$FF   ; set current line high byte to -1, indicate immediate mode
.AB55  D0 04    BNE $AB5B   ; branch always
.AB57  A5 3F    LDA $3F   ; get current DATA line number low byte
.AB59  A4 40    LDY $40   ; get current DATA line num...
