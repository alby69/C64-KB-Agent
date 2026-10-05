---
id: src-eadd-process-key-image
type: source
title: 'Source Summary: PROCESS KEY IMAGE'
aliases:
- PROCESS KEY IMAGE
- eadd-process-key-image.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eadd-process-key-image.md
  sha256: 0a6469147b0ce3c51bcc7c0261328329a0bca92bbbc583d35adcfc1558ba00ae
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PROCESS KEY IMAGE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eadd-process-key-image.md`
**SHA256**: `0a6469147b0ce3c51bcc7c0261328329a0bca92bbbc583d35adcfc1558ba00ae`

## Summary



# $EADD — PROCESS KEY IMAGE

## Disassemblatura
```assembly
.EADD  6C 8F 02 JMP ($028F)   ; jump through KEYLOG vector, points to $eae0
.EAE0  A4 CB    LDY $CB   ; SFDX, number of the key we pressed
.EAE2  B1 F5    LDA ($F5),Y   ; get ASCII value from decode table
.EAE4  AA       TAX   ; temp store
.EAE5  C4 C5    CPY $C5   ; same key as former interrupt
.EAE7  F0 07    BEQ $EAF0   ; yepp
.EAE9  A0 10    LDY #$10   ; restore the repeat delay counter
.EAEB  8C 8C 02 STY $028C   ; DELAY
.EAEE  D...
