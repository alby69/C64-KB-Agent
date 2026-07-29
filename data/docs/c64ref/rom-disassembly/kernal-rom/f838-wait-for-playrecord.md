---
title: wait for PLAY/RECORD
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
- f838-schreiben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F838
  address_end: $F83F
  symbol: wait-for-playrecord
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F838**: return the cassette sense in Zb'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F838**: fragt Bandtaste ab'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F838 — wait for PLAY/RECORD

## Disassemblatura
```assembly
.F838  20 2E F8 JSR $F82E   ; return the cassette sense in Zb
.F83B  F0 F9    BEQ $F836   ; exit if switch closed cassette switch was open
.F83D  A0 2E    LDY #$2E   ; index to "PRESS RECORD & PLAY ON TAPE"
.F83F  D0 DD    BNE $F81E   ; display message and wait for switch, branch always
```


## Commenti

### Original Disassembly (—)
- **$F838**: return the cassette sense in Zb
- **$F83B**: exit if switch closed cassette switch was open
- **$F83D**: index to "PRESS RECORD & PLAY ON TAPE"
- **$F83F**: display message and wait for switch, branch always

### Commodore-64-intern-Buch (Commodore)
- **$F838**: fragt Bandtaste ab
- **$F83B**: gedrückt, dann fertig
- **$F83D**: Offset für 'PRESS RECORD & PLAY ON TAPE'
- **$F83F**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*