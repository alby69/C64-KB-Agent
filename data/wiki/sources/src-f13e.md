---
id: src-f13e
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f13e.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f13e.md
  sha256: d0e51f89879c450e27a5ab56e5f42ab9c77ceaec8b231e737da30d4b2e29476e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f13e.md`
**SHA256**: `d0e51f89879c450e27a5ab56e5f42ab9c77ceaec8b231e737da30d4b2e29476e`

## Summary



# $F13E — ;

## Disassemblatura
```assembly
.F13E  A5 99    LDA $99   ; NGETIN LDA DFLTN       ;CHECK DEVICE
.F140  D0 08    BNE $F14A   ; BNE    GN10            ;NOT KEYBOARD ;
.F142  A5 C6    LDA $C6   ; LDA    NDX             ;QUEUE INDEX
.F144  F0 0F    BEQ $F155   ; BEQ    GN20            ;NOBODY THERE...EXIT ;
.F146  78       SEI   ; SEI
.F147  4C B4 E5 JMP $E5B4   ; JMP    LP2             ;GO REMOVE A CHARACTER ;
.F14A  C9 02    CMP #$02   ; GN10   CMP #2          ;IS IT RS-232
.F14C  D...
