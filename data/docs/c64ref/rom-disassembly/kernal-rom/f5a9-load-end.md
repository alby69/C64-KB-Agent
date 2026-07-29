---
title: LOAD END
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ece7-load
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  address: $F5A9
  address_end: $F5AE
  symbol: load-end
  sources:
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

# $F5A9 — LOAD END

## Disassemblatura
```assembly
.F5A9  18       CLC
.F5AA  A6 AE    LDX $AE
.F5AC  A4 AF    LDY $AF
.F5AE  60       RTS
```


## Commenti

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*