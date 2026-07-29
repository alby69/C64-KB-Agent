---
title: find file A
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f314-find-file-a
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $F314
  address_end: $F31E
  symbol: find-file-a
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F314**: get the open file count'
---

# $F314 — find file A

## Disassemblatura
```assembly
.F314  A6 98    LDX $98   ; get the open file count
.F316  CA       DEX   ; decrement the count to give the index
.F317  30 15    BMI $F32E   ; if no files just exit
.F319  DD 59 02 CMP $0259,X   ; compare the logical file number with the table logical file number
.F31C  D0 F8    BNE $F316   ; if no match go try again
.F31E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F314**: get the open file count
- **$F316**: decrement the count to give the index
- **$F317**: if no files just exit
- **$F319**: compare the logical file number with the table logical file number
- **$F31C**: if no match go try again

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*