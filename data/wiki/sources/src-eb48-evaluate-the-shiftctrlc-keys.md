---
id: src-eb48-evaluate-the-shiftctrlc-keys
type: source
title: 'Source Summary: evaluate the SHIFT/CTRL/C= keys'
aliases:
- evaluate the SHIFT/CTRL/C= keys
- eb48-evaluate-the-shiftctrlc-keys.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eb48-evaluate-the-shiftctrlc-keys.md
  sha256: 388046f56fe85acc9a31c4e4836e170e03505f3d47ac5716f414aa894df7b8e5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: evaluate the SHIFT/CTRL/C= keys

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eb48-evaluate-the-shiftctrlc-keys.md`
**SHA256**: `388046f56fe85acc9a31c4e4836e170e03505f3d47ac5716f414aa894df7b8e5`

## Summary



# $EB48 — evaluate the SHIFT/CTRL/C= keys

## Disassemblatura
```assembly
.EB48  AD 8D 02 LDA $028D   ; get the keyboard shift/control/c= flag
.EB4B  C9 03    CMP #$03   ; compare with [SHIFT][C=]
.EB4D  D0 15    BNE $EB64   ; if not [SHIFT][C=] go ??
.EB4F  CD 8E 02 CMP $028E   ; compare with last
.EB52  F0 EE    BEQ $EB42   ; exit if still the same
.EB54  AD 91 02 LDA $0291   ; get the shift mode switch $00 = enabled, $80 = locked
.EB57  30 1D    BMI $EB76   ; if locked continue keyboard dec...
