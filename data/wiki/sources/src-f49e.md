---
id: src-f49e
type: source
title: 'Source Summary: ;*'
aliases:
- ;*
- f49e.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f49e.md
  sha256: 2476ea9d9f067cfcf616181408b425afb6de5508c7ac3a841a135a29e9d7fb90
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;*

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f49e.md`
**SHA256**: `2476ea9d9f067cfcf616181408b425afb6de5508c7ac3a841a135a29e9d7fb90`

## Summary



# $F49E — ;*

## Disassemblatura
```assembly
.F49E  86 C3    STX $C3   ; LOADSP STX MEMUSS      ;.X HAS LOW ALT START
.F4A0  84 C4    STY $C4   ; STY    MEMUSS+1
.F4A2  6C 30 03 JMP ($0330)   ; LOAD   JMP (ILOAD)     ;MONITOR LOAD ENTRY ;
.F4A5  85 93    STA $93   ; NLOAD  STA VERCK       ;STORE VERIFY FLAG
.F4A7  A9 00    LDA #$00   ; LDA    #0
.F4A9  85 90    STA $90   ; STA    STATUS ;
.F4AB  A5 BA    LDA $BA   ; LDA    FA              ;CHECK DEVICE NUMBER
.F4AD  D0 03    BNE $F4B2   ; BNE ...
