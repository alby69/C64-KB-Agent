---
id: src-a96b-get-fixed-point-number-into-temporary-integer
type: source
title: 'Source Summary: get fixed-point number into temporary integer'
aliases:
- get fixed-point number into temporary integer
- a96b-get-fixed-point-number-into-temporary-integer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a96b-get-fixed-point-number-into-temporary-integer.md
  sha256: 251dee47e5dfd5ce76df1b05d0895cc0ade2cf369c8ce51ac9662cf23081651d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get fixed-point number into temporary integer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a96b-get-fixed-point-number-into-temporary-integer.md`
**SHA256**: `251dee47e5dfd5ce76df1b05d0895cc0ade2cf369c8ce51ac9662cf23081651d`

## Summary



# $A96B — get fixed-point number into temporary integer

## Disassemblatura
```assembly
.A96B  A2 00    LDX #$00   ; clear X
.A96D  86 14    STX $14   ; clear temporary integer low byte
.A96F  86 15    STX $15   ; clear temporary integer high byte
.A971  B0 F7    BCS $A96A   ; return if carry set, end of scan, character was not 0-9
.A973  E9 2F    SBC #$2F   ; subtract $30, $2F+carry, from byte
.A975  85 07    STA $07   ; store #
.A977  A5 15    LDA $15   ; get temporary integer high byte
.A97...
