---
id: src-f7d7-set-the-tape-buffer-start-and-end-pointers
type: source
title: 'Source Summary: set the tape buffer start and end pointers'
aliases:
- set the tape buffer start and end pointers
- f7d7-set-the-tape-buffer-start-and-end-pointers.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f7d7-set-the-tape-buffer-start-and-end-pointers.md
  sha256: 24af910372527aff9f686612bd95a7f9a3ab5573ea35dbec7d49a97b992091b5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the tape buffer start and end pointers

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f7d7-set-the-tape-buffer-start-and-end-pointers.md`
**SHA256**: `24af910372527aff9f686612bd95a7f9a3ab5573ea35dbec7d49a97b992091b5`

## Summary



# $F7D7 — set the tape buffer start and end pointers

## Disassemblatura
```assembly
.F7D7  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F7DA  8A       TXA   ; copy tape buffer start pointer low byte
.F7DB  85 C1    STA $C1   ; save as I/O address pointer low byte
.F7DD  18       CLC   ; clear carry for add
.F7DE  69 C0    ADC #$C0   ; add buffer length low byte
.F7E0  85 AE    STA $AE   ; save tape buffer end pointer low byte
.F7E2  98       TYA   ; copy tape buffer start point...
