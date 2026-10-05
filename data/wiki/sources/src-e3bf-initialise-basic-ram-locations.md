---
id: src-e3bf-initialise-basic-ram-locations
type: source
title: 'Source Summary: initialise BASIC RAM locations'
aliases:
- initialise BASIC RAM locations
- e3bf-initialise-basic-ram-locations.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e3bf-initialise-basic-ram-locations.md
  sha256: 8fde88b250badc4bfd3747aa4cf07f0073bddd689d69556f68c2f0beb9f9c828
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise BASIC RAM locations

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e3bf-initialise-basic-ram-locations.md`
**SHA256**: `8fde88b250badc4bfd3747aa4cf07f0073bddd689d69556f68c2f0beb9f9c828`

## Summary



# $E3BF — initialise BASIC RAM locations

## Disassemblatura
```assembly
.E3BF  A9 4C    LDA #$4C   ; opcode for JMP
.E3C1  85 54    STA $54   ; save for functions vector jump
.E3C3  8D 10 03 STA $0310   ; save for USR() vector jump set USR() vector to illegal quantity error
.E3C6  A9 48    LDA #$48   ; set USR() vector low byte
.E3C8  A0 B2    LDY #$B2   ; set USR() vector high byte
.E3CA  8D 11 03 STA $0311   ; save USR() vector low byte
.E3CD  8C 12 03 STY $0312   ; save USR() vector high b...
