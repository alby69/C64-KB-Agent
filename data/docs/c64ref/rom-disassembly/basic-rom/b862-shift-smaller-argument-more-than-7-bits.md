---
title: SHIFT SMALLER ARGUMENT MORE THAN 7 BITS
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
- 0068-bits
- b862-shift-smaller-argument-more-than-7-bits
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $B862
  address_end: $B865
  symbol: shift-smaller-argument-more-than-7-bits
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B862**: ALIGN RADIX BY SHIFTING'
---

# $B862 — SHIFT SMALLER ARGUMENT MORE THAN 7 BITS

## Disassemblatura
```assembly
.B862  20 99 B9 JSR $B999   ; ALIGN RADIX BY SHIFTING
.B865  90 3C    BCC $B8A3   ; ...ALWAYS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B862**: ALIGN RADIX BY SHIFTING
- **$B865**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*