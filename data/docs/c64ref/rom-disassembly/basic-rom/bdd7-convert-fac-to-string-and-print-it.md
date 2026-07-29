---
title: CONVERT (FAC) TO STRING, AND PRINT IT
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
- bc5b-fac
- bdd7-convert-fac-to-string-and-print-it
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BDD7
  address_end: $BDD7
  symbol: convert-fac-to-string-and-print-it
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BDD7**: CONVERT (FAC) TO STRING AT STACK'
---

# $BDD7 — CONVERT (FAC) TO STRING, AND PRINT IT

## Disassemblatura
```assembly
.BDD7  20 DF BD JSR $BDDF   ; CONVERT (FAC) TO STRING AT STACK
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BDD7**: CONVERT (FAC) TO STRING AT STACK

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*