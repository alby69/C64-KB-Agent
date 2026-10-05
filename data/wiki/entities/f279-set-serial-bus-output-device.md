---
id: f279-set-serial-bus-output-device
type: entity
title: set serial bus output device
aliases:
- set serial bus output device
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f279-set-serial-bus-output-device.md
  sha256: 6b6e5a207110f629f7eccac810a5e9f5e1badbb620849ebd7131e0510128dbad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f279-set-serial-bus-output-device
---

# set serial bus output device



# $F279 — set serial bus output device

## Disassemblatura
```assembly
.F279  AA       TAX
.F27A  20 0C ED JSR $ED0C
.F27D  A5 B9    LDA $B9
.F27F  10 05    BPL $F286
.F281  20 BE ED JSR $EDBE
.F284  D0 03    BNE $F289
.F286  20 B9 ED JSR $EDB9
.F289  8A       TXA
.F28A  24 90    BIT $90
.F28C  10 E7    BPL $F275
.F28E  4C 07 F7 JMP $F707
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F279**: Geräteadresse retten
- **$F27A**: LISTEN senden
- **$F27D**: Sekundäradresse laden
- **$F27F**: verzweige wenn kleiner 128
- **$F281**: ATN zurücksetzen
- **$F284**: unbedingter Sprung
- **$F286**: Sekundäradresse für LISTEN senden
- **$F289**: Geräteadresse wiederholen
- **$F28A**: Status abfragen
- **$F28C**: verzweige wenn ok
- **$F28E**: 'device not present'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f279-set-serial-bus-output-device]]
