---
id: src-aad7-print-crlf
type: source
title: 'Source Summary: print CR/LF'
aliases:
- print CR/LF
- aad7-print-crlf.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aad7-print-crlf.md
  sha256: 2d1636703f44639978636c9ddc1073f2c3b52afc4c8ae9178f4fc7321ddd8e6d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print CR/LF

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aad7-print-crlf.md`
**SHA256**: `2d1636703f44639978636c9ddc1073f2c3b52afc4c8ae9178f4fc7321ddd8e6d`

## Summary



# $AAD7 — print CR/LF

## Disassemblatura
```assembly
.AAD7  A9 0D    LDA #$0D   ; set [CR]
.AAD9  20 47 AB JSR $AB47   ; print the character
.AADC  24 13    BIT $13   ; test current I/O channel
.AADE  10 05    BPL $AAE5   ; if ?? toggle A, EOR #$FF and return
.AAE0  A9 0A    LDA #$0A   ; set [LF]
.AAE2  20 47 AB JSR $AB47   ; print the character toggle A
.AAE5  49 FF    EOR #$FF   ; invert A
.AAE7  60       RTS   ; was ","
.AAE8  38       SEC   ; set Cb for read cursor position
.AAE9  20 F0 F...
