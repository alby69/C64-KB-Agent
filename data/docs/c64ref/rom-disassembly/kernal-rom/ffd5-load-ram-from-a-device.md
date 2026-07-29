---
title: load RAM from a device
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
- ffd5-load-ram-from-a-device
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFD5
  address_end: $FFD5
  symbol: load-ram-from-a-device
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFD5**: load RAM from a device'
---

# $FFD5 — load RAM from a device

## Disassemblatura
```assembly
.FFD5  4C 9E F4 JMP $F49E   ; load RAM from a device
```


## Commenti

### Original Disassembly (—)
- **$FFD5**: load RAM from a device

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*