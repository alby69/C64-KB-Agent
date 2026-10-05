---
id: ab62-fehler-bei-input
type: entity
title: Fehler bei INPUT
aliases:
- Fehler bei INPUT
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab62-fehler-bei-input.md
  sha256: e36afd4a561ff6c05b65743114fd03027099ffbb863f8216113668ac8096b6d2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ab62-fehler-bei-input
---

# Fehler bei INPUT



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

## References
- Source: [[src-ab62-fehler-bei-input]]
