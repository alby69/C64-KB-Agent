---
id: src-ef3b-set-via-2-icr-from-a
type: source
title: 'Source Summary: set VIA 2 ICR from A'
aliases:
- set VIA 2 ICR from A
- ef3b-set-via-2-icr-from-a.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef3b-set-via-2-icr-from-a.md
  sha256: a2c31750414343dfb3fc3ac0ccfff07eb52e33d70c1e593ec6d1d8f5437dafaf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set VIA 2 ICR from A

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef3b-set-via-2-icr-from-a.md`
**SHA256**: `a2c31750414343dfb3fc3ac0ccfff07eb52e33d70c1e593ec6d1d8f5437dafaf`

## Summary



# $EF3B — set VIA 2 ICR from A

## Disassemblatura
```assembly
.EF3B  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.EF3E  4D A1 02 EOR $02A1   ; EOR with the RS-232 interrupt enable byte
.EF41  09 80    ORA #$80   ; set the interrupts enable bit
.EF43  8D A1 02 STA $02A1   ; save the RS-232 interrupt enable byte
.EF46  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.EF49  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EF3B**: save VIA 2 ICR
- **$EF3E**: EOR with the RS-232 interrupt enable ...
