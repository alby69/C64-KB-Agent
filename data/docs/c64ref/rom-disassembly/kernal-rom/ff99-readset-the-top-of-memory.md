---
title: read/set the top of memory
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
- ff99-readset-the-top-of-memory
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF99
  address_end: $FF99
  symbol: readset-the-top-of-memory
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF99**: read/set the top of memory'
---

# $FF99 — read/set the top of memory

## Disassemblatura
```assembly
.FF99  4C 25 FE JMP $FE25   ; read/set the top of memory
```


## Commenti

### Original Disassembly (—)
- **$FF99**: read/set the top of memory

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*