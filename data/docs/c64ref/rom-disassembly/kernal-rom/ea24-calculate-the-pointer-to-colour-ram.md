---
title: calculate the pointer to colour RAM
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
- ea24-zeiger-auf-farb-ram-berechnen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EA24
  address_end: $EA30
  symbol: calculate-the-pointer-to-colour-ram
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EA24**: get current screen line pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EA24**: $D1/$D2 = Zeiger auf Video-RAM-Position'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EA24**: copy screen line low byte'
---

# $EA24 — calculate the pointer to colour RAM

## Disassemblatura
```assembly
.EA24  A5 D1    LDA $D1   ; get current screen line pointer low byte
.EA26  85 F3    STA $F3   ; save pointer to colour RAM low byte
.EA28  A5 D2    LDA $D2   ; get current screen line pointer high byte
.EA2A  29 03    AND #$03   ; mask 0000 00xx, line memory page
.EA2C  09 D8    ORA #$D8   ; set  1101 01xx, colour memory page
.EA2E  85 F4    STA $F4   ; save pointer to colour RAM high byte
.EA30  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EA24**: get current screen line pointer low byte
- **$EA26**: save pointer to colour RAM low byte
- **$EA28**: get current screen line pointer high byte
- **$EA2A**: mask 0000 00xx, line memory page
- **$EA2C**: set  1101 01xx, colour memory page
- **$EA2E**: save pointer to colour RAM high byte

### Commodore-64-intern-Buch (Commodore)
- **$EA24**: $D1/$D2 = Zeiger auf Video-RAM-Position
- **$EA26**: LOW-Byte auf Zeichenposition = LOW-Byte auf Farbposition
- **$EA28**: HIGH-Byte der Zeichenposition
- **$EA2A**: mit HIGH-Byte der Farb-RAM-
- **$EA2C**: Position = $D8 verknüpfen und
- **$EA2E**: in $F4 = speichern
- **$EA30**: Rücksprung zum Hauptprogramm

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EA24**: copy screen line low byte
- **$EA26**: to colour RAM low byte
- **$EA28**: read'n modify the hi byte
- **$EA2E**: to suite the colour RAM

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*