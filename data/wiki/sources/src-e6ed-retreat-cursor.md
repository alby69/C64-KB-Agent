---
id: src-e6ed-retreat-cursor
type: source
title: 'Source Summary: RETREAT CURSOR'
aliases:
- RETREAT CURSOR
- e6ed-retreat-cursor.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e6ed-retreat-cursor.md
  sha256: d579b4b115470aa48ba448d0318f5b2d9a44496c47ad9c42f4c21d420ac20daa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RETREAT CURSOR

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e6ed-retreat-cursor.md`
**SHA256**: `d579b4b115470aa48ba448d0318f5b2d9a44496c47ad9c42f4c21d420ac20daa`

## Summary



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
...
