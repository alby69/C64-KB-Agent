---
title: set the top of memory
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
- fe2d-set-the-top-of-memory
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FE2D
  address_end: $FE33
  symbol: set-the-top-of-memory
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE2D**: set memory top low byte'
---

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
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*