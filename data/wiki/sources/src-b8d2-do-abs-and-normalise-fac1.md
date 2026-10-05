---
id: src-b8d2-do-abs-and-normalise-fac1
type: source
title: 'Source Summary: do ABS and normalise FAC1'
aliases:
- do ABS and normalise FAC1
- b8d2-do-abs-and-normalise-fac1.md
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
links_out: []
---

# Source Summary: do ABS and normalise FAC1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b8d2-do-abs-and-normalise-fac1.md`
**SHA256**: `f54fa03103deb879ee6392b9ddce6c5c303257d75f508a7453f8e5f2270f6f55`

## Summary



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
- **$B8DF**: HI-BYTE OF...
