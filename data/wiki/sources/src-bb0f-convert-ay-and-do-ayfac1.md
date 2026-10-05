---
id: src-bb0f-convert-ay-and-do-ayfac1
type: source
title: 'Source Summary: convert AY and do (AY)/FAC1'
aliases:
- convert AY and do (AY)/FAC1
- bb0f-convert-ay-and-do-ayfac1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bb0f-convert-ay-and-do-ayfac1.md
  sha256: ebc02d265dc6876aeaa25900e2188aaae03b361dd51cda5a90255a631540f7a4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: convert AY and do (AY)/FAC1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bb0f-convert-ay-and-do-ayfac1.md`
**SHA256**: `ebc02d265dc6876aeaa25900e2188aaae03b361dd51cda5a90255a631540f7a4`

## Summary



# $BB0F — convert AY and do (AY)/FAC1

## Disassemblatura
```assembly
.BB0F  20 8C BA JSR $BA8C   ; unpack memory (AY) into FAC2
.BB12  F0 76    BEQ $BB8A   ; if zero go do /0 error
.BB14  20 1B BC JSR $BC1B   ; round FAC1
.BB17  A9 00    LDA #$00   ; clear A
.BB19  38       SEC   ; set carry for subtract
.BB1A  E5 61    SBC $61   ; subtract FAC1 exponent (2s complement)
.BB1C  85 61    STA $61   ; save FAC1 exponent
.BB1E  20 B7 BA JSR $BAB7   ; test and adjust accumulators
.BB21  E6 61    IN...
