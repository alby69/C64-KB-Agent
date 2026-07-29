---
title: GET operand
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  address: $AEE3
  address_end: $AEF4
  symbol: get-operand
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AEEA**: SGN code or higher'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $AEE3 — GET operand

## Disassemblatura
```assembly
.AEE3  C9 A5    CMP #$A5
.AEE5  D0 03    BNE $AEEA
.AEE7  4C F4 B3 JMP $B3F4
.AEEA  C9 B4    CMP #$B4   ; SGN code or higher
.AEEC  90 03    BCC $AEF1
.AEEE  4C A7 AF JMP $AFA7
.AEF1  20 FA AE JSR $AEFA
.AEF4  20 9E AD JSR $AD9E
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$AEEA**: SGN code or higher

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*