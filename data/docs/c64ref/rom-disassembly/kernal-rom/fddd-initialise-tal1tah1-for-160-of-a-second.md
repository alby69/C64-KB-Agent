---
title: initialise TAL1/TAH1 for 1/60 of a second
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
  - magnus_nyman.txt
  address: $FDDD
  address_end: $FDF6
  symbol: initialise-tal1tah1-for-160-of-a-second
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FDDD**: PAL/NTSC flag'
---

# $FDDD — initialise TAL1/TAH1 for 1/60 of a second

## Disassemblatura
```assembly
.FDDD  AD A6 02 LDA $02A6
.FDE0  F0 0A    BEQ $FDEC
.FDE2  A9 25    LDA #$25
.FDE4  8D 04 DC STA $DC04
.FDE7  A9 40    LDA #$40
.FDE9  4C F3 FD JMP $FDF3
.FDEC  A9 95    LDA #$95
.FDEE  8D 04 DC STA $DC04
.FDF1  A9 42    LDA #$42
.FDF3  8D 05 DC STA $DC05
.FDF6  4C 6E FF JMP $FF6E
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FDDD**: PAL/NTSC flag
- **$FDE0**: NTSC setup
- **$FDE4**: CIA#1 timer A - lowbyte
- **$FDE7**: PAL-setup #4025
- **$FDEE**: CIA#1 timer A - lowbyte
- **$FDF1**: NTSC-setup #4295
- **$FDF3**: CIA#1 timer A - highbyte
- **$FDF6**: start timer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*