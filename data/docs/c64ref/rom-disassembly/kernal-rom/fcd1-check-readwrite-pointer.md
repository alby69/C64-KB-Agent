---
title: check read/write pointer
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
- fcd1-endadresse
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FCD1
  address_end: $FCDA
  symbol: check-readwrite-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FCD1**: set carry for subtract'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FCD1**: Carry für Subtraktion vorbereiten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FCD1 — check read/write pointer

## Disassemblatura
```assembly
.FCD1  38       SEC   ; set carry for subtract
.FCD2  A5 AC    LDA $AC   ; get buffer address low byte
.FCD4  E5 AE    SBC $AE   ; subtract buffer end low byte
.FCD6  A5 AD    LDA $AD   ; get buffer address high byte
.FCD8  E5 AF    SBC $AF   ; subtract buffer end high byte
.FCDA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCD1**: set carry for subtract
- **$FCD2**: get buffer address low byte
- **$FCD4**: subtract buffer end low byte
- **$FCD6**: get buffer address high byte
- **$FCD8**: subtract buffer end high byte

### Commodore-64-intern-Buch (Commodore)
- **$FCD1**: Carry für Subtraktion vorbereiten
- **$FCD2**: laufende Adresse
- **$FCD4**: $AC/$AD
- **$FCD6**: Endadresse
- **$FCD8**: $AE/$AF
- **$FCDA**: Rücksprung
- **$FCDB**: Adreßzeiger
- **$FCDD**: er-
- **$FCDF**: höhen
- **$FCE1**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*