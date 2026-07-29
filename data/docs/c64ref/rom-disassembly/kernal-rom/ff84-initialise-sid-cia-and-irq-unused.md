---
title: initialise SID, CIA and IRQ, unused
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
- ff84-initialise-sid-cia-and-irq-unused
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF84
  address_end: $FF84
  symbol: initialise-sid-cia-and-irq-unused
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF84**: initialise SID, CIA and IRQ'
---

# $FF84 — initialise SID, CIA and IRQ, unused

## Disassemblatura
```assembly
.FF84  4C A3 FD JMP $FDA3   ; initialise SID, CIA and IRQ
```


## Commenti

### Original Disassembly (—)
- **$FF84**: initialise SID, CIA and IRQ

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*