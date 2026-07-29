---
title: unused bytes
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
- ff41-unused-bytes
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF41
  address_end: $FF42
  symbol: unused-bytes
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF41**: waste cycles'
---

# $FF41 — unused bytes

## Disassemblatura
```assembly
.FF41  EA       NOP   ; waste cycles
.FF42  EA       NOP   ; waste cycles
```


## Commenti

### Original Disassembly (—)
- **$FF41**: waste cycles
- **$FF42**: waste cycles

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*