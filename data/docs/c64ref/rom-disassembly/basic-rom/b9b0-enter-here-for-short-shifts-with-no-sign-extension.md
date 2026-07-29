---
title: ENTER HERE FOR SHORT SHIFTS WITH NO SIGN EXTENSION
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00a5-count
- b9c1-log-polynomial-table
- b9d6-05-sqr2
- b9db-sqr2
- b9e0-05
- b9e5-log2
- clear
- return
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $B9B0
  address_end: $B9E5
  symbol: enter-here-for-short-shifts-with-no-sign-extension
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B9B6**: EXTENSION'
---

# $B9B0 — ENTER HERE FOR SHORT SHIFTS WITH NO SIGN EXTENSION

## Disassemblatura
```assembly
.B9B0  76 02    ROR $02,X
.B9B2  76 03    ROR $03,X
.B9B4  76 04    ROR $04,X
.B9B6  6A       ROR   ; EXTENSION
.B9B7  C8       INY   ; COUNT THE SHIFT
.B9B8  D0 EC    BNE $B9A6
.B9BA  18       CLC   ; RETURN WITH CARRY CLEAR
.B9BB  60       RTS
.B9BC  81 00 00 00 00
.B9C1  03   ; # OF COEFFICIENTS - 1
.B9C2  7F 5E 56 CB 79   ; X^7 +
.B9C7  80 13 9B 0B 64   ; X^5 +
.B9CC  80 76 38 93 16   ; X^3 +
.B9D1  82 38 AA 3B 20   ; X
.B9D6  80 35 04 F3 34   ; SQR(1/2)
.B9DB  81 35 04 F3 34   ; SQR(TWO)
.B9E0  80 80 00 00 00   ; -1/2
.B9E5  80 31 72 17 F8   ; LOG(2)
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B9B6**: EXTENSION
- **$B9B7**: COUNT THE SHIFT
- **$B9BA**: RETURN WITH CARRY CLEAR
- **$B9C1**: # OF COEFFICIENTS - 1
- **$B9C2**: X^7 +
- **$B9C7**: X^5 +
- **$B9CC**: X^3 +
- **$B9D1**: X
- **$B9D6**: SQR(1/2)
- **$B9DB**: SQR(TWO)
- **$B9E0**: -1/2
- **$B9E5**: LOG(2)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*