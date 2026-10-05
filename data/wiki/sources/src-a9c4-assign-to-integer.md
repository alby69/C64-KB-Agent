---
id: src-a9c4-assign-to-integer
type: source
title: 'Source Summary: assign to integer'
aliases:
- assign to integer
- a9c4-assign-to-integer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a9c4-assign-to-integer.md
  sha256: 6722e22b49265a7026c40feeccfb52e0fef65f0998d6ed0e109bcab3d9b73986
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: assign to integer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a9c4-assign-to-integer.md`
**SHA256**: `6722e22b49265a7026c40feeccfb52e0fef65f0998d6ed0e109bcab3d9b73986`

## Summary



# $A9C4 — assign to integer

## Disassemblatura
```assembly
.A9C4  20 1B BC JSR $BC1B
.A9C7  20 BF B1 JSR $B1BF
.A9CA  A0 00    LDY #$00
.A9CC  A5 64    LDA $64
.A9CE  91 49    STA ($49),Y
.A9D0  C8       INY
.A9D1  A5 65    LDA $65
.A9D3  91 49    STA ($49),Y
.A9D5  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A9C4**: FAC runden
- **$A9C7**: und nach INTEGER wandlen
- **$A9CA**: Zeiger setzen
- **$A9CC**: HIGH-Byte holen und
- **$A9CE**: Wert in Variable bring...
