---
id: src-f179-eingabe-vom-band
type: source
title: 'Source Summary: Eingabe vom Band'
aliases:
- Eingabe vom Band
- f179-eingabe-vom-band.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f179-eingabe-vom-band.md
  sha256: 1b551a53cf7a35a2407f69f37e9d7da620bf37ad05fccb135ca05d18525b0331
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Eingabe vom Band

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f179-eingabe-vom-band.md`
**SHA256**: `1b551a53cf7a35a2407f69f37e9d7da620bf37ad05fccb135ca05d18525b0331`

## Summary



# $F179 — Eingabe vom Band

## Disassemblatura
```assembly
.F179  86 97    STX $97   ; X-Register merken
.F17B  20 99 F1 JSR $F199   ; ein Zeichen vom Band holen
.F17E  B0 16    BCS $F196   ; verzweige bei Fehler
.F180  48       PHA   ; Akku retten
.F181  20 99 F1 JSR $F199   ; ein Zeichen vom Band holen
.F184  B0 0D    BCS $F193   ; verzweige bei Fehler
.F186  D0 05    BNE $F18D   ; letzes Zeichen ?
.F188  A9 40    LDA #$40   ; Code für 'End of Identify'
.F18A  20 1C FE JSR $FE1C   ; Status s...
