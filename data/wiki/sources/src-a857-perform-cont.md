---
id: src-a857-perform-cont
type: source
title: 'Source Summary: perform CONT'
aliases:
- perform CONT
- a857-perform-cont.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a857-perform-cont.md
  sha256: 1b23438e55529729b14c315d744366be614753ae1b0346ddaa0b9f0ec5a5e7a4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform CONT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a857-perform-cont.md`
**SHA256**: `1b23438e55529729b14c315d744366be614753ae1b0346ddaa0b9f0ec5a5e7a4`

## Summary



# $A857 — perform CONT

## Disassemblatura
```assembly
.A857  D0 17    BNE $A870   ; exit if following byte to allow syntax error
.A859  A2 1A    LDX #$1A   ; error code $1A, can't continue error
.A85B  A4 3E    LDY $3E   ; get continue pointer high byte
.A85D  D0 03    BNE $A862   ; go do continue if we can
.A85F  4C 37 A4 JMP $A437   ; else do error #X then warm start we can continue so ...
.A862  A5 3D    LDA $3D   ; get continue pointer low byte
.A864  85 7A    STA $7A   ; save BASIC execu...
