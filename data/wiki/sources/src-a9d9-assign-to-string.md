---
id: src-a9d9-assign-to-string
type: source
title: 'Source Summary: assign to string'
aliases:
- assign to string
- a9d9-assign-to-string.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a9d9-assign-to-string.md
  sha256: a8125741d3834e67b192b1d7811cfacbdec4db29643da09947c2409c1dc521be
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: assign to string

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a9d9-assign-to-string.md`
**SHA256**: `a8125741d3834e67b192b1d7811cfacbdec4db29643da09947c2409c1dc521be`

## Summary



# $A9D9 — assign to string

## Disassemblatura
```assembly
.A9D9  68       PLA
.A9DA  A4 4A    LDY $4A
.A9DC  C0 BF    CPY #$BF
.A9DE  D0 4C    BNE $AA2C
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A9D9**: Akku vom Stapel holen
- **$A9DA**: Variablenadresse (HIGH) holen
- **$A9DC**: ist Variable TI$?
- **$A9DE**: nein: $AA2C
- **$A9E0**: FRESTR
- **$A9E3**: Stringlänge gleich 6
- **$A9E5**: nein: 'illegal quantity'
- **$A9E7**: Wert holen
- **$A9E9**: und damit FAC
- **$A9...
