---
id: src-a8fb-add-y-to-the-basic-execute-pointer
type: source
title: 'Source Summary: add Y to the BASIC execute pointer'
aliases:
- add Y to the BASIC execute pointer
- a8fb-add-y-to-the-basic-execute-pointer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a8fb-add-y-to-the-basic-execute-pointer.md
  sha256: 04aa9b000b9d5b33407b6474ddb48c71c16c839d320eea5fcc7de0920c29cb09
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: add Y to the BASIC execute pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a8fb-add-y-to-the-basic-execute-pointer.md`
**SHA256**: `04aa9b000b9d5b33407b6474ddb48c71c16c839d320eea5fcc7de0920c29cb09`

## Summary



# $A8FB — add Y to the BASIC execute pointer

## Disassemblatura
```assembly
.A8FB  98       TYA   ; copy index to A
.A8FC  18       CLC   ; clear carry for add
.A8FD  65 7A    ADC $7A   ; add BASIC execute pointer low byte
.A8FF  85 7A    STA $7A   ; save BASIC execute pointer low byte
.A901  90 02    BCC $A905   ; skip increment if no carry
.A903  E6 7B    INC $7B   ; else increment BASIC execute pointer high byte
.A905  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A8FB*...
