---
title: do ABS and normalise FAC1
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
- b8d2-normalize-value-in-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B8D2
  address_end: $B8D4
  symbol: do-abs-and-normalise-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B8D2**: branch if number is +ve'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B8D7**: SHIFT UP SIGNIF DIGIT'
---

# $B8D2 — do ABS and normalise FAC1

## Disassemblatura
```assembly
.B8D2  B0 03    BCS $B8D7   ; branch if number is +ve
.B8D4  20 47 B9 JSR $B947   ; negate FAC1
```


## Commenti

### Original Disassembly (—)
- **$B8D2**: branch if number is +ve
- **$B8D4**: negate FAC1

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B8D7**: SHIFT UP SIGNIF DIGIT
- **$B8D9**: START A=0, COUNT SHIFTS IN A-REG
- **$B8DB**: LOOK AT MOST SIGNIFICANT BYTE
- **$B8DD**: SOME 1-BITS HERE
- **$B8DF**: HI-BYTE OF MANTISSA STILL ZERO,
- **$B8E1**: SO DO A FAST 8-BIT SHUFFLE
- **$B8EF**: ZERO EXTENSION BYTE
- **$B8F1**: BUMP SHIFT COUNT
- **$B8F3**: DONE 4 TIMES YET?
- **$B8F5**: NO, STILL MIGHT BE SOME 1'S YES, VALUE OF FAC IS ZERO

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*