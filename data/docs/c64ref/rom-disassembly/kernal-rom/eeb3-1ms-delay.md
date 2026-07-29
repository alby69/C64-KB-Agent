---
title: 1ms delay
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
- eeb3-verzgerung-1-millisekunde
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EEB3
  address_end: $EEBA
  symbol: 1ms-delay
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EEB3**: save X'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EEB3**: X-Register retten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EEB3**: move (X) to (A)'
---

# $EEB3 — 1ms delay

## Disassemblatura
```assembly
.EEB3  8A       TXA   ; save X
.EEB4  A2 B8    LDX #$B8   ; set the loop count
.EEB6  CA       DEX   ; decrement the loop count
.EEB7  D0 FD    BNE $EEB6   ; loop if more to do
.EEB9  AA       TAX   ; restore X
.EEBA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEB3**: save X
- **$EEB4**: set the loop count
- **$EEB6**: decrement the loop count
- **$EEB7**: loop if more to do
- **$EEB9**: restore X

### Commodore-64-intern-Buch (Commodore)
- **$EEB3**: X-Register retten
- **$EEB4**: X-Register mit $B8 laden
- **$EEB6**: herunterzählen
- **$EEB7**: verzweige wenn nicht fertig
- **$EEB9**: X-Register wiederherstellen
- **$EEBA**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EEB3**: move (X) to (A)
- **$EEB4**: start value
- **$EEB6**: decrement
- **$EEB7**: until zero
- **$EEB9**: (A) to (X)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*