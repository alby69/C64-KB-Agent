---
id: src-e9f0-fetch-a-screen-address
type: source
title: 'Source Summary: fetch a screen address'
aliases:
- fetch a screen address
- e9f0-fetch-a-screen-address.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e9f0-fetch-a-screen-address.md
  sha256: 238ee06ac44de0d9e610f0a24e40bf417432af849762317a9b8017d29fff7a7f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: fetch a screen address

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e9f0-fetch-a-screen-address.md`
**SHA256**: `238ee06ac44de0d9e610f0a24e40bf417432af849762317a9b8017d29fff7a7f`

## Summary



# $E9F0 — fetch a screen address

## Disassemblatura
```assembly
.E9F0  BD F0 EC LDA $ECF0,X   ; get the start of line low byte from the ROM table
.E9F3  85 D1    STA $D1   ; set the current screen line pointer low byte
.E9F5  B5 D9    LDA $D9,X   ; get the start of line high byte from the RAM table
.E9F7  29 03    AND #$03   ; mask 0000 00xx, line memory page
.E9F9  0D 88 02 ORA $0288   ; OR with the screen memory page
.E9FC  85 D2    STA $D2   ; save the current screen line pointer high byte...
