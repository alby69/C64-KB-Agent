---
title: CLEAR ALL VARIABLES
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
- 00d3-pntr
- a52a-clear-all-variables
- a533-basic-zeilen-neu-binden
- clear
- clears
- store
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $A52A
  address_end: $A579
  symbol: clear-all-variables
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A52A**: CLEAR ALL VARIABLES'
---

# $A52A — CLEAR ALL VARIABLES

## Disassemblatura
```assembly
.A52A  20 59 A6 JSR $A659   ; CLEAR ALL VARIABLES
.A52D  20 33 A5 JSR $A533
.A530  4C 80 A4 JMP $A480
.A533  A5 2B    LDA $2B   ; POINT INDEX AT START OF PROGRAM
.A535  A4 2C    LDY $2C
.A537  85 22    STA $22
.A539  84 23    STY $23
.A53B  18       CLC
.A53C  A0 01    LDY #$01   ; HI-BYTE OF NEXT FORWARD PNTR
.A53E  B1 22    LDA ($22),Y   ; END OF PROGRAM YET?
.A540  F0 1D    BEQ $A55F
.A542  A0 04    LDY #$04   ; FIND END OF THIS LINE
.A544  C8       INY   ; (NOTE MAXIMUM LENGTH < 256)
.A545  B1 22    LDA ($22),Y
.A547  D0 FB    BNE $A544
.A549  C8       INY   ; COMPUTE ADDRESS OF NEXT LINE
.A54A  98       TYA
.A54B  65 22    ADC $22
.A54D  AA       TAX
.A54E  A0 00    LDY #$00   ; STORE FORWARD PNTR IN THIS LINE
.A550  91 22    STA ($22),Y
.A552  A5 23    LDA $23
.A554  69 00    ADC #$00   ; (NOTE: THIS CLEARS CARRY)
.A556  C8       INY
.A557  91 22    STA ($22),Y
.A559  86 22    STX $22
.A55B  85 23    STA $23
.A55D  90 DD    BCC $A53C   ; ...ALWAYS
.A55F  60       RTS
.A560  A2 00    LDX #$00
.A562  20 12 E1 JSR $E112
.A565  C9 0D    CMP #$0D
.A567  F0 0D    BEQ $A576
.A569  9D 00 02 STA $0200,X
.A56C  E8       INX
.A56D  E0 59    CPX #$59
.A56F  90 F1    BCC $A562
.A571  A2 17    LDX #$17
.A573  4C 37 A4 JMP $A437
.A576  4C CA AA JMP $AACA
.A579  6C 04 03 JMP ($0304)
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A52A**: CLEAR ALL VARIABLES
- **$A533**: POINT INDEX AT START OF PROGRAM
- **$A53C**: HI-BYTE OF NEXT FORWARD PNTR
- **$A53E**: END OF PROGRAM YET?
- **$A542**: FIND END OF THIS LINE
- **$A544**: (NOTE MAXIMUM LENGTH < 256)
- **$A549**: COMPUTE ADDRESS OF NEXT LINE
- **$A54E**: STORE FORWARD PNTR IN THIS LINE
- **$A554**: (NOTE: THIS CLEARS CARRY)
- **$A55D**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*