---
id: src-ea24-calculate-the-pointer-to-colour-ram
type: source
title: 'Source Summary: calculate the pointer to colour RAM'
aliases:
- calculate the pointer to colour RAM
- ea24-calculate-the-pointer-to-colour-ram.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ea24-calculate-the-pointer-to-colour-ram.md
  sha256: 9503b4dd9156d526e4138893173222f292573ad5ad59eef305fe9a67ac2d6ca1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: calculate the pointer to colour RAM

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ea24-calculate-the-pointer-to-colour-ram.md`
**SHA256**: `9503b4dd9156d526e4138893173222f292573ad5ad59eef305fe9a67ac2d6ca1`

## Summary



# $EA24 — calculate the pointer to colour RAM

## Disassemblatura
```assembly
.EA24  A5 D1    LDA $D1   ; get current screen line pointer low byte
.EA26  85 F3    STA $F3   ; save pointer to colour RAM low byte
.EA28  A5 D2    LDA $D2   ; get current screen line pointer high byte
.EA2A  29 03    AND #$03   ; mask 0000 00xx, line memory page
.EA2C  09 D8    ORA #$D8   ; set  1101 01xx, colour memory page
.EA2E  85 F4    STA $F4   ; save pointer to colour RAM high byte
.EA30  60       RTS
```


...
