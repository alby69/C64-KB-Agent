---
id: fe27-read-the-top-of-memory
type: entity
title: read the top of memory
aliases:
- read the top of memory
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe27-read-the-top-of-memory.md
  sha256: b16add886f1067e262dfc93799154a0cb6c624722b9390fe0c9d1cb8eb348362
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe27-read-the-top-of-memory
---

# read the top of memory



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
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe27-read-the-top-of-memory]]
