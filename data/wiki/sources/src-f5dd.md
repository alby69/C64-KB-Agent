---
id: src-f5dd
type: source
title: 'Source Summary: ;**'
aliases:
- ;**
- f5dd.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5dd.md
  sha256: 3bee7fa25e73727eb5b820683f938b59e1133425e3c54f03ff8ca99bb3a9a68d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;**

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f5dd.md`
**SHA256**: `3bee7fa25e73727eb5b820683f938b59e1133425e3c54f03ff8ca99bb3a9a68d`

## Summary



# $F5DD — ;**

## Disassemblatura
```assembly
.F5DD  86 AE    STX $AE   ; SAVESP STX EAL
.F5DF  84 AF    STY $AF   ; STY    EAH
.F5E1  AA       TAX   ; TAX                    ;SET UP START
.F5E2  B5 00    LDA $00,X   ; LDA    $00,X
.F5E4  85 C1    STA $C1   ; STA    STAL
.F5E6  B5 01    LDA $01,X   ; LDA    $01,X
.F5E8  85 C2    STA $C2   ; STA    STAH ;
.F5EA  6C 32 03 JMP ($0332)   ; SAVE   JMP (ISAVE)
.F5ED  A5 BA    LDA $BA   ; NSAVE  LDA FA  ***MONITOR ENTRY
.F5EF  D0 03    BNE $F5F4   ; ...
