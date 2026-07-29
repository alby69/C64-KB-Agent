---
title: save ram to cassette
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
  address: $F65F
  address_end: $F68E
  symbol: save-ram-to-cassette
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F65F — save ram to cassette

## Disassemblatura
```assembly
.F65F  20 D0 F7 JSR $F7D0
.F662  90 8D    BCC $F5F1
.F664  20 38 F8 JSR $F838
.F667  B0 25    BCS $F68E
.F669  20 8F F6 JSR $F68F
.F66C  A2 03    LDX #$03
.F66E  A5 B9    LDA $B9
.F670  29 01    AND #$01
.F672  D0 02    BNE $F676
.F674  A2 01    LDX #$01
.F676  8A       TXA
.F677  20 6A F7 JSR $F76A
.F67A  B0 12    BCS $F68E
.F67C  20 67 F8 JSR $F867
.F67F  B0 0D    BCS $F68E
.F681  A5 B9    LDA $B9
.F683  29 02    AND #$02
.F685  F0 06    BEQ $F68D
.F687  A9 05    LDA #$05
.F689  20 6A F7 JSR $F76A
.F68C  24       .BYTE $24
.F68D  18       CLC
.F68E  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*