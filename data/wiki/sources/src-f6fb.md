---
id: src-f6fb
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f6fb.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f6fb.md
  sha256: 04312595e1865469d45c565aa0b728539a8f13489fcca3d6daa04321344f0af5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f6fb.md`
**SHA256**: `04312595e1865469d45c565aa0b728539a8f13489fcca3d6daa04321344f0af5`

## Summary



# $F6FB — ;

## Disassemblatura
```assembly
.F6FB  A9 01    LDA #$01   ; ERROR1 LDA #1          ;TOO MANY FILES
.F6FD  2C       .BYTE $2C   ; .BYT   $2C
.F6FE  A9 02    LDA #$02   ; ERROR2 LDA #2          ;FILE OPEN
.F700  2C       .BYTE $2C   ; .BYT   $2C
.F701  A9 03    LDA #$03   ; ERROR3 LDA #3          ;FILE NOT OPEN
.F703  2C       .BYTE $2C   ; .BYT   $2C
.F704  A9 04    LDA #$04   ; ERROR4 LDA #4          ;FILE NOT FOUND
.F706  2C       .BYTE $2C   ; .BYT   $2C
.F707  A9 05    LDA #$05...
