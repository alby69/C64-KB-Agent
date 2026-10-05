---
id: src-f1e5-ausgabe-auf-band
type: source
title: 'Source Summary: Ausgabe auf Band'
aliases:
- Ausgabe auf Band
- f1e5-ausgabe-auf-band.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1e5-ausgabe-auf-band.md
  sha256: 71dd18c9b662426fff97fa96914a03a8ffa0080124499b94523259255296085c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Ausgabe auf Band

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f1e5-ausgabe-auf-band.md`
**SHA256**: `71dd18c9b662426fff97fa96914a03a8ffa0080124499b94523259255296085c`

## Summary



# $F1E5 — Ausgabe auf Band

## Disassemblatura
```assembly
.F1E5  20 0D F8 JSR $F80D   ; Bandpuffer Zeiger erhöhen
.F1E8  D0 0E    BNE $F1F8   ; verzweige wenn Puffer nicht voll
.F1EA  20 64 F8 JSR $F864   ; Puffer auf Band schreiben
.F1ED  B0 0E    BCS $F1FD   ; STOP-Taste, dann Abbruch
.F1EF  A9 02    LDA #$02   ; Kontrollbyte für Datenblock
.F1F1  A0 00    LDY #$00   ; Pufferzeiger auf 0
.F1F3  91 B2    STA ($B2),Y   ; Akku in Puffer schreiben
.F1F5  C8       INY   ; Zeiger erhöhen
.F1F6  8...
