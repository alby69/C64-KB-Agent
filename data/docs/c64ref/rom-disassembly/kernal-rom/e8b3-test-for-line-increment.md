---
title: test for line increment
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
- e8b3-check-line-increment
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $E8B3
  address_end: $E8CA
  symbol: test-for-line-increment
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E8B3**: set the count'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E8B3**: start by testing position $27 (39)'
---

# $E8B3 — test for line increment

## Disassemblatura
```assembly
.E8B3  A2 02    LDX #$02   ; set the count
.E8B5  A9 27    LDA #$27   ; set the column
.E8B7  C5 D3    CMP $D3   ; compare the column with the cursor column
.E8B9  F0 07    BEQ $E8C2   ; if at end of line test and possibly increment cursor row
.E8BB  18       CLC   ; else clear carry for add
.E8BC  69 28    ADC #$28   ; increment to the next line
.E8BE  CA       DEX   ; decrement the loop count
.E8BF  D0 F6    BNE $E8B7   ; loop if more to test
.E8C1  60       RTS   ; cursor is at end of line
.E8C2  A6 D6    LDX $D6   ; get the cursor row
.E8C4  E0 19    CPX #$19   ; compare it with the end of the screen
.E8C6  F0 02    BEQ $E8CA   ; if at the end of screen just exit
.E8C8  E6 D6    INC $D6   ; else increment the cursor row
.E8CA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E8B3**: set the count
- **$E8B5**: set the column
- **$E8B7**: compare the column with the cursor column
- **$E8B9**: if at end of line test and possibly increment cursor row
- **$E8BB**: else clear carry for add
- **$E8BC**: increment to the next line
- **$E8BE**: decrement the loop count
- **$E8BF**: loop if more to test
- **$E8C1**: cursor is at end of line
- **$E8C2**: get the cursor row
- **$E8C4**: compare it with the end of the screen
- **$E8C6**: if at the end of screen just exit
- **$E8C8**: else increment the cursor row

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E8B3**: start by testing position $27 (39)
- **$E8B5**: compare with PNTR
- **$E8B7**: brach if equal, and move cursor down
- **$E8B9**: else, add $28 to test next physical line
- **$E8BC**: two lines to test
- **$E8BF**: return here without moving cursor down
- **$E8C1**: get TBLX
- **$E8C2**: and test if at the 25th line
- **$E8C4**: yepp, return without moving down
- **$E8C6**: increment TBLX

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*