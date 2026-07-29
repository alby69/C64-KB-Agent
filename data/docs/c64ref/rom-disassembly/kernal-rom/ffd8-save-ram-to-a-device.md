---
title: save RAM to a device
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
- ffd8-save-ram-to-a-device
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFD8
  address_end: $FFD8
  symbol: save-ram-to-a-device
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFD8**: save RAM to device'
---

# $FFD8 — save RAM to a device

## Disassemblatura
```assembly
.FFD8  4C DD F5 JMP $F5DD   ; save RAM to device
```


## Commenti

### Original Disassembly (—)
- **$FFD8**: save RAM to device

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*