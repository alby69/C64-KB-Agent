---
title: scan the stop key
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
- ffe1-scan-the-stop-key
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFE1
  address_end: $FFE1
  symbol: scan-the-stop-key
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFE1**: do scan stop key'
---

# $FFE1 — scan the stop key

## Disassemblatura
```assembly
.FFE1  6C 28 03 JMP ($0328)   ; do scan stop key
```


## Commenti

### Original Disassembly (—)
- **$FFE1**: do scan stop key

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*