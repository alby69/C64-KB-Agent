---
title: read/set X,Y cursor position
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
- fff0-readset-xy-cursor-position
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFF0
  address_end: $FFF0
  symbol: readset-xy-cursor-position
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFF0**: read/set X,Y cursor position'
---

# $FFF0 — read/set X,Y cursor position

## Disassemblatura
```assembly
.FFF0  4C 0A E5 JMP $E50A   ; read/set X,Y cursor position
```


## Commenti

### Original Disassembly (—)
- **$FFF0**: read/set X,Y cursor position

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*