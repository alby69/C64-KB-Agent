---
title: read I/O status word
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
- ffb7-read-io-status-word
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFB7
  address_end: $FFB7
  symbol: read-io-status-word
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFB7**: read I/O status word'
---

# $FFB7 — read I/O status word

## Disassemblatura
```assembly
.FFB7  4C 07 FE JMP $FE07   ; read I/O status word
```


## Commenti

### Original Disassembly (—)
- **$FFB7**: read I/O status word

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*