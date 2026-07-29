---
title: remove GOSUB block from stack
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
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
  - marko_mäkelä.txt
  address: $A8EB
  address_end: $A8F6
  symbol: remove-gosub-block-from-stack
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $A8EB — remove GOSUB block from stack

## Disassemblatura
```assembly
.A8EB  68       PLA
.A8EC  68       PLA
.A8ED  85 39    STA $39
.A8EF  68       PLA
.A8F0  85 3A    STA $3A
.A8F2  68       PLA
.A8F3  85 7A    STA $7A
.A8F5  68       PLA
.A8F6  85 7B    STA $7B
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*