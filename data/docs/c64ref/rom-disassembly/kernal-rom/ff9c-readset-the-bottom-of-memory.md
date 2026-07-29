---
title: read/set the bottom of memory
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
- ff9c-readset-the-bottom-of-memory
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF9C
  address_end: $FF9C
  symbol: readset-the-bottom-of-memory
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF9C**: read/set the bottom of memory'
---

# $FF9C — read/set the bottom of memory

## Disassemblatura
```assembly
.FF9C  4C 34 FE JMP $FE34   ; read/set the bottom of memory
```


## Commenti

### Original Disassembly (—)
- **$FF9C**: read/set the bottom of memory

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*