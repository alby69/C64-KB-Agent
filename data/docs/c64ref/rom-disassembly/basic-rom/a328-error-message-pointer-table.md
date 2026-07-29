---
title: error message pointer table
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A328
  address_end: $A360
  symbol: error-message-pointer-table
  sources:
  - name: Original Disassembly
    author: —
    description: Nessun commento disponibile.
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Nessun commento disponibile.
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A328**: 01 too many files'
---

# $A328 — error message pointer table

## Disassemblatura
```assembly
.A328  9E A1 AC A1 B5 A1 C2 A1
.A330  D0 A1 E2 A1 F0 A1 FF A1
.A338  10 A2 25 A2 35 A2 3B A2
.A340  4F A2 5A A2 6A A2 72 A2
.A348  7F A2 90 A2 9D A2 AA A2
.A350  BA A2 C8 A2 D5 A2 E4 A2
.A358  ED A2 00 A3 0E A3 1E A3
.A360  24 A3 83 A3
```


## Commenti

### Original Disassembly (—)
Nessun commento disponibile.

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
- **$A328**: 01 too many files
- **$A32A**: 02 file open
- **$A32C**: 03 file not open
- **$A32E**: 04 file not found
- **$A330**: 05 device not present
- **$A332**: 06 not input file
- **$A334**: 07 not output file
- **$A336**: 08 missing file name
- **$A338**: 09 illegal device number
- **$A33A**: 0A next without for
- **$A33C**: 0B syntax
- **$A33E**: 0C return without gosub
- **$A340**: 0D out of data
- **$A342**: 0E illegal quantity
- **$A344**: 0F overflow
- **$A346**: 10 out of memory
- **$A348**: 11 undef'd statement
- **$A34A**: 12 bad subscript
- **$A34C**: 13 redim'd array
- **$A34E**: 14 division by zero
- **$A350**: 15 illegal direct
- **$A352**: 16 type mismatch
- **$A354**: 17 string too long
- **$A356**: 18 file data
- **$A358**: 19 formula too complex
- **$A35A**: 1A can't continue
- **$A35C**: 1B undef'd function
- **$A35E**: 1C verify
- **$A360**: 1D load
- **$A362**: 1E break

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*