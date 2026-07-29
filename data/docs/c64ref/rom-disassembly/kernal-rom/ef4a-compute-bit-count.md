---
title: compute bit count
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ef4a-berechnen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EF4A
  address_end: $EF58
  symbol: compute-bit-count
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF4A**: set bit count to 9, 8 data + 1 stop bit'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EF4A**: Zähler für Wortlänge'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EF4E**: M51CTR, 6551 control register image'
---

# $EF4A — compute bit count

## Disassemblatura
```assembly
.EF4A  A2 09    LDX #$09   ; set bit count to 9, 8 data + 1 stop bit
.EF4C  A9 20    LDA #$20   ; mask for 8/7 data bits
.EF4E  2C 93 02 BIT $0293   ; test pseudo 6551 control register
.EF51  F0 01    BEQ $EF54   ; branch if 8 bits
.EF53  CA       DEX   ; else decrement count for 7 data bits
.EF54  50 02    BVC $EF58   ; branch if 7 bits
.EF56  CA       DEX   ; else decrement count ..
.EF57  CA       DEX   ; .. for 5 data bits
.EF58  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EF4A**: set bit count to 9, 8 data + 1 stop bit
- **$EF4C**: mask for 8/7 data bits
- **$EF4E**: test pseudo 6551 control register
- **$EF51**: branch if 8 bits
- **$EF53**: else decrement count for 7 data bits
- **$EF54**: branch if 7 bits
- **$EF56**: else decrement count ..
- **$EF57**: .. for 5 data bits

### Commodore-64-intern-Buch (Commodore)
- **$EF4A**: Zähler für Wortlänge
- **$EF4C**: Maskenwert für Bit 5
- **$EF4E**: Testen vom RS-232 Kontrollregister
- **$EF51**: verzweige wenn Bit 5 gelöscht
- **$EF53**: Zähler für Wortlänge vermindern
- **$EF54**: verzweige wenn Bit 6 gelöscht
- **$EF56**: Wortlänge um zwei
- **$EF57**: vermindern
- **$EF58**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EF4E**: M51CTR, 6551 control register image

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*