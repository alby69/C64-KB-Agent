---
title: increment real time clock
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
- ffea-increment-real-time-clock
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFEA
  address_end: $FFEA
  symbol: increment-real-time-clock
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFEA**: increment real time clock'
---

# $FFEA — increment real time clock

## Disassemblatura
```assembly
.FFEA  4C 9B F6 JMP $F69B   ; increment real time clock
```


## Commenti

### Original Disassembly (—)
- **$FFEA**: increment real time clock

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*