---
title: open cassette for input
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
  address: $F3B8
  address_end: $F3D4
  symbol: open-cassette-for-input
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F3B8 — open cassette for input

## Disassemblatura
```assembly
.F3B8  20 38 F8 JSR $F838
.F3BB  B0 17    BCS $F3D4
.F3BD  A9 04    LDA #$04
.F3BF  20 6A F7 JSR $F76A
.F3C2  A9 BF    LDA #$BF
.F3C4  A4 B9    LDY $B9
.F3C6  C0 60    CPY #$60
.F3C8  F0 07    BEQ $F3D1
.F3CA  A0 00    LDY #$00
.F3CC  A9 02    LDA #$02
.F3CE  91 B2    STA ($B2),Y
.F3D0  98       TYA
.F3D1  85 A6    STA $A6
.F3D3  18       CLC
.F3D4  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*