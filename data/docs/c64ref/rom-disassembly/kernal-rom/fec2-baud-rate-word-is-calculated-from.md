---
title: baud rate word is calculated from ..
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
- fec2-ntsc-version
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FEC2
  address_end: $FED4
  symbol: baud-rate-word-is-calculated-from
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FEC2**: 50   baud   1027700'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FEC2**: $27C1 = 10177       50 Baud'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FEC2**: 50'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FEC2**: 50 baud'
---

# $FEC2 — baud rate word is calculated from ..

## Disassemblatura
```assembly
.FEC2  C1 27   ; 50   baud   1027700
.FEC4  3E 1A   ; 75   baud   1022700
.FEC6  C5 11   ; 110   baud   1022780
.FEC8  74 0E   ; 134.5 baud   1022200
.FECA  ED 0C   ; 150   baud   1022700
.FECC  45 06   ; 300   baud   1023000
.FECE  F0 02   ; 600   baud   1022400
.FED0  46 01   ; 1200   baud   1022400
.FED2  B8 00   ; 1800   baud   1022400
.FED4  71 00   ; 2400   baud   1022400
```


## Commenti

### Original Disassembly (—)
- **$FEC2**: 50   baud   1027700
- **$FEC4**: 75   baud   1022700
- **$FEC6**: 110   baud   1022780
- **$FEC8**: 134.5 baud   1022200
- **$FECA**: 150   baud   1022700
- **$FECC**: 300   baud   1023000
- **$FECE**: 600   baud   1022400
- **$FED0**: 1200   baud   1022400
- **$FED2**: 1800   baud   1022400
- **$FED4**: 2400   baud   1022400

### Commodore-64-intern-Buch (Commodore)
- **$FEC2**: $27C1 = 10177       50 Baud
- **$FEC4**: $1A3E =  6718       75 Baud
- **$FEC6**: $11C5 =  4549      110 Baud
- **$FEC8**: $0E74 =  3700      134.5 Baud
- **$FECA**: $0CED =  3309      150 Baud
- **$FECC**: $0645 =  1605      300 Baud
- **$FECE**: $02F0 =   752      600 Baud
- **$FED0**: $0146 =   326     1200 Baud
- **$FED2**: $00B8 =   184     1800 Baud
- **$FED4**: $0071 =   113     2400 Baud

### Marko Mäkelä (Marko Mäkelä)
- **$FEC2**: 50
- **$FEC4**: 75
- **$FEC6**: 110
- **$FEC8**: 134.5
- **$FECA**: 150
- **$FECC**: 300
- **$FECE**: 600
- **$FED0**: 1200
- **$FED2**: 1800
- **$FED4**: 2400

### Magnus Nyman (Magnus Nyman)
- **$FEC2**: 50 baud
- **$FEC4**: 75 baud
- **$FEC6**: 110 baud
- **$FEC8**: 134.5 baud
- **$FECA**: 150 baud
- **$FECC**: 300 baud
- **$FECE**: 600 baud
- **$FED0**: 1200 baud
- **$FED2**: (1800) 2400 baud
- **$FED4**: 2400 baud

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*