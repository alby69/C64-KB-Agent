---
title: UNLESS CHAR AT TXTPTR = (A), SYNTAX ERROR
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
- 007a-txtptr
- aa2c-string
- af0d-recursive-get-value
- af61-integervariable-holen
- bc9b-integer
- return
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $AEFF
  address_end: $AFA4
  symbol: unless-char-at-txtptr-a-syntax-error
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AF05**: MATCH, GET NEXT CHAR &amp; RETURN'
---

# $AEFF — UNLESS CHAR AT TXTPTR = (A), SYNTAX ERROR

## Disassemblatura
```assembly
.AEFF  A0 00    LDY #$00
.AF01  D1 7A    CMP ($7A),Y
.AF03  D0 03    BNE $AF08
.AF05  4C 73 00 JMP $0073   ; MATCH, GET NEXT CHAR &amp; RETURN
.AF08  A2 0B    LDX #$0B
.AF0A  4C 37 A4 JMP $A437
.AF0D  A0 15    LDY #$15   ; POINT AT UNARY MINUS
.AF0F  68       PLA
.AF10  68       PLA
.AF11  4C FA AD JMP $ADFA
.AF14  38       SEC
.AF15  A5 64    LDA $64
.AF17  E9 00    SBC #$00
.AF19  A5 65    LDA $65
.AF1B  E9 A0    SBC #$A0
.AF1D  90 08    BCC $AF27
.AF1F  A9 A2    LDA #$A2
.AF21  E5 64    SBC $64
.AF23  A9 E3    LDA #$E3
.AF25  E5 65    SBC $65
.AF27  60       RTS
.AF28  20 8B B0 JSR $B08B
.AF2B  85 64    STA $64   ; ADDRESS OF VARIABLE
.AF2D  84 65    STY $65
.AF2F  A6 45    LDX $45   ; NUMERIC OR STRING?
.AF31  A4 46    LDY $46
.AF33  A5 0D    LDA $0D
.AF35  F0 26    BEQ $AF5D   ; NUMERIC
.AF37  A9 00    LDA #$00
.AF39  85 70    STA $70
.AF3B  20 14 AF JSR $AF14
.AF3E  90 1C    BCC $AF5C
.AF40  E0 54    CPX #$54
.AF42  D0 18    BNE $AF5C
.AF44  C0 C9    CPY #$C9
.AF46  D0 14    BNE $AF5C
.AF48  20 84 AF JSR $AF84
.AF4B  84 5E    STY $5E
.AF4D  88       DEY
.AF4E  84 71    STY $71
.AF50  A0 06    LDY #$06
.AF52  84 5D    STY $5D
.AF54  A0 24    LDY #$24
.AF56  20 68 BE JSR $BE68
.AF59  4C 6F B4 JMP $B46F
.AF5C  60       RTS
.AF5D  24 0E    BIT $0E
.AF5F  10 0D    BPL $AF6E   ; FLOATING POINT
.AF61  A0 00    LDY #$00   ; INTEGER
.AF63  B1 64    LDA ($64),Y
.AF65  AA       TAX   ; GET VALUE IN A,Y
.AF66  C8       INY
.AF67  B1 64    LDA ($64),Y
.AF69  A8       TAY
.AF6A  8A       TXA
.AF6B  4C 91 B3 JMP $B391   ; CONVERT A,Y TO FLOATING POINT
.AF6E  20 14 AF JSR $AF14
.AF71  90 2D    BCC $AFA0
.AF73  E0 54    CPX #$54
.AF75  D0 1B    BNE $AF92
.AF77  C0 49    CPY #$49
.AF79  D0 25    BNE $AFA0
.AF7B  20 84 AF JSR $AF84
.AF7E  98       TYA
.AF7F  A2 A0    LDX #$A0
.AF81  4C 4F BC JMP $BC4F
.AF84  20 DE FF JSR $FFDE
.AF87  86 64    STX $64
.AF89  84 63    STY $63
.AF8B  85 65    STA $65
.AF8D  A0 00    LDY #$00
.AF8F  84 62    STY $62
.AF91  60       RTS
.AF92  E0 53    CPX #$53
.AF94  D0 0A    BNE $AFA0
.AF96  C0 54    CPY #$54
.AF98  D0 06    BNE $AFA0
.AF9A  20 B7 FF JSR $FFB7
.AF9D  4C 3C BC JMP $BC3C
.AFA0  A5 64    LDA $64
.AFA2  A4 65    LDY $65
.AFA4  4C A2 BB JMP $BBA2
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AF05**: MATCH, GET NEXT CHAR &amp; RETURN
- **$AF0D**: POINT AT UNARY MINUS
- **$AF2B**: ADDRESS OF VARIABLE
- **$AF2F**: NUMERIC OR STRING?
- **$AF35**: NUMERIC
- **$AF5F**: FLOATING POINT
- **$AF61**: INTEGER
- **$AF65**: GET VALUE IN A,Y
- **$AF6B**: CONVERT A,Y TO FLOATING POINT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*