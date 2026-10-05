---
id: src-b3a6-check-for-non-direct-mode
type: source
title: 'Source Summary: check for non-direct mode'
aliases:
- check for non-direct mode
- b3a6-check-for-non-direct-mode.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3a6-check-for-non-direct-mode.md
  sha256: 557e9572778ea8f5ef85f9ff5c42c2caaaaaea209a5ae5404a6f7960b2f39a6c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check for non-direct mode

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b3a6-check-for-non-direct-mode.md`
**SHA256**: `557e9572778ea8f5ef85f9ff5c42c2caaaaaea209a5ae5404a6f7960b2f39a6c`

## Summary



# $B3A6 — check for non-direct mode

## Disassemblatura
```assembly
.B3A6  A6 3A    LDX $3A
.B3A8  E8       INX
.B3A9  D0 A0    BNE $B34B
.B3AB  A2 15    LDX #$15   ; error number
.B3AD  2C       .BYTE $2C
.B3AE  A2 1B    LDX #$1B   ; error number
.B3B0  4C 37 A4 JMP $A437
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B3A6**: Flag laden (Direktm. = $FF)
- **$B3A8**: testen
- **$B3A9**: nein: dann RTS
- **$B3AB**: Nummer für 'illegal direct'
- **$B3AE**: Nummer für 'undef'd f...
