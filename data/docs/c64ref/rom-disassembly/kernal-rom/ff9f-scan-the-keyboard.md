---
title: scan the keyboard
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
- ff9f-scan-the-keyboard
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF9F
  address_end: $FF9F
  symbol: scan-the-keyboard
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF9F**: scan keyboard'
---

# $FF9F — scan the keyboard

## Disassemblatura
```assembly
.FF9F  4C 87 EA JMP $EA87   ; scan keyboard
```


## Commenti

### Original Disassembly (—)
- **$FF9F**: scan keyboard

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*