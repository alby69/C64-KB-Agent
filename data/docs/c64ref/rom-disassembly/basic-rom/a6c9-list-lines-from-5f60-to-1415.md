---
title: list lines from $5F/$60 to $14/$15
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
  address: $A6C9
  address_end: $A714
  symbol: list-lines-from-5f60-to-1415
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $A6C9 — list lines from $5F/$60 to $14/$15

## Disassemblatura
```assembly
.A6C9  A0 01    LDY #$01
.A6CB  84 0F    STY $0F
.A6CD  B1 5F    LDA ($5F),Y
.A6CF  F0 43    BEQ $A714
.A6D1  20 2C A8 JSR $A82C
.A6D4  20 D7 AA JSR $AAD7
.A6D7  C8       INY
.A6D8  B1 5F    LDA ($5F),Y
.A6DA  AA       TAX
.A6DB  C8       INY
.A6DC  B1 5F    LDA ($5F),Y
.A6DE  C5 15    CMP $15
.A6E0  D0 04    BNE $A6E6
.A6E2  E4 14    CPX $14
.A6E4  F0 02    BEQ $A6E8
.A6E6  B0 2C    BCS $A714
.A6E8  84 49    STY $49
.A6EA  20 CD BD JSR $BDCD
.A6ED  A9 20    LDA #$20
.A6EF  A4 49    LDY $49
.A6F1  29 7F    AND #$7F
.A6F3  20 47 AB JSR $AB47
.A6F6  C9 22    CMP #$22
.A6F8  D0 06    BNE $A700
.A6FA  A5 0F    LDA $0F
.A6FC  49 FF    EOR #$FF
.A6FE  85 0F    STA $0F
.A700  C8       INY
.A701  F0 11    BEQ $A714
.A703  B1 5F    LDA ($5F),Y
.A705  D0 10    BNE $A717
.A707  A8       TAY
.A708  B1 5F    LDA ($5F),Y
.A70A  AA       TAX
.A70B  C8       INY
.A70C  B1 5F    LDA ($5F),Y
.A70E  86 5F    STX $5F
.A710  85 60    STA $60
.A712  D0 B5    BNE $A6C9
.A714  4C 86 E3 JMP $E386
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*