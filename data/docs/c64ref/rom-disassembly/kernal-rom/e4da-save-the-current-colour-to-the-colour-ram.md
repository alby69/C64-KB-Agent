---
title: save the current colour to the colour RAM
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
- e4da-hintergrundfarbe-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E4DA
  address_end: $E4DF
  symbol: save-the-current-colour-to-the-colour-ram
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E4DA**: get the current colour code'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E4DA**: Farbe holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E4DA**: get COLOR'
---

# $E4DA — save the current colour to the colour RAM

## Disassemblatura
```assembly
.E4DA  AD 21 D0 LDA $D021   ; get the current colour code
.E4DD  91 F3    STA ($F3),Y   ; save it to the colour RAM
.E4DF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E4DA**: get the current colour code
- **$E4DD**: save it to the colour RAM

### Commodore-64-intern-Buch (Commodore)
- **$E4DA**: Farbe holen
- **$E4DD**: ins Farbram schreiben
- **$E4DF**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E4DA**: get COLOR
- **$E4DD**: and store in current screen position

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*