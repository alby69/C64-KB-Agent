---
id: src-fa70
type: source
title: 'Source Summary: ;*'
aliases:
- ;*
- fa70.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fa70.md
  sha256: 999e47fb1adf174e30a0d31ecaad0b0b47413d9e1536c53119456ce1a81efd1b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;*

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fa70.md`
**SHA256**: `999e47fb1adf174e30a0d31ecaad0b0b47413d9e1536c53119456ce1a81efd1b`

## Summary



# $FA70 — ;*

## Disassemblatura
```assembly
.FA70  A9 0F    LDA #$0F   ; RD15   LDA #$F ;
.FA72  24 AA    BIT $AA   ; BIT    RDFLG           ;TEST FUNCTION MODE
.FA74  10 17    BPL $FA8D   ; BPL    RD20            ;NOT WAITING FOR ZEROS ;
.FA76  A5 B5    LDA $B5   ; LDA    DIFF            ;ZEROS YET?
.FA78  D0 0C    BNE $FA86   ; BNE    RD12            ;YES...WAIT FOR SYNC
.FA7A  A6 BE    LDX $BE   ; LDX    FSBLK           ;IS PASS OVER?
.FA7C  CA       DEX   ; DEX                    ;...IF F...
