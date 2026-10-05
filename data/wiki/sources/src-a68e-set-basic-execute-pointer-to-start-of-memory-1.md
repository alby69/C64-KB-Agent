---
id: src-a68e-set-basic-execute-pointer-to-start-of-memory-1
type: source
title: 'Source Summary: set BASIC execute pointer to start of memory - 1'
aliases:
- set BASIC execute pointer to start of memory - 1
- a68e-set-basic-execute-pointer-to-start-of-memory-1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a68e-set-basic-execute-pointer-to-start-of-memory-1.md
  sha256: 469b064b65217a7d132cb8e5dd737bf6e9612e26f00faebbfa821c21147f7d88
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set BASIC execute pointer to start of memory - 1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a68e-set-basic-execute-pointer-to-start-of-memory-1.md`
**SHA256**: `469b064b65217a7d132cb8e5dd737bf6e9612e26f00faebbfa821c21147f7d88`

## Summary



# $A68E — set BASIC execute pointer to start of memory - 1

## Disassemblatura
```assembly
.A68E  18       CLC   ; clear carry for add
.A68F  A5 2B    LDA $2B   ; get start of memory low byte
.A691  69 FF    ADC #$FF   ; add -1 low byte
.A693  85 7A    STA $7A   ; set BASIC execute pointer low byte
.A695  A5 2C    LDA $2C   ; get start of memory high byte
.A697  69 FF    ADC #$FF   ; add -1 high byte
.A699  85 7B    STA $7B   ; save BASIC execute pointer high byte
.A69B  60       RTS
```


## ...
