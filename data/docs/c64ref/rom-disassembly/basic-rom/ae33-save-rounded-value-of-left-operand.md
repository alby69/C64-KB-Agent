---
title: save rounded value of left operand
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
  address: $AE33
  address_end: $AE55
  symbol: save-rounded-value-of-left-operand
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AE39**: pull return address'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AE33**: GET FAC.SIGN TO PUSH IT'
---

# $AE33 — save rounded value of left operand

## Disassemblatura
```assembly
.AE33  A5 66    LDA $66
.AE35  BE 80 A0 LDX $A080,Y
.AE38  A8       TAY
.AE39  68       PLA   ; pull return address
.AE3A  85 22    STA $22
.AE3C  E6 22    INC $22
.AE3E  68       PLA   ; and store in $22/$23
.AE3F  85 23    STA $23
.AE41  98       TYA
.AE42  48       PHA
.AE43  20 1B BC JSR $BC1B
.AE46  A5 65    LDA $65
.AE48  48       PHA
.AE49  A5 64    LDA $64
.AE4B  48       PHA
.AE4C  A5 63    LDA $63
.AE4E  48       PHA
.AE4F  A5 62    LDA $62
.AE51  48       PHA
.AE52  A5 61    LDA $61
.AE54  48       PHA
.AE55  6C 22 00 JMP ($0022)   ; return to caller
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$AE39**: pull return address
- **$AE3E**: and store in $22/$23
- **$AE55**: return to caller

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AE33**: GET FAC.SIGN TO PUSH IT
- **$AE35**: PRECEDENCE BYTE FROM MATHTBL ENTER HERE FROM "STEP", TO PUSH STEP SIGN AND VALUE
- **$AE38**: FAC.SIGN OR SGN(STEP VALUE)
- **$AE39**: PULL RETURN ADDRESS AND ADD 1
- **$AE3A**: <<< ASSUMES NOT ON PAGE BOUNDARY! >>>
- **$AE3C**: PLACE BUMPED RETURN ADDRESS IN
- **$AE3E**: INDEX,INDEX+1
- **$AE41**: FAC.SIGN OR SGN(STEP VALUE)
- **$AE42**: PUSH FAC.SIGN OR SGN(STEP VALUE) ENTER HERE FROM "FOR", WITH (INDEX) = STEP, TO PUSH INITIAL VALUE OF "FOR" VARIABLE
- **$AE43**: ROUND TO 32 BITS
- **$AE46**: PUSH (FAC)
- **$AE55**: DO RTS FUNNY WAY
- **$AE58**: SET UP TO EXIT ROUTINE
- **$AE5B**: EXIT IF NO MATH TO DO

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*