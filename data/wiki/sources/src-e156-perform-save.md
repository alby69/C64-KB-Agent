---
id: src-e156-perform-save
type: source
title: 'Source Summary: perform SAVE'
aliases:
- perform SAVE
- e156-perform-save.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e156-perform-save.md
  sha256: 75408926bb50ba113f520421f56358e5cd5e3046989411b95f6c3140a86da574
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform SAVE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e156-perform-save.md`
**SHA256**: `75408926bb50ba113f520421f56358e5cd5e3046989411b95f6c3140a86da574`

## Summary



# $E156 — perform SAVE

## Disassemblatura
```assembly
.E156  20 D4 E1 JSR $E1D4   ; get parameters for LOAD/SAVE
.E159  A6 2D    LDX $2D   ; get start of variables low byte
.E15B  A4 2E    LDY $2E   ; get start of variables high byte
.E15D  A9 2B    LDA #$2B   ; index to start of program memory
.E15F  20 D8 FF JSR $FFD8   ; save RAM to device, A = index to start address, XY = end address low/high
.E162  B0 95    BCS $E0F9   ; if error go handle BASIC I/O error
.E164  60       RTS
```


## Com...
