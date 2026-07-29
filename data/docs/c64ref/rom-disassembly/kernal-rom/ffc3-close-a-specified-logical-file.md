---
title: close a specified logical file
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
- ffc3-close-a-specified-logical-file
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFC3
  address_end: $FFC3
  symbol: close-a-specified-logical-file
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFC3**: do close a specified logical file'
---

# $FFC3 — close a specified logical file

## Disassemblatura
```assembly
.FFC3  6C 1C 03 JMP ($031C)   ; do close a specified logical file
```


## Commenti

### Original Disassembly (—)
- **$FFC3**: do close a specified logical file

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*