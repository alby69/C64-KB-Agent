---
id: src-e9e0-calculate-pointers-to-screen-lines-colour-ram
type: source
title: 'Source Summary: calculate pointers to screen lines colour RAM'
aliases:
- calculate pointers to screen lines colour RAM
- e9e0-calculate-pointers-to-screen-lines-colour-ram.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e9e0-calculate-pointers-to-screen-lines-colour-ram.md
  sha256: 767d2f0fb16284eae50dfd88307c3f40a2e4119659bc65e2c33356f068972b52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: calculate pointers to screen lines colour RAM

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e9e0-calculate-pointers-to-screen-lines-colour-ram.md`
**SHA256**: `767d2f0fb16284eae50dfd88307c3f40a2e4119659bc65e2c33356f068972b52`

## Summary



# $E9E0 — calculate pointers to screen lines colour RAM

## Disassemblatura
```assembly
.E9E0  20 24 EA JSR $EA24   ; calculate the pointer to the current screen line colour RAM
.E9E3  A5 AC    LDA $AC   ; get the next screen line pointer low byte
.E9E5  85 AE    STA $AE   ; save the next screen line colour RAM pointer low byte
.E9E7  A5 AD    LDA $AD   ; get the next screen line pointer high byte
.E9E9  29 03    AND #$03   ; mask 0000 00xx, line memory page
.E9EB  09 D8    ORA #$D8   ; set  1...
