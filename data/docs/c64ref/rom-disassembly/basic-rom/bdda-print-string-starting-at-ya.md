---
title: PRINT STRING STARTING AT Y,A
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
- aa2c-string
- ab45-print
- bdda-print-string-starting-at-ya
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BDDA
  address_end: $BDDA
  symbol: print-string-starting-at-ya
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BDDA**: PRINT STRING AT A,Y'
---

# $BDDA — PRINT STRING STARTING AT Y,A

## Disassemblatura
```assembly
.BDDA  4C 1E AB JMP $AB1E   ; PRINT STRING AT A,Y
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BDDA**: PRINT STRING AT A,Y

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*