---
title: get character from input device
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
- ffe4-get-character-from-input-device
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFE4
  address_end: $FFE4
  symbol: get-character-from-input-device
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFE4**: do get character from input device'
---

# $FFE4 — get character from input device

## Disassemblatura
```assembly
.FFE4  6C 2A 03 JMP ($032A)   ; do get character from input device
```


## Commenti

### Original Disassembly (—)
- **$FFE4**: do get character from input device

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*