---
title: RAM test and find RAM end
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
- ff87-ram-test-and-find-ram-end
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF87
  address_end: $FF87
  symbol: ram-test-and-find-ram-end
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF87**: RAM test and find RAM end'
---

# $FF87 — RAM test and find RAM end

## Disassemblatura
```assembly
.FF87  4C 50 FD JMP $FD50   ; RAM test and find RAM end
```


## Commenti

### Original Disassembly (—)
- **$FF87**: RAM test and find RAM end

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*