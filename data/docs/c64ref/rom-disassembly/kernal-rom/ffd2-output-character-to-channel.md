---
title: output character to channel
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
- ffd2-output-character-to-channel
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFD2
  address_end: $FFD2
  symbol: output-character-to-channel
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFD2**: do output character to channel'
---

# $FFD2 — output character to channel

## Disassemblatura
```assembly
.FFD2  6C 26 03 JMP ($0326)   ; do output character to channel
```


## Commenti

### Original Disassembly (—)
- **$FFD2**: do output character to channel

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*