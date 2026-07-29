---
title: input character from channel
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
- ffcf-input-character-from-channel
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFCF
  address_end: $FFCF
  symbol: input-character-from-channel
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFCF**: do input character from channel'
---

# $FFCF — input character from channel

## Disassemblatura
```assembly
.FFCF  6C 24 03 JMP ($0324)   ; do input character from channel
```


## Commenti

### Original Disassembly (—)
- **$FFCF**: do input character from channel

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*