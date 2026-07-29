---
title: AND DESCRIPTOR IS A VARIABLE
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
- 00d3-pntr
- 00d7-data
- aa2c-string
- aa52-and-descriptor-is-a-variable
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $AA52
  address_end: $AA9D
  symbol: and-descriptor-is-a-variable
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AA52**: POINT AT LENGTH IN DESCRIPTOR'
---

# $AA52 — AND DESCRIPTOR IS A VARIABLE

## Disassemblatura
```assembly
.AA52  A0 00    LDY #$00   ; POINT AT LENGTH IN DESCRIPTOR
.AA54  B1 64    LDA ($64),Y   ; GET LENGTH
.AA56  20 75 B4 JSR $B475   ; MAKE A STRING THAT LONG UP ABOVE
.AA59  A5 50    LDA $50   ; SET UP SOURCE PNTR FOR MONINS
.AA5B  A4 51    LDY $51
.AA5D  85 6F    STA $6F
.AA5F  84 70    STY $70
.AA61  20 7A B6 JSR $B67A   ; MOVE STRING DATA TO NEW AREA
.AA64  A9 61    LDA #$61   ; ADDRESS OF DESCRIPTOR IS IN FAC
.AA66  A0 00    LDY #$00
.AA68  85 50    STA $50
.AA6A  84 51    STY $51
.AA6C  20 DB B6 JSR $B6DB   ; DISCARD DESCRIPTOR IF 'TWAS TEMPORARY
.AA6F  A0 00    LDY #$00   ; COPY STRING DESCRIPTOR
.AA71  B1 50    LDA ($50),Y
.AA73  91 49    STA ($49),Y
.AA75  C8       INY
.AA76  B1 50    LDA ($50),Y
.AA78  91 49    STA ($49),Y
.AA7A  C8       INY
.AA7B  B1 50    LDA ($50),Y
.AA7D  91 49    STA ($49),Y
.AA7F  60       RTS
.AA80  20 86 AA JSR $AA86
.AA83  4C B5 AB JMP $ABB5
.AA86  20 9E B7 JSR $B79E
.AA89  F0 05    BEQ $AA90
.AA8B  A9 2C    LDA #$2C
.AA8D  20 FF AE JSR $AEFF
.AA90  08       PHP
.AA91  86 13    STX $13
.AA93  20 18 E1 JSR $E118
.AA96  28       PLP
.AA97  4C A0 AA JMP $AAA0
.AA9A  20 21 AB JSR $AB21
.AA9D  20 79 00 JSR $0079
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AA52**: POINT AT LENGTH IN DESCRIPTOR
- **$AA54**: GET LENGTH
- **$AA56**: MAKE A STRING THAT LONG UP ABOVE
- **$AA59**: SET UP SOURCE PNTR FOR MONINS
- **$AA61**: MOVE STRING DATA TO NEW AREA
- **$AA64**: ADDRESS OF DESCRIPTOR IS IN FAC
- **$AA6C**: DISCARD DESCRIPTOR IF 'TWAS TEMPORARY
- **$AA6F**: COPY STRING DESCRIPTOR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*