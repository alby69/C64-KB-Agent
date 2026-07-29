---
title: set serial bus input device
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
  address: $F237
  address_end: $F24D
  symbol: set-serial-bus-input-device
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F237**: Geräteadresse retten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F237 — set serial bus input device

## Disassemblatura
```assembly
.F237  AA       TAX
.F238  20 09 ED JSR $ED09
.F23B  A5 B9    LDA $B9
.F23D  10 06    BPL $F245
.F23F  20 CC ED JSR $EDCC
.F242  4C 48 F2 JMP $F248
.F245  20 C7 ED JSR $EDC7
.F248  8A       TXA
.F249  24 90    BIT $90
.F24B  10 E6    BPL $F233
.F24D  4C 07 F7 JMP $F707
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F237**: Geräteadresse retten
- **$F238**: TALK senden
- **$F23B**: Sekundäradresse laden
- **$F23D**: verzweige wenn kleiner 128
- **$F23F**: wartet auf Takt-Signal
- **$F242**: nächsten Befehl überspringen
- **$F245**: Sekundäradresse für TALK senden
- **$F248**: Geräteadresse wiederholen
- **$F249**: Status abfragen
- **$F24B**: verzweige wenn ok
- **$F24D**: sonst 'DEVICE NOT PRESENT'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*