---
id: src-fe00-set-logical-first-and-second-addresses
type: source
title: 'Source Summary: set logical, first and second addresses'
aliases:
- set logical, first and second addresses
- fe00-set-logical-first-and-second-addresses.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe00-set-logical-first-and-second-addresses.md
  sha256: 485df2f4d77f964b791cd7801940baa45417fe743ac5ac0706d0a49d62cd5ca6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set logical, first and second addresses

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe00-set-logical-first-and-second-addresses.md`
**SHA256**: `485df2f4d77f964b791cd7801940baa45417fe743ac5ac0706d0a49d62cd5ca6`

## Summary



# $FE00 — set logical, first and second addresses

## Disassemblatura
```assembly
.FE00  85 B8    STA $B8   ; save the logical file
.FE02  86 BA    STX $BA   ; save the device number
.FE04  84 B9    STY $B9   ; save the secondary address
.FE06  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE00**: save the logical file
- **$FE02**: save the device number
- **$FE04**: save the secondary address

### Commodore-64-intern-Buch (Commodore)
- **$FE00**: logische Filenummer
- **$F...
