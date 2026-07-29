---
title: print "? " and get BASIC input
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
- abf9-get-line-into-input-buffer
- cursor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $ABF9
  address_end: $AC03
  symbol: print-and-get-basic-input
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ABF9**: get current I/O channel'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $ABF9 — print "? " and get BASIC input

## Disassemblatura
```assembly
.ABF9  A5 13    LDA $13   ; get current I/O channel
.ABFB  D0 06    BNE $AC03   ; skip "?" prompt if not default channel
.ABFD  20 45 AB JSR $AB45   ; print "?"
.AC00  20 3B AB JSR $AB3B   ; print [SPACE] or [CURSOR RIGHT]
.AC03  4C 60 A5 JMP $A560   ; call for BASIC input and return
```


## Commenti

### Original Disassembly (—)
- **$ABF9**: get current I/O channel
- **$ABFB**: skip "?" prompt if not default channel
- **$ABFD**: print "?"
- **$AC00**: print [SPACE] or [CURSOR RIGHT]
- **$AC03**: call for BASIC input and return

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*