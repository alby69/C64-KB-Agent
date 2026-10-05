---
id: src-f642-close-serial-bus-device
type: source
title: 'Source Summary: close serial bus device'
aliases:
- close serial bus device
- f642-close-serial-bus-device.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f642-close-serial-bus-device.md
  sha256: d8f43df79450af6a24d1df6f6d910d6c31e53c9ec10c05710465d5ad7524371a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: close serial bus device

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f642-close-serial-bus-device.md`
**SHA256**: `d8f43df79450af6a24d1df6f6d910d6c31e53c9ec10c05710465d5ad7524371a`

## Summary



# $F642 — close serial bus device

## Disassemblatura
```assembly
.F642  24 B9    BIT $B9
.F644  30 11    BMI $F657
.F646  A5 BA    LDA $BA
.F648  20 0C ED JSR $ED0C
.F64B  A5 B9    LDA $B9
.F64D  29 EF    AND #$EF
.F64F  09 E0    ORA #$E0
.F651  20 B9 ED JSR $EDB9
.F654  20 FE ED JSR $EDFE
.F657  18       CLC
.F658  60       RTS
.F659  4A       LSR
.F65A  B0 03    BCS $F65F
.F65C  4C 13 F7 JMP $F713
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F642**: Sekundäradresse teste...
