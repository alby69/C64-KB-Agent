---
id: src-f1b8-read-a-byte-from-rs-232-bus
type: source
title: 'Source Summary: read a byte from RS-232 bus'
aliases:
- read a byte from RS-232 bus
- f1b8-read-a-byte-from-rs-232-bus.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1b8-read-a-byte-from-rs-232-bus.md
  sha256: 8d3f6605972c8af6734e06d490560e733cb478163c832f79a38df5553de4451f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: read a byte from RS-232 bus

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f1b8-read-a-byte-from-rs-232-bus.md`
**SHA256**: `8d3f6605972c8af6734e06d490560e733cb478163c832f79a38df5553de4451f`

## Summary



# $F1B8 — read a byte from RS-232 bus

## Disassemblatura
```assembly
.F1B8  20 4E F1 JSR $F14E
.F1BB  B0 F7    BCS $F1B4
.F1BD  C9 00    CMP #$00
.F1BF  D0 F2    BNE $F1B3
.F1C1  AD 97 02 LDA $0297
.F1C4  29 60    AND #$60
.F1C6  D0 E9    BNE $F1B1
.F1C8  F0 EE    BEQ $F1B8
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F1B8**: ein Byte von RS 232 holen
- **$F1BB**: verzweige wenn Fehler
- **$F1BD**: vergleiche mit Nullbyte
- **$F1BF**: nein, dann ok
- **$F1C1**: Status lade...
