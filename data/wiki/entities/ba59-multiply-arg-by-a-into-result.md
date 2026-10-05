---
id: ba59-multiply-arg-by-a-into-result
type: entity
title: MULTIPLY ARG BY (A) INTO RESULT
aliases:
- MULTIPLY ARG BY (A) INTO RESULT
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ba59-multiply-arg-by-a-into-result.md
  sha256: 027cb83ce4df36329ebfea2aa24c7d14c7cb8357ca8b443669059ace1652cee8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ba59-multiply-arg-by-a-into-result
---

# MULTIPLY ARG BY (A) INTO RESULT



# $BA59 — MULTIPLY ARG BY (A) INTO RESULT

## Disassemblatura
```assembly
.BA59  D0 03    BNE $BA5E   ; THIS BYTE NON-ZERO
.BA5B  4C 83 B9 JMP $B983   ; (A)=0, JUST SHIFT ARG RIGHT 8
.BA5E  4A       LSR   ; SHIFT BIT INTO CARRY
.BA5F  09 80    ORA #$80   ; SUPPLY SENTINEL BIT
.BA61  A8       TAY   ; REMAINING MULTIPLIER TO Y
.BA62  90 19    BCC $BA7D   ; THIS MULTIPLIER BIT = 0
.BA64  18       CLC   ; = 1, SO ADD ARG TO RESULT
.BA65  A5 29    LDA $29
.BA67  65 6D    ADC $6D
.BA69  85 29    STA $29
.BA6B  A5 28    LDA $28
.BA6D  65 6C    ADC $6C
.BA6F  85 28    STA $28
.BA71  A5 27    LDA $27
.BA73  65 6B    ADC $6B
.BA75  85 27    STA $27
.BA77  A5 26    LDA $26
.BA79  65 6A    ADC $6A
.BA7B  85 26    STA $26
.BA7D  66 26    ROR $26   ; SHIFT RESULT RIGHT 1
.BA7F  66 27    ROR $27
.BA81  66 28    ROR $28
.BA83  66 29    ROR $29
.BA85  66 70    ROR $70
.BA87  98       TYA   ; REMAINING MULTIPLIER
.BA88  4A       LSR   ; LSB INTO CARRY
.BA89  D0 D6    BNE $BA61   ; IF SENTINEL STILL HERE, MULTIPLY
.BA8B  60       RTS   ; 8 X 32 COMPLETED
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BA59**: THIS BYTE NON-ZERO
- **$BA5B**: (A)=0, JUST SHIFT ARG RIGHT 8
- **$BA5E**: SHIFT BIT INTO CARRY
- **$BA5F**: SUPPLY SENTINEL BIT
- **$BA61**: REMAINING MULTIPLIER TO Y
- **$BA62**: THIS MULTIPLIER BIT = 0
- **$BA64**: = 1, SO ADD ARG TO RESULT
- **$BA7D**: SHIFT RESULT RIGHT 1
- **$BA87**: REMAINING MULTIPLIER
- **$BA88**: LSB INTO CARRY
- **$BA89**: IF SENTINEL STILL HERE, MULTIPLY
- **$BA8B**: 8 X 32 COMPLETED

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ba59-multiply-arg-by-a-into-result]]
