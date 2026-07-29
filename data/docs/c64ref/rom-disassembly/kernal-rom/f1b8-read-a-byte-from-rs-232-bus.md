---
title: read a byte from RS-232 bus
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
  address: $F1B8
  address_end: $F1C8
  symbol: read-a-byte-from-rs-232-bus
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F1B8**: ein Byte von RS 232 holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F1B8 — read a byte from RS-232 bus

## Disassemblatura
```assembly
.F1B8  20 4E F1 JSR $F14E
.F1BB  B0 F7    BCS $F1B4
.F1BD  C9 00    CMP #$00
.F1BF  D0 F2    BNE $F1B3
.F1C1  AD 97 02 LDA $0297
.F1C4  29 60    AND #$60
.F1C6  D0 E9    BNE $F1B1
.F1C8  F0 EE    BEQ $F1B8
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F1B8**: ein Byte von RS 232 holen
- **$F1BB**: verzweige wenn Fehler
- **$F1BD**: vergleiche mit Nullbyte
- **$F1BF**: nein, dann ok
- **$F1C1**: Status laden
- **$F1C4**: fehlt DSR ?
- **$F1C6**: ja, 'CR' zurückgeben
- **$F1C8**: nein, neuer Versuch

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*