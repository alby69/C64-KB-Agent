---
title: get exponent of number from string
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
  address: $BD91
  address_end: $BDB0
  symbol: get-exponent-of-number-from-string
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BDAC**: 0'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BD91**: CHECK CURRENT VALUE'
---

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