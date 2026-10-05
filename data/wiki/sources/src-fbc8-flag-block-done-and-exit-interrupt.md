---
id: src-fbc8-flag-block-done-and-exit-interrupt
type: source
title: 'Source Summary: flag block done and exit interrupt'
aliases:
- flag block done and exit interrupt
- fbc8-flag-block-done-and-exit-interrupt.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fbc8-flag-block-done-and-exit-interrupt.md
  sha256: f0734f25bf8e0de731c6058123458a28102ab085c4fb6ea61c62122cb31ab499
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: flag block done and exit interrupt

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fbc8-flag-block-done-and-exit-interrupt.md`
**SHA256**: `f0734f25bf8e0de731c6058123458a28102ab085c4fb6ea61c62122cb31ab499`

## Summary



# $FBC8 — flag block done and exit interrupt

## Disassemblatura
```assembly
.FBC8  38       SEC   ; set carry flag
.FBC9  66 B6    ROR $B6   ; set buffer address high byte negative, flag all sync, data and checksum bytes written
.FBCB  30 3C    BMI $FC09   ; restore registers and exit interrupt, branch always
```


## Commenti

### Original Disassembly (—)
- **$FBC8**: set carry flag
- **$FBC9**: set buffer address high byte negative, flag all sync, data and checksum bytes written
- **$FBCB**...
