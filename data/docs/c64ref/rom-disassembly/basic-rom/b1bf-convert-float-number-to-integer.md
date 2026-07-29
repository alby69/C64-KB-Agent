---
title: convert float number to integer
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
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
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  address: $B1BF
  address_end: $B1CE
  symbol: convert-float-number-to-integer
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B1C5**: low  B1A5'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B1BF**: EXPONENT OF VALUE IN FAC'
---

# $B1BF — convert float number to integer

## Disassemblatura
```assembly
.B1BF  A5 61    LDA $61
.B1C1  C9 90    CMP #$90
.B1C3  90 09    BCC $B1CE
.B1C5  A9 A5    LDA #$A5   ; low  B1A5
.B1C7  A0 B1    LDY #$B1   ; high B1A5
.B1C9  20 5B BC JSR $BC5B
.B1CC  D0 7A    BNE $B248
.B1CE  4C 9B BC JMP $BC9B
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$B1C5**: low  B1A5
- **$B1C7**: high B1A5

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B1BF**: EXPONENT OF VALUE IN FAC
- **$B1C1**: ABS(VALUE) < 32768?
- **$B1C3**: YES, OK FOR INTEGER
- **$B1C5**: NO; NEXT FEW LINES ARE SUPPOSED TO
- **$B1C7**: ALLOW -32768 ($8000)
- **$B1CC**: ILLEGAL QUANTITY
- **$B1CE**: CONVERT TO INTEGER

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*