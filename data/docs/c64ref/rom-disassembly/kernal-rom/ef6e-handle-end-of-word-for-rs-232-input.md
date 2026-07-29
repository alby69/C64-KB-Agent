---
title: handle end of word for RS-232 input
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
  address: $EF6E
  address_end: $EF7C
  symbol: handle-end-of-word-for-rs-232-input
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $EF6E — handle end of word for RS-232 input

## Disassemblatura
```assembly
.EF6E  C6 A8    DEC $A8
.EF70  A5 A7    LDA $A7
.EF72  F0 67    BEQ $EFDB
.EF74  AD 93 02 LDA $0293
.EF77  0A       ASL
.EF78  A9 01    LDA #$01
.EF7A  65 A8    ADC $A8
.EF7C  D0 EF    BNE $EF6D
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*