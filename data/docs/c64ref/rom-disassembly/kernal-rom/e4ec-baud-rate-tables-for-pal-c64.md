---
title: baud rate tables for PAL C64
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
- e4ec-baud-rate-pal-version
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E4EC
  address_end: $E4FE
  symbol: baud-rate-tables-for-pal-c64
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E4EC**: 50   baud   985300'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E4EC**: $2619 = 9753     50 Baud'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E4EC**: 50'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E4EC**: 50 baud'
---

# $E4EC — baud rate tables for PAL C64

## Disassemblatura
```assembly
.E4EC  19 26   ; 50   baud   985300
.E4EE  44 19   ; 75   baud   985200
.E4F0  1A 11   ; 110   baud   985160
.E4F2  E8 0D   ; 134.5 baud   984540
.E4F4  70 0C   ; 150   baud   985200
.E4F6  06 06   ; 300   baud   985200
.E4F8  D1 02   ; 600   baud   985200
.E4FA  37 01   ; 1200   baud   986400
.E4FC  AE 00   ; 1800   baud   986400
.E4FE  69 00   ; 2400   baud   984000
```


## Commenti

### Original Disassembly (—)
- **$E4EC**: 50   baud   985300
- **$E4EE**: 75   baud   985200
- **$E4F0**: 110   baud   985160
- **$E4F2**: 134.5 baud   984540
- **$E4F4**: 150   baud   985200
- **$E4F6**: 300   baud   985200
- **$E4F8**: 600   baud   985200
- **$E4FA**: 1200   baud   986400
- **$E4FC**: 1800   baud   986400
- **$E4FE**: 2400   baud   984000

### Commodore-64-intern-Buch (Commodore)
- **$E4EC**: $2619 = 9753     50 Baud
- **$E4EE**: $1944 = 6468     75 Baud
- **$E4F0**: $111A = 4378    110 Baud
- **$E4F2**: $0DE8 = 3560    134.5 Baud
- **$E4F4**: $0C70 = 3184    150 Baud
- **$E4F6**: $0606 = 1542    300 Baud
- **$E4F8**: $02D1 =  736    600 Baud
- **$E4FA**: $0137 =  311   1200 Baud
- **$E4FC**: $00AE =  174   1800 Baud
- **$E4FE**: $0069 =  105   2400 Baud

### Marko Mäkelä (Marko Mäkelä)
- **$E4EC**: 50
- **$E4EE**: 75
- **$E4F0**: 110
- **$E4F2**: 134.5
- **$E4F4**: 150
- **$E4F6**: 300
- **$E4F8**: 600
- **$E4FA**: 1200
- **$E4FC**: 1800
- **$E4FE**: 2400

### Magnus Nyman (Magnus Nyman)
- **$E4EC**: 50 baud
- **$E4EE**: 75 baud
- **$E4F0**: 110 baud
- **$E4F2**: 134.5 baud
- **$E4F4**: 150 baud
- **$E4F6**: 300 baud
- **$E4F8**: 600 baud
- **$E4FA**: 1200 baud
- **$E4FC**: (1800) 2400 baud
- **$E4FE**: 2400 baud

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*