---
id: bd91-get-exponent-of-number-from-string
type: entity
title: get exponent of number from string
aliases:
- get exponent of number from string
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bd91-get-exponent-of-number-from-string.md
  sha256: c86959ab2099843b38bc849733fc98d7b101d0ac57775c56448c95f41dff03f1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bd91-get-exponent-of-number-from-string
---

# get exponent of number from string



# $BD91 — get exponent of number from string

## Disassemblatura
```assembly
.BD91  A5 5E    LDA $5E
.BD93  C9 0A    CMP #$0A
.BD95  90 09    BCC $BDA0
.BD97  A9 64    LDA #$64
.BD99  24 60    BIT $60
.BD9B  30 11    BMI $BDAE
.BD9D  4C 7E B9 JMP $B97E
.BDA0  0A       ASL
.BDA1  0A       ASL
.BDA2  18       CLC
.BDA3  65 5E    ADC $5E
.BDA5  0A       ASL
.BDA6  18       CLC
.BDA7  A0 00    LDY #$00
.BDA9  71 7A    ADC ($7A),Y
.BDAB  38       SEC
.BDAC  E9 30    SBC #$30   ; 0
.BDAE  85 5E    STA $5E
.BDB0  4C 30 BD JMP $BD30
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$BDAC**: 0

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BD91**: CHECK CURRENT VALUE
- **$BD93**: FOR MORE THAN 2 DIGITS
- **$BD95**: NO, THIS IS 1ST OR 2ND DIGIT
- **$BD97**: EXPONENT TOO BIG
- **$BD99**: UNLESS IT IS NEGATIVE
- **$BD9B**: LARGE NEGATIVE EXPONENT MAKES FAC=0
- **$BD9D**: LARGE POSITIVE EXPONENT IS ERROR
- **$BDA0**: EXPONENT TIMES 10
- **$BDA6**: <<< ASL ALREADY DID THIS! >>>
- **$BDA7**: ADD THE NEW DIGIT
- **$BDA9**: BUT THIS IS IN ASCII,
- **$BDAB**: SO ADJUST BACK TO BINARY
- **$BDAE**: NEW VALUE
- **$BDB0**: BACK FOR MORE
- **$BDB3**: 99,999,999.9
- **$BDB8**: 999,999,999
- **$BDBD**: 1,000,000,000

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bd91-get-exponent-of-number-from-string]]
