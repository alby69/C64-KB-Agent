---
title: get character from current screen line
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
  address: $E63A
  address_end: $E683
  symbol: get-character-from-current-screen-line
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E67C**: screen PI code'
---

# $E63A — get character from current screen line

## Disassemblatura
```assembly
.E63A  A4 D3    LDY $D3
.E63C  B1 D1    LDA ($D1),Y
.E63E  85 D7    STA $D7
.E640  29 3F    AND #$3F
.E642  06 D7    ASL $D7
.E644  24 D7    BIT $D7
.E646  10 02    BPL $E64A
.E648  09 80    ORA #$80
.E64A  90 04    BCC $E650
.E64C  A6 D4    LDX $D4
.E64E  D0 04    BNE $E654
.E650  70 02    BVS $E654
.E652  09 40    ORA #$40
.E654  E6 D3    INC $D3
.E656  20 84 E6 JSR $E684
.E659  C4 C8    CPY $C8
.E65B  D0 17    BNE $E674
.E65D  A9 00    LDA #$00
.E65F  85 D0    STA $D0
.E661  A9 0D    LDA #$0D
.E663  A6 99    LDX $99
.E665  E0 03    CPX #$03
.E667  F0 06    BEQ $E66F
.E669  A6 9A    LDX $9A
.E66B  E0 03    CPX #$03
.E66D  F0 03    BEQ $E672
.E66F  20 16 E7 JSR $E716
.E672  A9 0D    LDA #$0D
.E674  85 D7    STA $D7
.E676  68       PLA
.E677  AA       TAX
.E678  68       PLA
.E679  A8       TAY
.E67A  A5 D7    LDA $D7
.E67C  C9 DE    CMP #$DE   ; screen PI code
.E67E  D0 02    BNE $E682
.E680  A9 FF    LDA #$FF   ; petscii PI code
.E682  18       CLC
.E683  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$E67C**: screen PI code
- **$E680**: petscii PI code

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*