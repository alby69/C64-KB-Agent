---
title: Fehler bei INPUT
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00d7-data
- ab62-fehler-bei-input
- input
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AB62
  address_end: $AB7A
  symbol: fehler-bei-input
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AB62**: Nummer des Eingabegeräts'
---

# $AB62 — Fehler bei INPUT

## Disassemblatura
```assembly
.AB62  A5 13    LDA $13   ; Nummer des Eingabegeräts
.AB64  F0 05    BEQ $AB6B   ; Tastatur: 'REDO FROM START'
.AB66  A2 18    LDX #$18   ; Nummer für 'FILE DATA'
.AB68  4C 37 A4 JMP $A437   ; Fehlermeldung ausgeben
.AB6B  A9 0C    LDA #$0C   ; Zeiger in Akku und Y-Reg.
.AB6D  A0 AD    LDY #$AD   ; auf '?REDO FROM START'
.AB6F  20 1E AB JSR $AB1E   ; String ausgeben
.AB72  A5 3D    LDA $3D   ; Werte holen und
.AB74  A4 3E    LDY $3E   ; Programmzeiger
.AB76  85 7A    STA $7A   ; zurücksetzen
.AB78  84 7B    STY $7B   ; auf INPUT-Befehl
.AB7A  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AB62**: Nummer des Eingabegeräts
- **$AB64**: Tastatur: 'REDO FROM START'
- **$AB66**: Nummer für 'FILE DATA'
- **$AB68**: Fehlermeldung ausgeben
- **$AB6B**: Zeiger in Akku und Y-Reg.
- **$AB6D**: auf '?REDO FROM START'
- **$AB6F**: String ausgeben
- **$AB72**: Werte holen und
- **$AB74**: Programmzeiger
- **$AB76**: zurücksetzen
- **$AB78**: auf INPUT-Befehl
- **$AB7A**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*