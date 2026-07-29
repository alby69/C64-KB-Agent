---
title: keyboard buffer for auto load/run
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
- ece7-runstop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $ECE7
  address_end: $ECEF
  symbol: keyboard-buffer-for-auto-loadrun
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ECE7**: ''load (cr) run (cr)'''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$ECE7**: ''load (cr) run (cr)'''
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$ECE7**: LOAD <CR> RUN <CR>'
---

# $ECE7 — keyboard buffer for auto load/run

## Disassemblatura
```assembly
.ECE7  4C 4F 41 44 0D 52 55 4E   ; 'load (cr) run (cr)'
.ECEF  0D
```


## Commenti

### Original Disassembly (—)
- **$ECE7**: 'load (cr) run (cr)'

### Commodore-64-intern-Buch (Commodore)
- **$ECE7**: 'load (cr) run (cr)'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$ECE7**: LOAD <CR> RUN <CR>

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*