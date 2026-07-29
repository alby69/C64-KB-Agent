---
title: RETREAT CURSOR
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00d3-pntr
- 00d6-tblx
- 00d9-ldtb1
- cursor
- e6ed-retreat-cursor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  address: $E6ED
  address_end: $E700
  symbol: retreat-cursor
  sources:
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E6ED**: LDTB1, screen line link table'
---

# $E6ED — RETREAT CURSOR

## Disassemblatura
```assembly
.E6ED  B5 D9    LDA $D9,X   ; LDTB1, screen line link table
.E6EF  30 03    BMI $E6F4   ; test bit7
.E6F1  CA       DEX   ; next line
.E6F2  D0 F9    BNE $E6ED   ; till all are done
.E6F4  4C F0 E9 JMP $E9F0   ; set start of line
.E6F7  C6 D6    DEC $D6   ; decrement TBLX, cursor line
.E6F9  20 7C E8 JSR $E87C   ; goto next line
.E6FC  A9 00    LDA #$00
.E6FE  85 D3    STA $D3   ; set PNTR, the cursor column, to zero
.E700  60       RTS
```


## Commenti

### Magnus Nyman (Magnus Nyman)
- **$E6ED**: LDTB1, screen line link table
- **$E6EF**: test bit7
- **$E6F1**: next line
- **$E6F2**: till all are done
- **$E6F4**: set start of line
- **$E6F7**: decrement TBLX, cursor line
- **$E6F9**: goto next line
- **$E6FE**: set PNTR, the cursor column, to zero

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*