---
title: calculate pointers to screen lines colour RAM
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
- e9e0-scrollzeile-berechnen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E9E0
  address_end: $E9EF
  symbol: calculate-pointers-to-screen-lines-colour-ram
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E9E0**: calculate the pointer to the current screen line colour
      RAM'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E9E0**: Zeiger auf Farb-RAM berechnen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E9E0**: synchronise colour pointer'
---

# $E9E0 — calculate pointers to screen lines colour RAM

## Disassemblatura
```assembly
.E9E0  20 24 EA JSR $EA24   ; calculate the pointer to the current screen line colour RAM
.E9E3  A5 AC    LDA $AC   ; get the next screen line pointer low byte
.E9E5  85 AE    STA $AE   ; save the next screen line colour RAM pointer low byte
.E9E7  A5 AD    LDA $AD   ; get the next screen line pointer high byte
.E9E9  29 03    AND #$03   ; mask 0000 00xx, line memory page
.E9EB  09 D8    ORA #$D8   ; set  1101 01xx, colour memory page
.E9ED  85 AF    STA $AF   ; save the next screen line colour RAM pointer high byte
.E9EF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E9E0**: calculate the pointer to the current screen line colour RAM
- **$E9E3**: get the next screen line pointer low byte
- **$E9E5**: save the next screen line colour RAM pointer low byte
- **$E9E7**: get the next screen line pointer high byte
- **$E9E9**: mask 0000 00xx, line memory page
- **$E9EB**: set  1101 01xx, colour memory page
- **$E9ED**: save the next screen line colour RAM pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$E9E0**: Zeiger auf Farb-RAM berechnen
- **$E9E3**: Zeiger
- **$E9E5**: für Zeile
- **$E9E7**: speichern
- **$E9E9**: Startadresse
- **$E9EB**: des Video-RAM
- **$E9ED**: berechnen
- **$E9EF**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E9E0**: synchronise colour pointer
- **$E9E3**: SAL, pointer for screen scroll
- **$E9E5**: EAL
- **$E9EB**: setup colour ram to $d800

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*