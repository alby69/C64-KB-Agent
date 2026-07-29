---
title: constants and series for SIN/COS(n)
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
- e2e0-konstanten-fr-sin-und-cos
- e2e5-2-pi
- e2ea-025
- e2ef-polynomial-table
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E2E0
  address_end: $E309
  symbol: constants-and-series-for-sincosn
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E2E0**: 1.570796371, pi/2, as floating number'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E2E0**: 1.57079633   Pi/2'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E2E0**: ; 1.570796327 (pi/2)'
---

# $E2E0 — constants and series for SIN/COS(n)

## Disassemblatura
```assembly
.E2E0  81 49 0F DA A2   ; 1.570796371, pi/2, as floating number
.E2E5  83 49 0F DA A2   ; 6.28319, 2*pi, as floating number
.E2EA  7F 00 00 00 00   ; 0.25
.E2EF  05   ; series counter
.E2F0  84 E6 1A 2D 1B   ; -14.3813907
.E2F5  86 28 07 FB F8   ; 42.0077971
.E2FA  87 99 68 89 01   ; -76.7041703
.E2FF  87 23 35 DF E1   ; 81.6052237
.E304  86 A5 5D E7 28   ; -41.3147021
.E309  83 49 0F DA A2   ; 6.28318531   2*pi
```


## Commenti

### Original Disassembly (—)
- **$E2E0**: 1.570796371, pi/2, as floating number
- **$E2E5**: 6.28319, 2*pi, as floating number
- **$E2EA**: 0.25
- **$E2EF**: series counter
- **$E2F0**: -14.3813907
- **$E2F5**: 42.0077971
- **$E2FA**: -76.7041703
- **$E2FF**: 81.6052237
- **$E304**: -41.3147021
- **$E309**: 6.28318531   2*pi

### Commodore-64-intern-Buch (Commodore)
- **$E2E0**: 1.57079633   Pi/2
- **$E2E5**: 6.28318531   2*Pi
- **$E2EA**: .25
- **$E2EF**: 5 = Polynomgrad, 6 Koeffizienten
- **$E2F0**: -14.3813907
- **$E2F5**: 42.0077971
- **$E2FA**: -76.7041703
- **$E2FF**: 81.6052237
- **$E304**: -41.3147021
- **$E309**: 6.28318531   2*Pi

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E2E0**: ; 1.570796327 (pi/2)
- **$E2E5**: ; 6.28318531  (pi*2)
- **$E2EA**: ; 0.25
- **$E2EF**: ; 5 (one byte counter for SIN series)
- **$E2F0**: ; -14.3813907 (SIN constant 1)
- **$E2F5**: ; 42.0077971  (SIN constant 2)
- **$E2FA**: ; -76.7041703 (SIN constant 3)
- **$E2FF**: ; 81.6052237  (SIN constant 4)
- **$E304**: ; -41.3417021 (SIN constant 5)
- **$E309**: ; 6.28318531  (SIN constant 6, pi*2)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*