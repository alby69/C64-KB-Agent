---
title: read/set vectored I/O
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
- ff8d-readset-vectored-io
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF8D
  address_end: $FF8D
  symbol: readset-vectored-io
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF8D**: read/set vectored I/O'
---

# $FF8D — read/set vectored I/O

## Disassemblatura
```assembly
.FF8D  4C 1A FD JMP $FD1A   ; read/set vectored I/O
```


## Commenti

### Original Disassembly (—)
- **$FF8D**: read/set vectored I/O

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*