---
id: src-a81d-perform-restore
type: source
title: 'Source Summary: perform RESTORE'
aliases:
- perform RESTORE
- a81d-perform-restore.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a81d-perform-restore.md
  sha256: f4fb1cf6940906d31e32ea61a7085a392d0ea21c281d577f3fe632f57694302e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform RESTORE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a81d-perform-restore.md`
**SHA256**: `f4fb1cf6940906d31e32ea61a7085a392d0ea21c281d577f3fe632f57694302e`

## Summary



# $A81D — perform RESTORE

## Disassemblatura
```assembly
.A81D  38       SEC   ; set carry for subtract
.A81E  A5 2B    LDA $2B   ; get start of memory low byte
.A820  E9 01    SBC #$01   ; -1
.A822  A4 2C    LDY $2C   ; get start of memory high byte
.A824  B0 01    BCS $A827   ; branch if no rollunder
.A826  88       DEY   ; else decrement high byte
.A827  85 41    STA $41   ; set DATA pointer low byte
.A829  84 42    STY $42   ; set DATA pointer high byte
.A82B  60       RTS
```


## Commen...
