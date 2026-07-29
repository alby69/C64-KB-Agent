---
title: assign to TI$
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
  address: $A9E0
  address_end: $AA1A
  symbol: assign-to-ti
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A9E3**: length 6'
---

# $A9E0 — assign to TI$

## Disassemblatura
```assembly
.A9E0  20 A6 B6 JSR $B6A6
.A9E3  C9 06    CMP #$06   ; length 6
.A9E5  D0 3D    BNE $AA24
.A9E7  A0 00    LDY #$00
.A9E9  84 61    STY $61
.A9EB  84 66    STY $66
.A9ED  84 71    STY $71
.A9EF  20 1D AA JSR $AA1D
.A9F2  20 E2 BA JSR $BAE2
.A9F5  E6 71    INC $71
.A9F7  A4 71    LDY $71
.A9F9  20 1D AA JSR $AA1D
.A9FC  20 0C BC JSR $BC0C
.A9FF  AA       TAX
.AA00  F0 05    BEQ $AA07
.AA02  E8       INX
.AA03  8A       TXA
.AA04  20 ED BA JSR $BAED
.AA07  A4 71    LDY $71
.AA09  C8       INY
.AA0A  C0 06    CPY #$06
.AA0C  D0 DF    BNE $A9ED
.AA0E  20 E2 BA JSR $BAE2
.AA11  20 9B BC JSR $BC9B
.AA14  A6 64    LDX $64
.AA16  A4 63    LDY $63
.AA18  A5 65    LDA $65
.AA1A  4C DB FF JMP $FFDB
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$A9E3**: length 6

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*