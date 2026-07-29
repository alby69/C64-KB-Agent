---
title: INSTALL STRING, DESCRIPTOR ADDRESS IS AT FAC+3,4
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
- 0033-fretop
- 00d7-data
- a9da-install-string-descriptor-address-is-at-fac34
- aa2c-string
- bc5b-fac
- store
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $A9DA
  address_end: $AA4F
  symbol: install-string-descriptor-address-is-at-fac34
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A9DA**: STRING DATA ALREADY IN STRING AREA?'
---

# $A9DA — INSTALL STRING, DESCRIPTOR ADDRESS IS AT FAC+3,4

## Disassemblatura
```assembly
.A9DA  A4 4A    LDY $4A   ; STRING DATA ALREADY IN STRING AREA?
.A9DC  C0 BF    CPY #$BF
.A9DE  D0 4C    BNE $AA2C
.A9E0  20 A6 B6 JSR $B6A6
.A9E3  C9 06    CMP #$06
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
.AA1D  B1 22    LDA ($22),Y
.AA1F  20 80 00 JSR $0080
.AA22  90 03    BCC $AA27
.AA24  4C 48 B2 JMP $B248
.AA27  E9 2F    SBC #$2F
.AA29  4C 7E BD JMP $BD7E
.AA2C  A0 02    LDY #$02
.AA2E  B1 64    LDA ($64),Y   ; (STRING AREA IS BTWN FRETOP
.AA30  C5 34    CMP $34   ; HIMEM)
.AA32  90 17    BCC $AA4B   ; YES, DATA ALREADY UP THERE
.AA34  D0 07    BNE $AA3D   ; NO
.AA36  88       DEY   ; MAYBE, TEST LOW BYTE OF POINTER
.AA37  B1 64    LDA ($64),Y
.AA39  C5 33    CMP $33
.AA3B  90 0E    BCC $AA4B   ; YES, ALREADY THERE
.AA3D  A4 65    LDY $65   ; NO. DESCRIPTOR ALREADY AMONG VARIABLES?
.AA3F  C4 2E    CPY $2E
.AA41  90 08    BCC $AA4B   ; NO
.AA43  D0 0D    BNE $AA52   ; YES
.AA45  A5 64    LDA $64   ; MAYBE, COMPARE LO-BYTE
.AA47  C5 2D    CMP $2D
.AA49  B0 07    BCS $AA52   ; YES, DESCRIPTOR IS AMONG VARIABLES
.AA4B  A5 64    LDA $64   ; EITHER STRING ALREADY ON TOP, OR
.AA4D  A4 65    LDY $65   ; DESCRIPTOR IS NOT A VARIABLE
.AA4F  4C 68 AA JMP $AA68   ; SO JUST STORE THE DESCRIPTOR
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A9DA**: STRING DATA ALREADY IN STRING AREA?
- **$AA2E**: (STRING AREA IS BTWN FRETOP
- **$AA30**: HIMEM)
- **$AA32**: YES, DATA ALREADY UP THERE
- **$AA34**: NO
- **$AA36**: MAYBE, TEST LOW BYTE OF POINTER
- **$AA3B**: YES, ALREADY THERE
- **$AA3D**: NO. DESCRIPTOR ALREADY AMONG VARIABLES?
- **$AA41**: NO
- **$AA43**: YES
- **$AA45**: MAYBE, COMPARE LO-BYTE
- **$AA49**: YES, DESCRIPTOR IS AMONG VARIABLES
- **$AA4B**: EITHER STRING ALREADY ON TOP, OR
- **$AA4D**: DESCRIPTOR IS NOT A VARIABLE
- **$AA4F**: SO JUST STORE THE DESCRIPTOR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*