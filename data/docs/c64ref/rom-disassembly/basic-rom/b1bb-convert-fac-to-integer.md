---
title: CONVERT FAC TO INTEGER
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
- b1bb-convert-fac-to-integer
- bc5b-fac
- bc9b-integer
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $B1BB
  address_end: $B1BD
  symbol: convert-fac-to-integer
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B1BB**: ERROR IF -'
---

# $B1BB — CONVERT FAC TO INTEGER

## Disassemblatura
```assembly
.B1BB  A5 66    LDA $66   ; ERROR IF -
.B1BD  30 0D    BMI $B1CC
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B1BB**: ERROR IF -

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*