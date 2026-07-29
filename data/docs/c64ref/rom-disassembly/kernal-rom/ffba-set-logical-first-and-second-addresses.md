---
title: set logical, first and second addresses
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
- ffba-set-logical-first-and-second-addresses
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFBA
  address_end: $FFBA
  symbol: set-logical-first-and-second-addresses
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFBA**: set logical, first and second addresses'
---

# $FFBA — set logical, first and second addresses

## Disassemblatura
```assembly
.FFBA  4C 00 FE JMP $FE00   ; set logical, first and second addresses
```


## Commenti

### Original Disassembly (—)
- **$FFBA**: set logical, first and second addresses

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*