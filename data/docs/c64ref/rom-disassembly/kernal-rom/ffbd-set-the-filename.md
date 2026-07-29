---
title: set the filename
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
- ffbd-set-the-filename
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFBD
  address_end: $FFBD
  symbol: set-the-filename
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFBD**: set the filename'
---

# $FFBD — set the filename

## Disassemblatura
```assembly
.FFBD  4C F9 FD JMP $FDF9   ; set the filename
```


## Commenti

### Original Disassembly (—)
- **$FFBD**: set the filename

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*