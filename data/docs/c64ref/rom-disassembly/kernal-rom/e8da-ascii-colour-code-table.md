---
title: ASCII colour code table
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
- e8da-tabelle-der-farb-kodes
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E8DA
  address_end: $E8E9
  symbol: ascii-colour-code-table
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E8DA**: 144    black'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Nessun commento disponibile.
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E8DA**: color0, black'
---

# $E8DA — ASCII colour code table

## Disassemblatura
```assembly
.E8DA  90   ; 144    black
.E8DB  05   ; 5    white
.E8DC  1C   ; 28    red
.E8DD  9F   ; 159    cyan
.E8DE  9C   ; 156    purple
.E8DF  1E   ; 30    green
.E8E0  1F   ; 31    blue
.E8E1  9E   ; 158    yellow
.E8E2  81   ; 129    orange
.E8E3  95   ; 149    brown
.E8E4  96   ; 150    light red
.E8E5  97   ; 151    dark grey
.E8E6  98   ; 152    medium grey
.E8E7  99   ; 153    light green
.E8E8  9A   ; 154    light blue
.E8E9  9B   ; 155    light grey
```


## Commenti

### Original Disassembly (—)
- **$E8DA**: 144    black
- **$E8DB**: 5    white
- **$E8DC**: 28    red
- **$E8DD**: 159    cyan
- **$E8DE**: 156    purple
- **$E8DF**: 30    green
- **$E8E0**: 31    blue
- **$E8E1**: 158    yellow
- **$E8E2**: 129    orange
- **$E8E3**: 149    brown
- **$E8E4**: 150    light red
- **$E8E5**: 151    dark grey
- **$E8E6**: 152    medium grey
- **$E8E7**: 153    light green
- **$E8E8**: 154    light blue
- **$E8E9**: 155    light grey

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E8DA**: color0, black
- **$E8DB**: color1, white
- **$E8DC**: color2, red
- **$E8DD**: color3, cyan
- **$E8DE**: color4, purple
- **$E8DF**: color5, green
- **$E8E0**: color6, blue
- **$E8E1**: color7, yellow
- **$E8E2**: color8, orange
- **$E8E3**: color9, brown
- **$E8E4**: colorA, pink
- **$E8E5**: colorB, grey1
- **$E8E6**: colorC, grey2
- **$E8E7**: colorD, light green
- **$E8E8**: colorE, light blue
- **$E8E9**: colorF, grey3

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*