---
title: perform SAVE
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
- e156-save-befehl
- ece7-load
- f5ed-save
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E156
  address_end: $E164
  symbol: perform-save
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E156**: get parameters for LOAD/SAVE'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E156**: Parameter (Filenamen, Prim, und Sek. Adresse)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E156**: get SAVE parameters from text'
---

# $E156 — perform SAVE

## Disassemblatura
```assembly
.E156  20 D4 E1 JSR $E1D4   ; get parameters for LOAD/SAVE
.E159  A6 2D    LDX $2D   ; get start of variables low byte
.E15B  A4 2E    LDY $2E   ; get start of variables high byte
.E15D  A9 2B    LDA #$2B   ; index to start of program memory
.E15F  20 D8 FF JSR $FFD8   ; save RAM to device, A = index to start address, XY = end address low/high
.E162  B0 95    BCS $E0F9   ; if error go handle BASIC I/O error
.E164  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E156**: get parameters for LOAD/SAVE
- **$E159**: get start of variables low byte
- **$E15B**: get start of variables high byte
- **$E15D**: index to start of program memory
- **$E15F**: save RAM to device, A = index to start address, XY = end address low/high
- **$E162**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E156**: Parameter (Filenamen, Prim, und Sek. Adresse)
- **$E159**: Endadresse gleich
- **$E15B**: BASIC-Rücksprung
- **$E15D**: Startadresse gleich Zeiger auf BASIC Anfang
- **$E15F**: Save-Routine
- **$E162**: Fehler ?
- **$E164**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E156**: get SAVE parameters from text
- **$E159**: VARTAB, start of variables
- **$E15D**: <TXTTAB, start of BASIC text
- **$E15F**: execute SAVE
- **$E162**: if carry is set, handle I/O errors

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*