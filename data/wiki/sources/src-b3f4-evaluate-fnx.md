---
id: src-b3f4-evaluate-fnx
type: source
title: 'Source Summary: Evaluate FNx'
aliases:
- Evaluate FNx
- b3f4-evaluate-fnx.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3f4-evaluate-fnx.md
  sha256: 7c266973f0ac371db4429e0c8a90dbd8d41153b0c75806923a9493596f6e1334
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Evaluate FNx

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b3f4-evaluate-fnx.md`
**SHA256**: `7c266973f0ac371db4429e0c8a90dbd8d41153b0c75806923a9493596f6e1334`

## Summary



# $B3F4 — Evaluate FNx

## Disassemblatura
```assembly
.B3F4  20 E1 B3 JSR $B3E1   ; check FNx syntax
.B3F7  A5 4F    LDA $4F   ; get function pointer high byte
.B3F9  48       PHA   ; push it
.B3FA  A5 4E    LDA $4E   ; get function pointer low byte
.B3FC  48       PHA   ; push it
.B3FD  20 F1 AE JSR $AEF1   ; evaluate expression within parentheses
.B400  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B403  68       PLA   ; pop function pointer low byte
.B404  85 4E...
