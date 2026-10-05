---
id: src-fe72-rs232-nmi-routine
type: source
title: 'Source Summary: RS232 NMI routine'
aliases:
- RS232 NMI routine
- fe72-rs232-nmi-routine.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe72-rs232-nmi-routine.md
  sha256: 8174bdaeeee288585b87177b6407ae28c1ce45b4323d45c0494511c3e19ddb2d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RS232 NMI routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe72-rs232-nmi-routine.md`
**SHA256**: `8174bdaeeee288585b87177b6407ae28c1ce45b4323d45c0494511c3e19ddb2d`

## Summary



# $FE72 — RS232 NMI routine

## Disassemblatura
```assembly
.FE72  98       TYA
.FE73  2D A1 02 AND $02A1   ; AND with the RS-232 interrupt enable byte
.FE76  AA       TAX
.FE77  29 01    AND #$01
.FE79  F0 28    BEQ $FEA3
.FE7B  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.FE7E  29 FB    AND #$FB   ; mask xxxx x0xx, clear RS232 Tx DATA
.FE80  05 B5    ORA $B5   ; OR in the RS232 transmit data bit
.FE82  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video addr...
