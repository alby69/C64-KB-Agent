---
title: wait for PLAY
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
- f817-wartet-auf-bandtaste
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F817
  address_end: $F82B
  symbol: wait-for-play
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F817**: return cassette sense in Zb'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F817**: fragt BandtTaste ab'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F817 — wait for PLAY

## Disassemblatura
```assembly
.F817  20 2E F8 JSR $F82E   ; return cassette sense in Zb
.F81A  F0 1A    BEQ $F836   ; if switch closed just exit cassette switch was open
.F81C  A0 1B    LDY #$1B   ; index to "PRESS PLAY ON TAPE"
.F81E  20 2F F1 JSR $F12F   ; display kernel I/O message
.F821  20 D0 F8 JSR $F8D0   ; scan stop key and flag abort if pressed note if STOP was pressed the return is to the routine that called this one and not here
.F824  20 2E F8 JSR $F82E   ; return cassette sense in Zb
.F827  D0 F8    BNE $F821   ; loop if the cassette switch is open
.F829  A0 6A    LDY #$6A   ; index to "OK"
.F82B  4C 2F F1 JMP $F12F   ; display kernel I/O message and return
```


## Commenti

### Original Disassembly (—)
- **$F817**: return cassette sense in Zb
- **$F81A**: if switch closed just exit cassette switch was open
- **$F81C**: index to "PRESS PLAY ON TAPE"
- **$F81E**: display kernel I/O message
- **$F821**: scan stop key and flag abort if pressed note if STOP was pressed the return is to the routine that called this one and not here
- **$F824**: return cassette sense in Zb
- **$F827**: loop if the cassette switch is open
- **$F829**: index to "OK"
- **$F82B**: display kernel I/O message and return

### Commodore-64-intern-Buch (Commodore)
- **$F817**: fragt BandtTaste ab
- **$F81A**: gedrückt, dann fertig
- **$F81C**: Offset für 'PRESS PLAY ON TAPE'
- **$F81E**: und ausgeben
- **$F821**: testet auf STOP-Taste
- **$F824**: fragt BandtTaste ab
- **$F827**: nicht gedrückt so erneut abfragen
- **$F829**: Offset für 'OK'
- **$F82B**: und ausgeben, Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*