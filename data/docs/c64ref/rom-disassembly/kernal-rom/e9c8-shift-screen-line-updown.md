---
title: shift screen line up/down
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
- e9c8-zeile-nach-oben-schieben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E9C8
  address_end: $E9DF
  symbol: shift-screen-line-updown
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E9C8**: mask 0000 00xx, line memory page'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E9C8**: Bildschirmzeiger'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E9CA**: HIBASE, top of screen page'
---

# $E9C8 — shift screen line up/down

## Disassemblatura
```assembly
.E9C8  29 03    AND #$03   ; mask 0000 00xx, line memory page
.E9CA  0D 88 02 ORA $0288   ; OR with screen memory page
.E9CD  85 AD    STA $AD   ; save next/previous line pointer high byte
.E9CF  20 E0 E9 JSR $E9E0   ; calculate pointers to screen lines colour RAM
.E9D2  A0 27    LDY #$27   ; set the column count
.E9D4  B1 AC    LDA ($AC),Y   ; get character from next/previous screen line
.E9D6  91 D1    STA ($D1),Y   ; save character to current screen line
.E9D8  B1 AE    LDA ($AE),Y   ; get colour from next/previous screen line colour RAM
.E9DA  91 F3    STA ($F3),Y   ; save colour to current screen line colour RAM
.E9DC  88       DEY   ; decrement column index/count
.E9DD  10 F5    BPL $E9D4   ; loop if more to do
.E9DF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E9C8**: mask 0000 00xx, line memory page
- **$E9CA**: OR with screen memory page
- **$E9CD**: save next/previous line pointer high byte
- **$E9CF**: calculate pointers to screen lines colour RAM
- **$E9D2**: set the column count
- **$E9D4**: get character from next/previous screen line
- **$E9D6**: save character to current screen line
- **$E9D8**: get colour from next/previous screen line colour RAM
- **$E9DA**: save colour to current screen line colour RAM
- **$E9DC**: decrement column index/count
- **$E9DD**: loop if more to do

### Commodore-64-intern-Buch (Commodore)
- **$E9C8**: Bildschirmzeiger
- **$E9CA**: für neue Zeile
- **$E9CD**: berechnen
- **$E9CF**: Zeiger für neue Zeile berechnen
- **$E9D2**: 39 Zeichen
- **$E9D4**: alle
- **$E9D6**: Zeichen
- **$E9D8**: und
- **$E9DA**: Farbe übertragen
- **$E9DC**: nächstes Zeichen
- **$E9DD**: schon alle ?
- **$E9DF**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E9CA**: HIBASE, top of screen page
- **$E9CD**: store >SAL, screen scroll pointer
- **$E9CF**: synchronise colour transfer
- **$E9D2**: offset for character on screen line
- **$E9D4**: move screen character
- **$E9D8**: move character colour
- **$E9DC**: next character
- **$E9DD**: till all 40 are done

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*