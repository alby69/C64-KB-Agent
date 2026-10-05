---
id: src-f5fa-save-to-serial-bus
type: source
title: 'Source Summary: SAVE TO SERIAL BUS'
aliases:
- SAVE TO SERIAL BUS
- f5fa-save-to-serial-bus.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5fa-save-to-serial-bus.md
  sha256: 06111619747b49beaa146877544acdaac41bf3afc867a05bee93c4373d832041
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SAVE TO SERIAL BUS

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f5fa-save-to-serial-bus.md`
**SHA256**: `06111619747b49beaa146877544acdaac41bf3afc867a05bee93c4373d832041`

## Summary



# $F5FA — SAVE TO SERIAL BUS

## Disassemblatura
```assembly
.F5FA  A9 61    LDA #$61
.F5FC  85 B9    STA $B9   ; set SA, secondary address, to #1
.F5FE  A4 B7    LDY $B7   ; FNLEN, length of current filename
.F600  D0 03    BNE $F605   ; ok
.F602  4C 10 F7 JMP $F710   ; I/O error #8, missing filename
.F605  20 D5 F3 JSR $F3D5   ; send SA & filename
.F608  20 8F F6 JSR $F68F   ; print 'SAVING' and filename
.F60B  A5 BA    LDA $BA   ; FA, current device number
.F60D  20 0C ED JSR $ED0C   ; send...
