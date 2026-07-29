---
title: input byte from serial bus
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
- ffa5-input-byte-from-serial-bus
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFA5
  address_end: $FFA5
  symbol: input-byte-from-serial-bus
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFA5**: input byte from serial bus'
---

# $FFA5 — input byte from serial bus

## Disassemblatura
```assembly
.FFA5  4C 13 EE JMP $EE13   ; input byte from serial bus
```


## Commenti

### Original Disassembly (—)
- **$FFA5**: input byte from serial bus

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*