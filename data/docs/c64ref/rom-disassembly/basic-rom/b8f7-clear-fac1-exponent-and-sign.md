---
title: clear FAC1 exponent and sign
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
- b8f7-set-fac-0
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B8F7
  address_end: $B8F9
  symbol: clear-fac1-exponent-and-sign
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B8F7**: clear A'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B8F7 — clear FAC1 exponent and sign

## Disassemblatura
```assembly
.B8F7  A9 00    LDA #$00   ; clear A
.B8F9  85 61    STA $61   ; set FAC1 exponent
```


## Commenti

### Original Disassembly (—)
- **$B8F7**: clear A
- **$B8F9**: set FAC1 exponent

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*