---
title: FLOAT (Y) INTO FAC, GIVING VALUE 0-255
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
- b3a2-float-y-into-fac-giving-value-0-255
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $B3A2
  address_end: $B3A4
  symbol: float-y-into-fac-giving-value-0-255
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B3A2**: MSB = 0'
---

# $B3A2 — FLOAT (Y) INTO FAC, GIVING VALUE 0-255

## Disassemblatura
```assembly
.B3A2  A9 00    LDA #$00   ; MSB = 0
.B3A4  F0 EB    BEQ $B391   ; ...ALWAYS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B3A2**: MSB = 0
- **$B3A4**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*