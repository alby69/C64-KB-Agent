---
title: kernel I/O messages
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
- f0bd-systemmeldungen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F0BD
  address_end: $F127
  symbol: kernel-io-messages
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F0BD**: I/O ERROR #'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F0BD**: I/O ERROR #'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$F0BD**: I/O error'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F0BD**: I/O error'
---

# $F0BD — kernel I/O messages

## Disassemblatura
```assembly
.F0BD  0D 49 2F 4F 20 45 52 52   ; I/O ERROR #
.F0C5  4F 52 20 A3
.F0C9  0D 53 45 41 52 43 48 49   ; SEARCHING
.F0D1  4E 47 A0
.F0D4  46 4F 52 A0   ; FOR
.F0D8  0D 50 52 45 53 53 20 50   ; PRESS PLAY ON TAPE
.F0E0  4C 41 59 20 4F 4E 20 54
.F0E8  41 50 C5
.F0EB  50 52 45 53 53 20 52 45   ; PRESS RECORD & PLAY ON TAPE
.F0F3  43 4F 52 44 20 26 20 50
.F0FB  4C 41 59 20 4F 4E 20 54
.F103  41 50 C5
.F106  0D 4C 4F 41 44 49 4E C7   ; LOADING
.F10E  0D 53 41 56 49 4E 47 A0   ; SAVING
.F116  0D 56 45 52 49 46 59 49   ; VERIFYING
.F11E  4E C7
.F120  0D 46 4F 55 4E 44 A0   ; FOUND
.F127  0D 4F 4B 8D   ; OK
```


## Commenti

### Original Disassembly (—)
- **$F0BD**: I/O ERROR #
- **$F0C9**: SEARCHING
- **$F0D4**: FOR
- **$F0D8**: PRESS PLAY ON TAPE
- **$F0EB**: PRESS RECORD & PLAY ON TAPE
- **$F106**: LOADING
- **$F10E**: SAVING
- **$F116**: VERIFYING
- **$F120**: FOUND
- **$F127**: OK

### Commodore-64-intern-Buch (Commodore)
- **$F0BD**: I/O ERROR #
- **$F0C9**: SEARCHING
- **$F0D4**: FOR
- **$F0D8**: PRESS PLAY ON TAPE
- **$F0EB**: PRESS RECORD & PLAY ON TAPE
- **$F106**: LOADING
- **$F10E**: SAVING
- **$F116**: VERIFYING
- **$F120**: FOUND
- **$F127**: OK

### Marko Mäkelä (Marko Mäkelä)
- **$F0BD**: I/O error
- **$F0C9**: searching for
- **$F0D8**: press play on tape
- **$F0EB**: press record and play on tape
- **$F106**: loading
- **$F10E**: saving
- **$F116**: verifying
- **$F120**: found
- **$F127**: ok

### Magnus Nyman (Magnus Nyman)
- **$F0BD**: I/O error
- **$F0C9**: searching for
- **$F0D8**: press play on tape
- **$F0EB**: press record and play on tape
- **$F106**: loading
- **$F10E**: saving
- **$F116**: verifying
- **$F120**: found
- **$F127**: ok

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*