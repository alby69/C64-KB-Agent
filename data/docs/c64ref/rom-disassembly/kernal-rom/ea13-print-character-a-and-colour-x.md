---
title: print character A and colour X
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
- ea13-print-to-screen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $EA13
  address_end: $EA1B
  symbol: print-character-a-and-colour-x
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EA13**: copy the character'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EA13**: put print character in (Y)'
---

# $EA13 — print character A and colour X

## Disassemblatura
```assembly
.EA13  A8       TAY   ; copy the character
.EA14  A9 02    LDA #$02   ; set the count to $02, usually $14 ??
.EA16  85 CD    STA $CD   ; save the cursor countdown
.EA18  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.EA1B  98       TYA   ; get the character back
```


## Commenti

### Original Disassembly (—)
- **$EA13**: copy the character
- **$EA14**: set the count to $02, usually $14 ??
- **$EA16**: save the cursor countdown
- **$EA18**: calculate the pointer to colour RAM
- **$EA1B**: get the character back

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EA13**: put print character in (Y)
- **$EA16**: store initial value in BLNCT, timer to toggle cursor
- **$EA18**: synchronise colour pointer
- **$EA1B**: print character back to (A)
- **$EA1C**: PNTR, cursor column on line
- **$EA1E**: store character on screen
- **$EA21**: store character colour

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*