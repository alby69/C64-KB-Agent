---
id: src-f47d-set-the-top-of-memory-to-f0xx
type: source
title: 'Source Summary: set the top of memory to F0xx'
aliases:
- set the top of memory to F0xx
- f47d-set-the-top-of-memory-to-f0xx.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f47d-set-the-top-of-memory-to-f0xx.md
  sha256: 22518c3f1e18e3d8df20897e554a04d3a2d871a6f0e9475eefc8032d2cf2e5ea
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the top of memory to F0xx

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f47d-set-the-top-of-memory-to-f0xx.md`
**SHA256**: `22518c3f1e18e3d8df20897e554a04d3a2d871a6f0e9475eefc8032d2cf2e5ea`

## Summary



# $F47D — set the top of memory to F0xx

## Disassemblatura
```assembly
.F47D  38       SEC   ; read the top of memory
.F47E  A9 F0    LDA #$F0   ; set $F000
.F480  4C 2D FE JMP $FE2D   ; set the top of memory and return
```


## Commenti

### Original Disassembly (—)
- **$F47D**: read the top of memory
- **$F47E**: set $F000
- **$F480**: set the top of memory and return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
