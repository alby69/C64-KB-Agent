---
title: COPY RESULT INTO FAC MANTISSA, AND NORMALIZE
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
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BB8F
  address_end: $BB9F
  symbol: copy-result-into-fac-mantissa-and-normalize
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $BB8F — COPY RESULT INTO FAC MANTISSA, AND NORMALIZE

## Disassemblatura
```assembly
.BB8F  A5 26    LDA $26
.BB91  85 62    STA $62
.BB93  A5 27    LDA $27
.BB95  85 63    STA $63
.BB97  A5 28    LDA $28
.BB99  85 64    STA $64
.BB9B  A5 29    LDA $29
.BB9D  85 65    STA $65
.BB9F  4C D7 B8 JMP $B8D7
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*