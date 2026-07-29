---
title: routine for printing TAB( and SPC(
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
  address: $AAE8
  address_end: $AB1C
  symbol: routine-for-printing-tab-and-spc
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AB02**: )'
---

# $AAE8 — routine for printing TAB( and SPC(

## Disassemblatura
```assembly
.AAE8  38       SEC
.AAE9  20 F0 FF JSR $FFF0
.AAEC  98       TYA
.AAED  38       SEC
.AAEE  E9 0A    SBC #$0A
.AAF0  B0 FC    BCS $AAEE
.AAF2  49 FF    EOR #$FF
.AAF4  69 01    ADC #$01
.AAF6  D0 16    BNE $AB0E
.AAF8  08       PHP
.AAF9  38       SEC
.AAFA  20 F0 FF JSR $FFF0
.AAFD  84 09    STY $09
.AAFF  20 9B B7 JSR $B79B
.AB02  C9 29    CMP #$29   ; )
.AB04  D0 59    BNE $AB5F
.AB06  28       PLP
.AB07  90 06    BCC $AB0F
.AB09  8A       TXA
.AB0A  E5 09    SBC $09
.AB0C  90 05    BCC $AB13
.AB0E  AA       TAX
.AB0F  E8       INX
.AB10  CA       DEX
.AB11  D0 06    BNE $AB19
.AB13  20 73 00 JSR $0073
.AB16  4C A2 AA JMP $AAA2
.AB19  20 3B AB JSR $AB3B
.AB1C  D0 F2    BNE $AB10
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$AB02**: )

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*