---
id: src-bbd4-pack-fac1-into-xy
type: source
title: 'Source Summary: pack FAC1 into (XY)'
aliases:
- pack FAC1 into (XY)
- bbd4-pack-fac1-into-xy.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbd4-pack-fac1-into-xy.md
  sha256: 9e8a6769252aa5a5b139934276b229da6980b69d4ea8d0583cafea91ec15320c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: pack FAC1 into (XY)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bbd4-pack-fac1-into-xy.md`
**SHA256**: `9e8a6769252aa5a5b139934276b229da6980b69d4ea8d0583cafea91ec15320c`

## Summary



# $BBD4 — pack FAC1 into (XY)

## Disassemblatura
```assembly
.BBD4  20 1B BC JSR $BC1B   ; round FAC1
.BBD7  86 22    STX $22   ; save pointer low byte
.BBD9  84 23    STY $23   ; save pointer high byte
.BBDB  A0 04    LDY #$04   ; set index
.BBDD  A5 65    LDA $65   ; get FAC1 mantissa 4
.BBDF  91 22    STA ($22),Y   ; store in destination
.BBE1  88       DEY   ; decrement index
.BBE2  A5 64    LDA $64   ; get FAC1 mantissa 3
.BBE4  91 22    STA ($22),Y   ; store in destination
.BBE6  88    ...
