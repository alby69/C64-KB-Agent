---
id: src-fe2d-set-the-top-of-memory
type: source
title: 'Source Summary: set the top of memory'
aliases:
- set the top of memory
- fe2d-set-the-top-of-memory.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe2d-set-the-top-of-memory.md
  sha256: 867c116a61b0881076e1210b8ba46149c1edd076c03454a51273f775e8b5e69f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the top of memory

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe2d-set-the-top-of-memory.md`
**SHA256**: `867c116a61b0881076e1210b8ba46149c1edd076c03454a51273f775e8b5e69f`

## Summary



# $FE2D — set the top of memory

## Disassemblatura
```assembly
.FE2D  8E 83 02 STX $0283   ; set memory top low byte
.FE30  8C 84 02 STY $0284   ; set memory top high byte
.FE33  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE2D**: set memory top low byte
- **$FE30**: set memory top high byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
