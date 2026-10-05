---
id: fddd-initialise-tal1tah1-for-160-of-a-second
type: entity
title: initialise TAL1/TAH1 for 1/60 of a second
aliases:
- initialise TAL1/TAH1 for 1/60 of a second
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fddd-initialise-tal1tah1-for-160-of-a-second.md
  sha256: 1ff89f6db54c573579de9f2a0572dd4abe08eab9b3235bb410f6965eabe82a4a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fddd-initialise-tal1tah1-for-160-of-a-second
---

# initialise TAL1/TAH1 for 1/60 of a second



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

## References
- Source: [[src-fddd-initialise-tal1tah1-for-160-of-a-second]]
