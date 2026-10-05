---
id: src-aef1-evaluate-expression
type: source
title: 'Source Summary: EVALUATE "(EXPRESSION)"'
aliases:
- EVALUATE "(EXPRESSION)"
- aef1-evaluate-expression.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aef1-evaluate-expression.md
  sha256: eb6af03ad38d05d57c771f420e2c5d6f7d17ad8290e9cce51828d0cccf0283a8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: EVALUATE "(EXPRESSION)"

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aef1-evaluate-expression.md`
**SHA256**: `eb6af03ad38d05d57c771f420e2c5d6f7d17ad8290e9cce51828d0cccf0283a8`

## Summary



# $AEF1 — EVALUATE "(EXPRESSION)"

## Disassemblatura
```assembly
.AEF1  20 FA AE JSR $AEFA   ; IS THERE A '(' AT TXTPTR?
.AEF4  20 9E AD JSR $AD9E   ; YES, EVALUATE EXPRESSION
.AEF7  A9 29    LDA #$29   ; CHECK FOR ')'
.AEF9  2C       .BYTE $2C   ; TRICK
.AEFA  A9 28    LDA #$28
.AEFC  2C       .BYTE $2C   ; TRICK
.AEFD  A9 2C    LDA #$2C   ; COMMA AT TXTPTR?
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AEF1**: prüft auf Klammer auf
- **$AEF4**: FRMEVL holt Term

### Bob S...
