---
title: reset execute pointer and do CLR
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a659-reset-execute-pointer-and-do-clr
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $A659
  address_end: $A65C
  symbol: reset-execute-pointer-and-do-clr
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A659**: set BASIC execute pointer to start of memory - 1'
---

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