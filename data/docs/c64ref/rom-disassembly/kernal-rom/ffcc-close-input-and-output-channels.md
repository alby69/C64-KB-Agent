---
title: close input and output channels
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
- ffcc-close-input-and-output-channels
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFCC
  address_end: $FFCC
  symbol: close-input-and-output-channels
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFCC**: do close input and output channels'
---

# $FFCC — close input and output channels

## Disassemblatura
```assembly
.FFCC  6C 22 03 JMP ($0322)   ; do close input and output channels
```


## Commenti

### Original Disassembly (—)
- **$FFCC**: do close input and output channels

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*