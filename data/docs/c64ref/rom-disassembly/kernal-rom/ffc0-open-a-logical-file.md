---
title: open a logical file
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
- ffc0-open-a-logical-file
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFC0
  address_end: $FFC0
  symbol: open-a-logical-file
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFC0**: do open a logical file'
---

# $FFC0 — open a logical file

## Disassemblatura
```assembly
.FFC0  6C 1A 03 JMP ($031A)   ; do open a logical file
```


## Commenti

### Original Disassembly (—)
- **$FFC0**: do open a logical file

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*