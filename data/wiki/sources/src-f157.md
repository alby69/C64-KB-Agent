---
id: src-f157
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f157.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f157.md
  sha256: cb662af369eef94caf23e5eb4d4170e11887baffec7f1632f52543d2b9fc56af
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f157.md`
**SHA256**: `cb662af369eef94caf23e5eb4d4170e11887baffec7f1632f52543d2b9fc56af`

## Summary



# $F157 — ;

## Disassemblatura
```assembly
.F157  A5 99    LDA $99   ; NBASIN LDA DFLTN       ;CHECK DEVICE
.F159  D0 0B    BNE $F166   ; BNE    BN10            ;IS NOT KEYBOARD... ; ;INPUT FROM KEYBOARD ;
.F15B  A5 D3    LDA $D3   ; LDA    PNTR            ;SAVE CURRENT...
.F15D  85 CA    STA $CA   ; STA    LSTP            ;... CURSOR COLUMN
.F15F  A5 D6    LDA $D6   ; LDA    TBLX            ;SAVE CURRENT...
.F161  85 C9    STA $C9   ; STA    LSXP            ;... LINE NUMBER
.F163  4C 32 E6 J...
