---
title: MOVE GENERIC CHRGET AND RANDOM SEED INTO PLACE
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0022-index
- 0073-chrget
- 00b1-temp
- aa2c-string
- d41b-random
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $E3E0
  address_end: $E45E
  symbol: move-generic-chrget-and-random-seed-into-place
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E3EA**: SET LENGTH OF TEMP. STRING DESCRIPTORS'
---

# $E3E0 — MOVE GENERIC CHRGET AND RANDOM SEED INTO PLACE

## Disassemblatura
```assembly
.E3E0  A2 1C    LDX #$1C
.E3E2  BD A2 E3 LDA $E3A2,X
.E3E5  95 73    STA $73,X
.E3E7  CA       DEX
.E3E8  10 F8    BPL $E3E2
.E3EA  A9 03    LDA #$03   ; SET LENGTH OF TEMP. STRING DESCRIPTORS
.E3EC  85 53    STA $53   ; FOR GARBAGE COLLECTION SUBROUTINE
.E3EE  A9 00    LDA #$00
.E3F0  85 68    STA $68
.E3F2  85 13    STA $13
.E3F4  85 18    STA $18
.E3F6  A2 01    LDX #$01   ; SET UP FAKE FORWARD LINK
.E3F8  8E FD 01 STX $01FD
.E3FB  8E FC 01 STX $01FC
.E3FE  A2 19    LDX #$19   ; INIT INDEX TO TEMP STRING DESCRIPTORS
.E400  86 16    STX $16
.E402  38       SEC
.E403  20 9C FF JSR $FF9C
.E406  86 2B    STX $2B
.E408  84 2C    STY $2C
.E40A  38       SEC
.E40B  20 99 FF JSR $FF99
.E40E  86 37    STX $37
.E410  84 38    STY $38
.E412  86 33    STX $33
.E414  84 34    STY $34
.E416  A0 00    LDY #$00
.E418  98       TYA
.E419  91 2B    STA ($2B),Y
.E41B  E6 2B    INC $2B
.E41D  D0 02    BNE $E421
.E41F  E6 2C    INC $2C
.E421  60       RTS
.E422  A5 2B    LDA $2B
.E424  A4 2C    LDY $2C
.E426  20 08 A4 JSR $A408
.E429  A9 73    LDA #$73
.E42B  A0 E4    LDY #$E4
.E42D  20 1E AB JSR $AB1E
.E430  A5 37    LDA $37
.E432  38       SEC
.E433  E5 2B    SBC $2B
.E435  AA       TAX
.E436  A5 38    LDA $38
.E438  E5 2C    SBC $2C
.E43A  20 CD BD JSR $BDCD
.E43D  A9 60    LDA #$60
.E43F  A0 E4    LDY #$E4
.E441  20 1E AB JSR $AB1E
.E444  4C 44 A6 JMP $A644
.E447  8B E3 83 A4 7C A5 1A A7
.E44F  E4 A7 86 AE
.E453  A2 0B    LDX #$0B
.E455  BD 47 E4 LDA $E447,X
.E458  9D 00 03 STA $0300,X
.E45B  CA       DEX
.E45C  10 F7    BPL $E455
.E45E  60       RTS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E3EA**: SET LENGTH OF TEMP. STRING DESCRIPTORS
- **$E3EC**: FOR GARBAGE COLLECTION SUBROUTINE
- **$E3F6**: SET UP FAKE FORWARD LINK
- **$E3FE**: INIT INDEX TO TEMP STRING DESCRIPTORS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*