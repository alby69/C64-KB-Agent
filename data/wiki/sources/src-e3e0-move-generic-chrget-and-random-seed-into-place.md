---
id: src-e3e0-move-generic-chrget-and-random-seed-into-place
type: source
title: 'Source Summary: MOVE GENERIC CHRGET AND RANDOM SEED INTO PLACE'
aliases:
- MOVE GENERIC CHRGET AND RANDOM SEED INTO PLACE
- e3e0-move-generic-chrget-and-random-seed-into-place.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e3e0-move-generic-chrget-and-random-seed-into-place.md
  sha256: 62b017631e551fd0b62765d7263765959aeb7dd478ba3c7eb4962213c7bc41e1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MOVE GENERIC CHRGET AND RANDOM SEED INTO PLACE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e3e0-move-generic-chrget-and-random-seed-into-place.md`
**SHA256**: `62b017631e551fd0b62765d7263765959aeb7dd478ba3c7eb4962213c7bc41e1`

## Summary



# $E3E0 — MOVE GENERIC CHRGET AND RANDOM SEED INTO PLACE

## Disassemblatura
```assembly
.E3E0  A2 1C    LDX #$1C
.E3E2  BD A2 E3 LDA $E3A2,X
.E3E5  95 73    STA $73,X
.E3E7  CA       DEX
.E3E8  10 F8    BPL $E3E2
.E3EA  A9 03    LDA #$03   ; SET LENGTH OF TEMP. STRING DESCRIPTORS
.E3EC  85 53    STA $53   ; FOR GARBAGE COLLECTION SUBROUTINE
.E3EE  A9 00    LDA #$00
.E3F0  85 68    STA $68
.E3F2  85 13    STA $13
.E3F4  85 18    STA $18
.E3F6  A2 01    LDX #$01   ; SET UP FAKE FORWARD LINK
.E3...
