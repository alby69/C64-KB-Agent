---
title: bump tape pointer
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
- f80d-bandpufferzeiger-erhhen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F80D
  address_end: $F816
  symbol: bump-tape-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F80D**: get tape buffer start pointer in XY'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F80D**: Bandpufferadresse holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F80D — bump tape pointer

## Disassemblatura
```assembly
.F80D  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F810  E6 A6    INC $A6   ; increment tape buffer index
.F812  A4 A6    LDY $A6   ; get tape buffer index
.F814  C0 C0    CPY #$C0   ; compare with buffer length
.F816  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F80D**: get tape buffer start pointer in XY
- **$F810**: increment tape buffer index
- **$F812**: get tape buffer index
- **$F814**: compare with buffer length

### Commodore-64-intern-Buch (Commodore)
- **$F80D**: Bandpufferadresse holen
- **$F810**: Zeiger erhöhen
- **$F812**: und laden um
- **$F814**: mit Maximalwert (192) zu vergleichen
- **$F816**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*