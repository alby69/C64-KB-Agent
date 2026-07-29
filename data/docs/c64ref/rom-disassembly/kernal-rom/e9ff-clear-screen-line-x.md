---
title: clear screen line X
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
- e9ff-bildschirmzeile-x-lschen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E9FF
  address_end: $EA11
  symbol: clear-screen-line-x
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E9FF**: set number of columns to clear'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E9FF**: 40-1 Spalten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EA01**: set start of line'
---

# $E9FF — clear screen line X

## Disassemblatura
```assembly
.E9FF  A0 27    LDY #$27   ; set number of columns to clear
.EA01  20 F0 E9 JSR $E9F0   ; fetch a screen address
.EA04  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.EA07  20 DA E4 JSR $E4DA   ; save the current colour to the colour RAM
.EA0A  A9 20    LDA #$20   ; set [SPACE]
.EA0C  91 D1    STA ($D1),Y   ; clear character in current screen line
.EA0E  88       DEY   ; decrement index
.EA0F  10 F6    BPL $EA07   ; loop if more to do
.EA11  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E9FF**: set number of columns to clear
- **$EA01**: fetch a screen address
- **$EA04**: calculate the pointer to colour RAM
- **$EA07**: save the current colour to the colour RAM
- **$EA0A**: set [SPACE]
- **$EA0C**: clear character in current screen line
- **$EA0E**: decrement index
- **$EA0F**: loop if more to do

### Commodore-64-intern-Buch (Commodore)
- **$E9FF**: 40-1 Spalten
- **$EA01**: Zeilenpointer (D1/D2) setzen
- **$EA04**: Pointer (F3/F4) für Farb-RAM berechnen
- **$EA07**: Leerzeichen
- **$EA09**: ins Video-RAM schreiben
- **$EA0B**: Hintergrundfarbe setzen
- **$EA0F**: schon 40 Zeichen gelöscht?
- **$EA10**: wenn nicht, fortfahren
- **$EA12**: Rücksprung zum Hauptprogramm
- **$EA13**: Akku retten
- **$EA16**: Blinkzähler bei Repeatfunktion setzen
- **$EA18**: Pointer für Farb-RAM berechnen
- **$EA1B**: Akku wieder holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EA01**: set start of line
- **$EA04**: synchronise colour pointer
- **$EA07**: reset character colour, to COLOR
- **$EA0A**: ASCII space
- **$EA0C**: store character on screen
- **$EA0E**: next
- **$EA0F**: till hole line is done
- **$EA12**: free byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*