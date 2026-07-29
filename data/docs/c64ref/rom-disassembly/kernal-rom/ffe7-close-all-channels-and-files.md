---
title: close all channels and files
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
- ffe7-close-all-channels-and-files
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFE7
  address_end: $FFE7
  symbol: close-all-channels-and-files
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFE7**: do close all channels and files'
---

# $FFE7 — close all channels and files

## Disassemblatura
```assembly
.FFE7  6C 2C 03 JMP ($032C)   ; do close all channels and files
```


## Commenti

### Original Disassembly (—)
- **$FFE7**: do close all channels and files

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*