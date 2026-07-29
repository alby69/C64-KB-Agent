---
title: EVALUATE ",EXPRESSION"
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
- b7f1-evaluate-expression
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $B7F1
  address_end: $B7F4
  symbol: evaluate-expression
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B7F1**: MUST HAVE COMMA FIRST'
---

# $B7F1 — EVALUATE ",EXPRESSION"

## Disassemblatura
```assembly
.B7F1  20 FD AE JSR $AEFD   ; MUST HAVE COMMA FIRST
.B7F4  4C 9E B7 JMP $B79E   ; CONVERT EXPRESSION TO BYTE IN X-REG
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B7F1**: MUST HAVE COMMA FIRST
- **$B7F4**: CONVERT EXPRESSION TO BYTE IN X-REG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*