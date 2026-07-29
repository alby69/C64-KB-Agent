---
title: POP RETURN ADDRESS AND SET FAC=0
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
- bc5b-fac
- return
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BADA
  address_end: $BADF
  symbol: pop-return-address-and-set-fac0
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $BADA — POP RETURN ADDRESS AND SET FAC=0

## Disassemblatura
```assembly
.BADA  68       PLA
.BADB  68       PLA
.BADC  4C F7 B8 JMP $B8F7
.BADF  4C 7E B9 JMP $B97E
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*