---
title: read the real time clock
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
- ffde-read-the-real-time-clock
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFDE
  address_end: $FFDE
  symbol: read-the-real-time-clock
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFDE**: read real time clock'
---

# $FFDE — read the real time clock

## Disassemblatura
```assembly
.FFDE  4C DD F6 JMP $F6DD   ; read real time clock
```


## Commenti

### Original Disassembly (—)
- **$FFDE**: read real time clock

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*