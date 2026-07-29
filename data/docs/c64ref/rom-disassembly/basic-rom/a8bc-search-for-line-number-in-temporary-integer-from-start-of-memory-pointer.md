---
title: search for line number in temporary integer from start of memory pointer
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
- a8bc-search-for-line-number-in-temporary-integer-from-start-of-memory-pointer
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $A8BC
  address_end: $A8BE
  symbol: search-for-line-number-in-temporary-integer-from-start-of-memory-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A8BC**: get start of memory low byte'
---

# $A8BC — search for line number in temporary integer from start of memory pointer

## Disassemblatura
```assembly
.A8BC  A5 2B    LDA $2B   ; get start of memory low byte
.A8BE  A6 2C    LDX $2C   ; get start of memory high byte
```


## Commenti

### Original Disassembly (—)
- **$A8BC**: get start of memory low byte
- **$A8BE**: get start of memory high byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*