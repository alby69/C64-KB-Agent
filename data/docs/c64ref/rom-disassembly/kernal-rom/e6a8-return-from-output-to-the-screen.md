---
title: return from output to the screen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $E6A8
  address_end: $E6B5
  symbol: return-from-output-to-the-screen
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $E6A8 — return from output to the screen

## Disassemblatura
```assembly
.E6A8  68       PLA
.E6A9  A8       TAY
.E6AA  A5 D8    LDA $D8
.E6AC  F0 02    BEQ $E6B0
.E6AE  46 D4    LSR $D4
.E6B0  68       PLA
.E6B1  AA       TAX
.E6B2  68       PLA
.E6B3  18       CLC
.E6B4  58       CLI
.E6B5  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*