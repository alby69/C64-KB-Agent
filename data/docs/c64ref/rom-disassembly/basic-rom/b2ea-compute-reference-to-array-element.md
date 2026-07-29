---
title: compute reference to array element
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
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
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  address: $B2EA
  address_end: $B34B
  symbol: compute-reference-to-array-element
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B2EA**: GET # OF DIMENSIONS'
---

# $B2EA — compute reference to array element

## Disassemblatura
```assembly
.B2EA  B1 5F    LDA ($5F),Y
.B2EC  85 0B    STA $0B
.B2EE  A9 00    LDA #$00
.B2F0  85 71    STA $71
.B2F2  85 72    STA $72
.B2F4  C8       INY
.B2F5  68       PLA
.B2F6  AA       TAX
.B2F7  85 64    STA $64
.B2F9  68       PLA
.B2FA  85 65    STA $65
.B2FC  D1 5F    CMP ($5F),Y
.B2FE  90 0E    BCC $B30E
.B300  D0 06    BNE $B308
.B302  C8       INY
.B303  8A       TXA
.B304  D1 5F    CMP ($5F),Y
.B306  90 07    BCC $B30F
.B308  4C 45 B2 JMP $B245
.B30B  4C 35 A4 JMP $A435
.B30E  C8       INY
.B30F  A5 72    LDA $72
.B311  05 71    ORA $71
.B313  18       CLC
.B314  F0 0A    BEQ $B320
.B316  20 4C B3 JSR $B34C
.B319  8A       TXA
.B31A  65 64    ADC $64
.B31C  AA       TAX
.B31D  98       TYA
.B31E  A4 22    LDY $22
.B320  65 65    ADC $65
.B322  86 71    STX $71
.B324  C6 0B    DEC $0B
.B326  D0 CA    BNE $B2F2
.B328  85 72    STA $72
.B32A  A2 05    LDX #$05
.B32C  A5 45    LDA $45
.B32E  10 01    BPL $B331
.B330  CA       DEX
.B331  A5 46    LDA $46
.B333  10 02    BPL $B337
.B335  CA       DEX
.B336  CA       DEX
.B337  86 28    STX $28
.B339  A9 00    LDA #$00
.B33B  20 55 B3 JSR $B355
.B33E  8A       TXA
.B33F  65 58    ADC $58
.B341  85 47    STA $47
.B343  98       TYA
.B344  65 59    ADC $59
.B346  85 48    STA $48
.B348  A8       TAY
.B349  A5 47    LDA $47
.B34B  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B2EA**: GET # OF DIMENSIONS
- **$B2EE**: ZERO SUBSCRIPT ACCUMULATOR
- **$B2F5**: PULL NEXT SUBSCRIPT FROM STACK
- **$B2F6**: SAVE IN FAC+3,4
- **$B2F7**: AND COMPARE WITH DIMENSIONED SIZE
- **$B2FE**: SUBSCRIPT NOT TOO LARGE
- **$B300**: SUBSCRIPT IS TOO LARGE
- **$B302**: CHECK LOW-BYTE OF SUBSCRIPT
- **$B306**: NOT TOO LARGE
- **$B308**: BAD SUBSCRIPTS ERROR
- **$B30B**: MEM FULL ERROR
- **$B30E**: BUMP POINTER INTO DESCRIPTOR
- **$B30F**: BYPASS MULTIPLICATION IF VALUE SO
- **$B311**: FAR = 0
- **$B314**: IT IS ZERO SO FAR
- **$B316**: NOT ZERO, SO MULTIPLY
- **$B319**: ADD CURRENT SUBSCRIPT
- **$B31E**: RETRIEVE Y SAVED BY MULTIPLY.SUBSCRIPT
- **$B320**: FINISH ADDING CURRENT SUBSCRIPT
- **$B322**: STORE ACCUMULATED OFFSET
- **$B324**: LAST SUBSCRIPT YET?
- **$B326**: NO, LOOP TILL DONE
- **$B328**: YES, NOW MULTIPLY BE ELEMENT SIZE
- **$B32A**: START WITH SIZE = 5
- **$B32C**: DETERMINE VARIABLE TYPE
- **$B32E**: NOT INTEGER
- **$B330**: INTEGER, BACK DOWN SIZE TO 4 BYTES
- **$B331**: DISCRIMINATE BETWEEN REAL AND STR
- **$B333**: IT IS REAL
- **$B335**: SIZE = 3 IF STRING, =2 IF INTEGER
- **$B337**: SET UP MULTIPLIER
- **$B339**: HI-BYTE OF MULTIPLIER
- **$B33B**: (STRNG2) BY ELEMENT SIZE
- **$B33E**: ADD ACCUMULATED OFFSET
- **$B33F**: TO ADDRESS OF 1ST ELEMENT
- **$B341**: TO GET ADDRESS OF SPECIFIED ELEMENT
- **$B348**: RETURN WITH ADDR IN VARPNT
- **$B349**: AND IN Y,A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*