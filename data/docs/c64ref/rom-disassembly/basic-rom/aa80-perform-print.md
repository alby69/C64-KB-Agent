---
title: perform PRINT#
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- aa80-basic-befehl-print
- ab45-print
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AA80
  address_end: $AA83
  symbol: perform-print
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AA80**: perform CMD'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AA80**: CMD-Befehl'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AA80 — perform PRINT#

## Disassemblatura
```assembly
.AA80  20 86 AA JSR $AA86   ; perform CMD
.AA83  4C B5 AB JMP $ABB5   ; close input and output channels and return
```


## Commenti

### Original Disassembly (—)
- **$AA80**: perform CMD
- **$AA83**: close input and output channels and return

### Commodore-64-intern-Buch (Commodore)
- **$AA80**: CMD-Befehl
- **$AA83**: und CLRCH

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*