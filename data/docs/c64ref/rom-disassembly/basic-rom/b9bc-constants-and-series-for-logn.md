---
title: constants and series for LOG(n)
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
- b9bc-konstanten-fr-log
- b9c1-log-polynomial-table
- b9d6-05-sqr2
- b9db-sqr2
- b9e0-05
- b9e5-log2
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B9BC
  address_end: $B9E5
  symbol: constants-and-series-for-logn
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B9BC**: 1'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B9BC**: 1'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B9BC — constants and series for LOG(n)

## Disassemblatura
```assembly
.B9BC  81 00 00 00 00   ; 1
.B9C1  03   ; series counter
.B9C2  7F 5E 56 CB 79   ; .434255942
.B9C7  80 13 9B 0B 64   ; .576584541
.B9CC  80 76 38 93 16   ; .961800759
.B9D1  82 38 AA 3B 20   ; 2.88539007
.B9D6  80 35 04 F3 34   ; .707106781 = 1/SQR(2)
.B9DB  81 35 04 F3 34   ; 1.41421356 = SQR(2)
.B9E0  80 80 00 00 00   ; -.5
.B9E5  80 31 72 17 F8   ; .693147181  =  LOG(2)
```


## Commenti

### Original Disassembly (—)
- **$B9BC**: 1
- **$B9C1**: series counter
- **$B9C2**: .434255942
- **$B9C7**: .576584541
- **$B9CC**: .961800759
- **$B9D1**: 2.88539007
- **$B9D6**: .707106781 = 1/SQR(2)
- **$B9DB**: 1.41421356 = SQR(2)
- **$B9E0**: -.5
- **$B9E5**: .693147181  =  LOG(2)

### Commodore-64-intern-Buch (Commodore)
- **$B9BC**: 1
- **$B9C1**: 3 = Polynomgrad, dann 4 Koeffizienten
- **$B9C2**: .434255942
- **$B9C7**: .576584541
- **$B9CC**: .961800759
- **$B9D1**: 2.88539007
- **$B9D6**: .707106781 = 1/SQR(2)
- **$B9DB**: 1.41421356 = SQR(2)
- **$B9E0**: -.5
- **$B9E5**: .693147181  =  LOG(2)

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*