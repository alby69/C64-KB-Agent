---
id: a659-reset-execute-pointer-and-do-clr
type: entity
title: reset execute pointer and do CLR
aliases:
- reset execute pointer and do CLR
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a659-reset-execute-pointer-and-do-clr.md
  sha256: 5cd1adfba99b74449f53a8d91ea08088630b53fa88cbed69d3723e64f56e6b4a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a659-reset-execute-pointer-and-do-clr
---

# reset execute pointer and do CLR



# $A659 — reset execute pointer and do CLR

## Disassemblatura
```assembly
.A659  20 8E A6 JSR $A68E   ; set BASIC execute pointer to start of memory - 1
.A65C  A9 00    LDA #$00   ; set Zb for CLR entry
```


## Commenti

### Original Disassembly (—)
- **$A659**: set BASIC execute pointer to start of memory - 1
- **$A65C**: set Zb for CLR entry

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a659-reset-execute-pointer-and-do-clr]]
