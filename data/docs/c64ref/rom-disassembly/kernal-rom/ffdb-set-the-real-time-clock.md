---
title: set the real time clock
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
- ffdb-set-the-real-time-clock
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFDB
  address_end: $FFDB
  symbol: set-the-real-time-clock
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFDB**: set real time clock'
---

# $FFDB — set the real time clock

## Disassemblatura
```assembly
.FFDB  4C E4 F6 JMP $F6E4   ; set real time clock
```


## Commenti

### Original Disassembly (—)
- **$FFDB**: set real time clock

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*