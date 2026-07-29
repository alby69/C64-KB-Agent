---
title: display "LOADING" or "VERIFYING"
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
- f5d2-loadingverifying-ausgeben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F5D2
  address_end: $F5DA
  symbol: display-loading-or-verifying
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F5D2**: point to "LOADING"'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F5D2**: Offset für ''LOADING'''
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F5D2**: offset to verify message'
---

# $F5D2 — display "LOADING" or "VERIFYING"

## Disassemblatura
```assembly
.F5D2  A0 49    LDY #$49   ; point to "LOADING"
.F5D4  A5 93    LDA $93   ; get load/verify flag
.F5D6  F0 02    BEQ $F5DA   ; branch if load
.F5D8  A0 59    LDY #$59   ; point to "VERIFYING"
.F5DA  4C 2B F1 JMP $F12B   ; display kernel I/O message if in direct mode and return
```


## Commenti

### Original Disassembly (—)
- **$F5D2**: point to "LOADING"
- **$F5D4**: get load/verify flag
- **$F5D6**: branch if load
- **$F5D8**: point to "VERIFYING"
- **$F5DA**: display kernel I/O message if in direct mode and return

### Commodore-64-intern-Buch (Commodore)
- **$F5D2**: Offset für 'LOADING'
- **$F5D4**: Load/Verify-Flag laden
- **$F5D6**: Load wenn 0, dann ausgeben
- **$F5D8**: sonst Offset für 'VERIFYING'
- **$F5DA**: Meldung ausgeben, Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F5D2**: offset to verify message
- **$F5D4**: VERCK, load/verify flag
- **$F5D6**: verify
- **$F5D8**: offset to load message
- **$F5DA**: output message flagged by (Y)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*