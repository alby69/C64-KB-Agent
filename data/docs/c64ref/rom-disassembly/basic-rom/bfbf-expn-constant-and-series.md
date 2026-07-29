---
title: exp(n) constant and series
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bfbf-konstanten-fr-exp
- bfc4-exp-polynomial-table
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BFBF
  address_end: $BFE8
  symbol: expn-constant-and-series
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BFBF**: 1.44269504 = 1/LOG(2)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BFBF**: 1.44269504 = 1/LOG(2)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $BFBF — exp(n) constant and series

## Disassemblatura
```assembly
.BFBF  81 38 AA 3B 29   ; 1.44269504 = 1/LOG(2)
.BFC4  07   ; series count
.BFC5  71 34 58 3E 56   ; 2.14987637E-5
.BFCA  74 16 7E B3 1B   ; 1.43523140E-4
.BFCF  77 2F EE E3 85   ; 1.34226348E-3
.BFD4  7A 1D 84 1C 2A   ; 9.61401701E-3
.BFD9  7C 63 59 58 0A   ; 5.55051269E-2
.BFDE  7E 75 FD E7 C6   ; 2.40226385E-1
.BFE3  80 31 72 18 10   ; 6.93147186E-1
.BFE8  81 00 00 00 00   ; 1.00000000
```


## Commenti

### Original Disassembly (—)
- **$BFBF**: 1.44269504 = 1/LOG(2)
- **$BFC4**: series count
- **$BFC5**: 2.14987637E-5
- **$BFCA**: 1.43523140E-4
- **$BFCF**: 1.34226348E-3
- **$BFD4**: 9.61401701E-3
- **$BFD9**: 5.55051269E-2
- **$BFDE**: 2.40226385E-1
- **$BFE3**: 6.93147186E-1
- **$BFE8**: 1.00000000

### Commodore-64-intern-Buch (Commodore)
- **$BFBF**: 1.44269504 = 1/LOG(2)
- **$BFC4**: 7 = Polynomgrad, 8 Koeffizienten
- **$BFC5**: 2.14987637E-5
- **$BFCA**: 1.4352314E-4
- **$BFCF**: 1.34226348E-3
- **$BFD4**: 9.614011701E-3
- **$BFD9**: .0555051269
- **$BFDE**: .240226385
- **$BFE3**: .693147186
- **$BFE8**: 1

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*