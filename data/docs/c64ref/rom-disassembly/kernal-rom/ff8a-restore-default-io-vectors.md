---
title: restore default I/O vectors
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
- ff8a-restore-default-io-vectors
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF8A
  address_end: $FF8A
  symbol: restore-default-io-vectors
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF8A**: restore default I/O vectors'
---

# $FF8A — restore default I/O vectors

## Disassemblatura
```assembly
.FF8A  4C 15 FD JMP $FD15   ; restore default I/O vectors
```


## Commenti

### Original Disassembly (—)
- **$FF8A**: restore default I/O vectors

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*