---
id: src-a480-eingabe-warteschleife
type: source
title: 'Source Summary: Eingabe-Warteschleife'
aliases:
- Eingabe-Warteschleife
- a480-eingabe-warteschleife.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a480-eingabe-warteschleife.md
  sha256: ce639098591b0e4eb04591521062f3b36e58a68cccd604558084672a71cfcd27
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Eingabe-Warteschleife

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a480-eingabe-warteschleife.md`
**SHA256**: `ce639098591b0e4eb04591521062f3b36e58a68cccd604558084672a71cfcd27`

## Summary



# $A480 — Eingabe-Warteschleife

## Disassemblatura
```assembly
.A480  6C 02 03 JMP ($0302)   ; JMP $A483
.A483  20 60 A5 JSR $A560   ; BASIC-Zeile nach Eingabepuffer
.A486  86 7A    STX $7A   ; CHRGET Zeiger auf
.A488  84 7B    STY $7B   ; Eingabepuffer
.A48A  20 73 00 JSR $0073   ; nächstes Zeichen holen
.A48D  AA       TAX   ; Puffer leer?
.A48E  F0 F0    BEQ $A480   ; Ja: dann weiter warten
.A490  A2 FF    LDX #$FF   ; Wert für
.A492  86 3A    STX $3A   ; Kennzeichen für Direktmodus
.A494 ...
