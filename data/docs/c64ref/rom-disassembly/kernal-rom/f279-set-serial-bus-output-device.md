---
title: set serial bus output device
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $F279
  address_end: $F28E
  symbol: set-serial-bus-output-device
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F279**: Geräteadresse retten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

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