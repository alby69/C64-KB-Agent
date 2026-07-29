---
title: command serial bus to UNLISTEN
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
- ffae-command-serial-bus-to-unlisten
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFAE
  address_end: $FFAE
  symbol: command-serial-bus-to-unlisten
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFAE**: command serial bus to UNLISTEN'
---

# $FFAE — command serial bus to UNLISTEN

## Disassemblatura
```assembly
.FFAE  4C FE ED JMP $EDFE   ; command serial bus to UNLISTEN
```


## Commenti

### Original Disassembly (—)
- **$FFAE**: command serial bus to UNLISTEN

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*