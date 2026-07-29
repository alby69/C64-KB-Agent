---
title: command serial bus to UNTALK
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
- ffab-command-serial-bus-to-untalk
- untalk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFAB
  address_end: $FFAB
  symbol: command-serial-bus-to-untalk
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFAB**: command serial bus to UNTALK'
---

# $FFAB — command serial bus to UNTALK

## Disassemblatura
```assembly
.FFAB  4C EF ED JMP $EDEF   ; command serial bus to UNTALK
```


## Commenti

### Original Disassembly (—)
- **$FFAB**: command serial bus to UNTALK

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*