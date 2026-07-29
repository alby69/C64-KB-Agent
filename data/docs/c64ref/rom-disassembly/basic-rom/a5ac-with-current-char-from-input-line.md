---
title: WITH CURRENT CHAR FROM INPUT LINE
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
- 0022-index
- 00d7-data
- a5ac-with-current-char-from-input-line
- bc5b-fac
- bit
- clear
- f5ed-save
- input
- inx
- iny
- output
- store
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $A5AC
  address_end: $A5E3
  symbol: with-current-char-from-input-line
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A5AC**: SAVE INDEX TO OUTPUT LINE'
---

# $A5AC — WITH CURRENT CHAR FROM INPUT LINE

## Disassemblatura
```assembly
.A5AC  84 71    STY $71   ; SAVE INDEX TO OUTPUT LINE
.A5AE  A0 00    LDY #$00   ; USE Y-REG WITH (FAC) TO ADDRESS TABLE
.A5B0  84 0B    STY $0B   ; HOLDS CURRENT TOKEN-$80
.A5B2  88       DEY   ; PREPARE FOR "INY" A FEW LINES DOWN
.A5B3  86 7A    STX $7A   ; SAVE POSITION IN INPUT LINE
.A5B5  CA       DEX   ; PREPARE FOR "INX" A FEW LINES DOWN
.A5B6  C8       INY   ; ADVANCE POINTER TO TOKEN TABLE
.A5B7  E8       INX
.A5B8  BD 00 02 LDA $0200,X   ; NEXT CHAR FROM INPUT LINE
.A5BB  38       SEC   ; NO, COMPARE TO CHAR IN TABLE
.A5BC  F9 9E A0 SBC $A09E,Y   ; SAME AS NEXT CHAR OF TOKEN NAME?
.A5BF  F0 F5    BEQ $A5B6   ; YES, CONTINUE MATCHING
.A5C1  C9 80    CMP #$80   ; MAYBE; WAS IT SAME EXCEPT FOR BIT 7?
.A5C3  D0 30    BNE $A5F5   ; NO, SKIP TO NEXT TOKEN
.A5C5  05 0B    ORA $0B   ; YES, END OF TOKEN; GET TOKEN #
.A5C7  A4 71    LDY $71   ; GET INDEX TO OUTPUT LINE IN Y-REG
.A5C9  E8       INX   ; ADVANCE INPUT INDEX
.A5CA  C8       INY   ; ADVANCE OUTPUT INDEX
.A5CB  99 FB 01 STA $01FB,Y   ; STORE CHAR OR TOKEN
.A5CE  B9 FB 01 LDA $01FB,Y   ; TEST FOR EOL OR EOS
.A5D1  F0 36    BEQ $A609   ; END OF LINE
.A5D3  38       SEC
.A5D4  E9 3A    SBC #$3A   ; END OF STATEMENT?
.A5D6  F0 04    BEQ $A5DC   ; YES, CLEAR DATAFLG
.A5D8  C9 49    CMP #$49   ; "DATA" TOKEN?
.A5DA  D0 02    BNE $A5DE   ; NO, LEAVE DATAFLG ALONE
.A5DC  85 0F    STA $0F   ; DATAFLG = 0 OR $83-$3A = $49
.A5DE  38       SEC   ; IS IT A "REM" TOKEN?
.A5DF  E9 55    SBC #$55
.A5E1  D0 9F    BNE $A582   ; NO, CONTINUE PARSING LINE
.A5E3  85 08    STA $08   ; YES, CLEAR LITERAL FLAG
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A5AC**: SAVE INDEX TO OUTPUT LINE
- **$A5AE**: USE Y-REG WITH (FAC) TO ADDRESS TABLE
- **$A5B0**: HOLDS CURRENT TOKEN-$80
- **$A5B2**: PREPARE FOR "INY" A FEW LINES DOWN
- **$A5B3**: SAVE POSITION IN INPUT LINE
- **$A5B5**: PREPARE FOR "INX" A FEW LINES DOWN
- **$A5B6**: ADVANCE POINTER TO TOKEN TABLE
- **$A5B8**: NEXT CHAR FROM INPUT LINE
- **$A5BB**: NO, COMPARE TO CHAR IN TABLE
- **$A5BC**: SAME AS NEXT CHAR OF TOKEN NAME?
- **$A5BF**: YES, CONTINUE MATCHING
- **$A5C1**: MAYBE; WAS IT SAME EXCEPT FOR BIT 7?
- **$A5C3**: NO, SKIP TO NEXT TOKEN
- **$A5C5**: YES, END OF TOKEN; GET TOKEN #
- **$A5C7**: GET INDEX TO OUTPUT LINE IN Y-REG
- **$A5C9**: ADVANCE INPUT INDEX
- **$A5CA**: ADVANCE OUTPUT INDEX
- **$A5CB**: STORE CHAR OR TOKEN
- **$A5CE**: TEST FOR EOL OR EOS
- **$A5D1**: END OF LINE
- **$A5D4**: END OF STATEMENT?
- **$A5D6**: YES, CLEAR DATAFLG
- **$A5D8**: "DATA" TOKEN?
- **$A5DA**: NO, LEAVE DATAFLG ALONE
- **$A5DC**: DATAFLG = 0 OR $83-$3A = $49
- **$A5DE**: IS IT A "REM" TOKEN?
- **$A5E1**: NO, CONTINUE PARSING LINE
- **$A5E3**: YES, CLEAR LITERAL FLAG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*