---
id: bfbf-expn-constant-and-series
type: entity
title: exp(n) constant and series
aliases:
- exp(n) constant and series
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bfbf-expn-constant-and-series.md
  sha256: f6b9115d0cd04f12298d2a075d40c08a642f5d8d4a5d978ac4d938400d092c22
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bfbf-expn-constant-and-series
---

# exp(n) constant and series



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

## References
- Source: [[src-bfbf-expn-constant-and-series]]
