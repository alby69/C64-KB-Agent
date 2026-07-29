---
title: if open quote toggle cursor quote flag
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
- e684-auf-hochkomma-testen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E684
  address_end: $E690
  symbol: if-open-quote-toggle-cursor-quote-flag
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E684**: comapre byte with "'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E684**: ''"'' ?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E684**: quote mark'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E684**: ASCII quotes (")'
---

# $E684 — if open quote toggle cursor quote flag

## Disassemblatura
```assembly
.E684  C9 22    CMP #$22   ; comapre byte with "
.E686  D0 08    BNE $E690   ; exit if not "
.E688  A5 D4    LDA $D4   ; get cursor quote flag, $xx = quote, $00 = no quote
.E68A  49 01    EOR #$01   ; toggle it
.E68C  85 D4    STA $D4   ; save cursor quote flag
.E68E  A9 22    LDA #$22   ; restore the "
.E690  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E684**: comapre byte with "
- **$E686**: exit if not "
- **$E688**: get cursor quote flag, $xx = quote, $00 = no quote
- **$E68A**: toggle it
- **$E68C**: save cursor quote flag
- **$E68E**: restore the "

### Commodore-64-intern-Buch (Commodore)
- **$E684**: '"' ?
- **$E686**: nein ?, dann fertig
- **$E688**: Hochkomma-
- **$E68A**: Flag
- **$E68C**: umdrehen
- **$E68E**: Hochkomma-Code wieder- herstellen
- **$E690**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E684**: quote mark
- **$E68E**: quote mark

### Magnus Nyman (Magnus Nyman)
- **$E684**: ASCII quotes (")
- **$E686**: nope, return
- **$E688**: QTSW, quotes mode flag
- **$E68A**: toggle on/off
- **$E68C**: store
- **$E68E**: restore (A) to #$22

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*