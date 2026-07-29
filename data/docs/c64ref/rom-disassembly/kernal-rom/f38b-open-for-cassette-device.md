---
title: open for cassette device
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
  address: $F38B
  address_end: $F3B6
  symbol: open-for-cassette-device
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F38B — open for cassette device

## Disassemblatura
```assembly
.F38B  20 D0 F7 JSR $F7D0
.F38E  B0 03    BCS $F393
.F390  4C 13 F7 JMP $F713
.F393  A5 B9    LDA $B9
.F395  29 0F    AND #$0F
.F397  D0 1F    BNE $F3B8
.F399  20 17 F8 JSR $F817
.F39C  B0 36    BCS $F3D4
.F39E  20 AF F5 JSR $F5AF
.F3A1  A5 B7    LDA $B7
.F3A3  F0 0A    BEQ $F3AF
.F3A5  20 EA F7 JSR $F7EA
.F3A8  90 18    BCC $F3C2
.F3AA  F0 28    BEQ $F3D4
.F3AC  4C 04 F7 JMP $F704
.F3AF  20 2C F7 JSR $F72C
.F3B2  F0 20    BEQ $F3D4
.F3B4  90 0C    BCC $F3C2
.F3B6  B0 F4    BCS $F3AC
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*