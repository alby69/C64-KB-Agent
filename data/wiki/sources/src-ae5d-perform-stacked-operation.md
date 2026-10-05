---
id: src-ae5d-perform-stacked-operation
type: source
title: 'Source Summary: PERFORM STACKED OPERATION'
aliases:
- PERFORM STACKED OPERATION
- ae5d-perform-stacked-operation.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae5d-perform-stacked-operation.md
  sha256: ca7d2c0305ccaa577dc92082d715ba1ab5fb5c749e79b94879f640607ab506bf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PERFORM STACKED OPERATION

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ae5d-perform-stacked-operation.md`
**SHA256**: `ca7d2c0305ccaa577dc92082d715ba1ab5fb5c749e79b94879f640607ab506bf`

## Summary



# $AE5D — PERFORM STACKED OPERATION

## Disassemblatura
```assembly
.AE5D  C9 64    CMP #$64   ; WAS IT RELATIONAL OPERATOR?
.AE5F  F0 03    BEQ $AE64   ; YES, ALLOW STRING COMPARE
.AE61  20 8D AD JSR $AD8D   ; MUST BE NUMERIC VALUE
.AE64  84 4B    STY $4B
.AE66  68       PLA   ; GET 0000<=>C FROM STACK
.AE67  4A       LSR   ; SHIFT TO 00000<=> FORM
.AE68  85 12    STA $12   ; 00000<=>
.AE6A  68       PLA
.AE6B  85 69    STA $69   ; GET FLOATING POINT VALUE OFF STACK,
.AE6D  68       PLA   ; A...
