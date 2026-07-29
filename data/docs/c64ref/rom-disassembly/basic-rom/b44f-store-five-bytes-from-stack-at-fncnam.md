---
title: STORE FIVE BYTES FROM STACK AT (FNCNAM)
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
- store
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $B44F
  address_end: $B464
  symbol: store-five-bytes-from-stack-at-fncnam
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B44F — STORE FIVE BYTES FROM STACK AT (FNCNAM)

## Disassemblatura
```assembly
.B44F  A0 00    LDY #$00
.B451  68       PLA
.B452  91 4E    STA ($4E),Y
.B454  68       PLA
.B455  C8       INY
.B456  91 4E    STA ($4E),Y
.B458  68       PLA
.B459  C8       INY
.B45A  91 4E    STA ($4E),Y
.B45C  68       PLA
.B45D  C8       INY
.B45E  91 4E    STA ($4E),Y
.B460  68       PLA
.B461  C8       INY
.B462  91 4E    STA ($4E),Y
.B464  60       RTS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*