---
title: set the top of memory to F0xx
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f47d-set-the-top-of-memory-to-f0xx
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $F47D
  address_end: $F480
  symbol: set-the-top-of-memory-to-f0xx
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F47D**: read the top of memory'
---

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
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*