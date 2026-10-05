---
id: b8d2-do-abs-and-normalise-fac1
type: entity
title: do ABS and normalise FAC1
aliases:
- do ABS and normalise FAC1
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b8d2-do-abs-and-normalise-fac1.md
  sha256: f54fa03103deb879ee6392b9ddce6c5c303257d75f508a7453f8e5f2270f6f55
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b8d2-do-abs-and-normalise-fac1
---

# do ABS and normalise FAC1



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

## References
- Source: [[src-b8d2-do-abs-and-normalise-fac1]]
