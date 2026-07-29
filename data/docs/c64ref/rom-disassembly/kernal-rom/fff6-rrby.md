---
title: RRBY
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- fff6-rrby
- fff6-unused
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $FFF6
  address_end: $FFF6
  symbol: rrby
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFF6**: RRBY'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FFFA**: NMI vector'
---

# $FFF6 — RRBY

## Disassemblatura
```assembly
.FFF6  52 52 42 59   ; RRBY
```


## Commenti

### Original Disassembly (—)
- **$FFF6**: RRBY

### Marko Mäkelä (Marko Mäkelä)
- **$FFFA**: NMI vector
- **$FFFC**: RESET vector
- **$FFFE**: IRQ/BRK vector

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*