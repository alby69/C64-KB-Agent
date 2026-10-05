---
id: src-ed21-defer-a-command
type: source
title: 'Source Summary: defer a command'
aliases:
- defer a command
- ed21-defer-a-command.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed21-defer-a-command.md
  sha256: 1766a0f76890aa90297d69a18794bcbc205108c120201ba78f1cab982c3a2952
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: defer a command

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ed21-defer-a-command.md`
**SHA256**: `1766a0f76890aa90297d69a18794bcbc205108c120201ba78f1cab982c3a2952`

## Summary



# $ED21 — defer a command

## Disassemblatura
```assembly
.ED21  85 95    STA $95   ; save as serial deferred character
.ED23  78       SEI   ; disable the interrupts
.ED24  20 97 EE JSR $EE97   ; set the serial data out high
.ED27  C9 3F    CMP #$3F   ; compare read byte with $3F
.ED29  D0 03    BNE $ED2E   ; branch if not $3F, this branch will always be taken as after VIA 2's PCR is read it is ANDed with $DF, so the result can never be $3F ??
.ED2B  20 85 EE JSR $EE85   ; set the serial cloc...
