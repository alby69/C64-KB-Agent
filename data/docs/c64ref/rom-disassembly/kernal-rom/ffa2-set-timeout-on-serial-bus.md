---
title: set timeout on serial bus
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
- ffa2-set-timeout-on-serial-bus
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFA2
  address_end: $FFA2
  symbol: set-timeout-on-serial-bus
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFA2**: set timeout on serial bus'
---

# $FFA2 — set timeout on serial bus

## Disassemblatura
```assembly
.FFA2  4C 21 FE JMP $FE21   ; set timeout on serial bus
```


## Commenti

### Original Disassembly (—)
- **$FFA2**: set timeout on serial bus

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*