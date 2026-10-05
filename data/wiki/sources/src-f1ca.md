---
id: src-f1ca
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f1ca.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1ca.md
  sha256: 2f5fef3487d1640271a343d7e031f10a99920ea118f157a856b4ad3973a370d2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f1ca.md`
**SHA256**: `2f5fef3487d1640271a343d7e031f10a99920ea118f157a856b4ad3973a370d2`

## Summary



# $F1CA — ;

## Disassemblatura
```assembly
.F1CA  48       PHA   ; NBSOUT PHA             ;PRESERVE .A
.F1CB  A5 9A    LDA $9A   ; LDA    DFLTO           ;CHECK DEVICE
.F1CD  C9 03    CMP #$03   ; CMP    #3              ;IS IT THE SCREEN?
.F1CF  D0 04    BNE $F1D5   ; BNE    BO10            ;NO... ; ;PRINT TO CRT ;
.F1D1  68       PLA   ; PLA                    ;RESTORE DATA
.F1D2  4C 16 E7 JMP $E716   ; JMP    PRT             ;PRINT ON CRT ; BO10
.F1D5  90 04    BCC $F1DB   ; BCC    BO20    ...
