---
title: get the tape buffer start pointer
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
- f7d0-und-prfen-ob-gltig
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F7D0
  address_end: $F7D6
  symbol: get-the-tape-buffer-start-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F7D0**: get tape buffer start pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F7D0**: Anfang Bandpuffer LOW in X'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F7D0 — get the tape buffer start pointer

## Disassemblatura
```assembly
.F7D0  A6 B2    LDX $B2   ; get tape buffer start pointer low byte
.F7D2  A4 B3    LDY $B3   ; get tape buffer start pointer high byte
.F7D4  C0 02    CPY #$02   ; compare high byte with $02xx
.F7D6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F7D0**: get tape buffer start pointer low byte
- **$F7D2**: get tape buffer start pointer high byte
- **$F7D4**: compare high byte with $02xx

### Commodore-64-intern-Buch (Commodore)
- **$F7D0**: Anfang Bandpuffer LOW in X
- **$F7D2**: Anfang Bandpuffer HIGH in Y
- **$F7D4**: Adresse kleiner $200 ?
- **$F7D6**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*