---
id: src-a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here
type: source
title: 'Source Summary: BASIC warm start, the warm start vector is initialised to
  point here'
aliases:
- BASIC warm start, the warm start vector is initialised to point here
- a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here.md
  sha256: 290d04c5f1a11085e9d3cfd6796ee19379b9c9dbb1fe22b7ce55ec76f0f80561
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BASIC warm start, the warm start vector is initialised to point here

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here.md`
**SHA256**: `290d04c5f1a11085e9d3cfd6796ee19379b9c9dbb1fe22b7ce55ec76f0f80561`

## Summary



# $A483 — BASIC warm start, the warm start vector is initialised to point here

## Disassemblatura
```assembly
.A483  20 60 A5 JSR $A560   ; call for BASIC input
.A486  86 7A    STX $7A   ; save BASIC execute pointer low byte
.A488  84 7B    STY $7B   ; save BASIC execute pointer high byte
.A48A  20 73 00 JSR $0073   ; increment and scan memory
.A48D  AA       TAX   ; copy byte to set flags
.A48E  F0 F0    BEQ $A480   ; loop if no input got to interpret the input line now ....
.A490  A2 FF    ...
