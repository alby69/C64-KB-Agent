---
id: src-e168-perform-load
type: source
title: 'Source Summary: perform LOAD'
aliases:
- perform LOAD
- e168-perform-load.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e168-perform-load.md
  sha256: b6fef79e8914d206f18c900c94bd27dd6e27837fa6817afa1c5b19ecfa392a80
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform LOAD

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e168-perform-load.md`
**SHA256**: `b6fef79e8914d206f18c900c94bd27dd6e27837fa6817afa1c5b19ecfa392a80`

## Summary



# $E168 — perform LOAD

## Disassemblatura
```assembly
.E168  A9 00    LDA #$00   ; flag load
.E16A  85 0A    STA $0A   ; set load/verify flag
.E16C  20 D4 E1 JSR $E1D4   ; get parameters for LOAD/SAVE
.E16F  A5 0A    LDA $0A   ; get load/verify flag
.E171  A6 2B    LDX $2B   ; get start of memory low byte
.E173  A4 2C    LDY $2C   ; get start of memory high byte
.E175  20 D5 FF JSR $FFD5   ; load RAM from a device
.E178  B0 57    BCS $E1D1   ; if error go handle BASIC I/O error
.E17A  A5 0A  ...
