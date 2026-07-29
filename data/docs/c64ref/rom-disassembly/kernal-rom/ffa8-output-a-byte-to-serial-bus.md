---
title: output a byte to serial bus
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
- ffa8-output-a-byte-to-serial-bus
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFA8
  address_end: $FFA8
  symbol: output-a-byte-to-serial-bus
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFA8**: output byte to serial bus'
---

# $FFA8 — output a byte to serial bus

## Disassemblatura
```assembly
.FFA8  4C DD ED JMP $EDDD   ; output byte to serial bus
```


## Commenti

### Original Disassembly (—)
- **$FFA8**: output byte to serial bus

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*