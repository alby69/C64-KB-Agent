---
title: PERFORM STACKED OPERATION
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
- 0069-arg
- 0090-status
- aa2c-string
- ae5d-perform-stacked-operation
- bc5b-fac
- eor
- f5ed-save
- rts
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $AE5D
  address_end: $AE82
  symbol: perform-stacked-operation
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AE5D**: WAS IT RELATIONAL OPERATOR?'
---

# $AE5D — PERFORM STACKED OPERATION

## Disassemblatura
```assembly
.AE5D  C9 64    CMP #$64   ; WAS IT RELATIONAL OPERATOR?
.AE5F  F0 03    BEQ $AE64   ; YES, ALLOW STRING COMPARE
.AE61  20 8D AD JSR $AD8D   ; MUST BE NUMERIC VALUE
.AE64  84 4B    STY $4B
.AE66  68       PLA   ; GET 0000<=>C FROM STACK
.AE67  4A       LSR   ; SHIFT TO 00000<=> FORM
.AE68  85 12    STA $12   ; 00000<=>
.AE6A  68       PLA
.AE6B  85 69    STA $69   ; GET FLOATING POINT VALUE OFF STACK,
.AE6D  68       PLA   ; AND PUT IT IN ARG
.AE6E  85 6A    STA $6A
.AE70  68       PLA
.AE71  85 6B    STA $6B
.AE73  68       PLA
.AE74  85 6C    STA $6C
.AE76  68       PLA
.AE77  85 6D    STA $6D
.AE79  68       PLA
.AE7A  85 6E    STA $6E
.AE7C  45 66    EOR $66   ; SAVE EOR OF SIGNS OF THE OPERANDS,
.AE7E  85 6F    STA $6F   ; IN CASE OF MULTIPLY OR DIVIDE
.AE80  A5 61    LDA $61   ; FAC EXPONENT IN A-REG
.AE82  60       RTS   ; STATUS .EQ. IF (FAC)=0 RTS GOES TO PERFORM OPERATION
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AE5D**: WAS IT RELATIONAL OPERATOR?
- **$AE5F**: YES, ALLOW STRING COMPARE
- **$AE61**: MUST BE NUMERIC VALUE
- **$AE66**: GET 0000<=>C FROM STACK
- **$AE67**: SHIFT TO 00000<=> FORM
- **$AE68**: 00000<=>
- **$AE6B**: GET FLOATING POINT VALUE OFF STACK,
- **$AE6D**: AND PUT IT IN ARG
- **$AE7C**: SAVE EOR OF SIGNS OF THE OPERANDS,
- **$AE7E**: IN CASE OF MULTIPLY OR DIVIDE
- **$AE80**: FAC EXPONENT IN A-REG
- **$AE82**: STATUS .EQ. IF (FAC)=0 RTS GOES TO PERFORM OPERATION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*