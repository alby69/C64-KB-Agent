---
title: read the top of memory
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
- fe27-read-the-top-of-memory
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FE27
  address_end: $FE2A
  symbol: read-the-top-of-memory
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE27**: get memory top low byte'
---

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