---
id: src-fe27-read-the-top-of-memory
type: source
title: 'Source Summary: read the top of memory'
aliases:
- read the top of memory
- fe27-read-the-top-of-memory.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe27-read-the-top-of-memory.md
  sha256: b16add886f1067e262dfc93799154a0cb6c624722b9390fe0c9d1cb8eb348362
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: read the top of memory

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe27-read-the-top-of-memory.md`
**SHA256**: `b16add886f1067e262dfc93799154a0cb6c624722b9390fe0c9d1cb8eb348362`

## Summary



# $FE27 — read the top of memory

## Disassemblatura
```assembly
.FE27  AE 83 02 LDX $0283   ; get memory top low byte
.FE2A  AC 84 02 LDY $0284   ; get memory top high byte
```


## Commenti

### Original Disassembly (—)
- **$FE27**: get memory top low byte
- **$FE2A**: get memory top high byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
