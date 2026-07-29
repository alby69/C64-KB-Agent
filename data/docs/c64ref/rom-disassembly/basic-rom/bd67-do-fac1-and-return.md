---
title: do - FAC1 and return
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bd67-do-fac1-and-return
- bd6a-accumulate-a-digit-into-fac
- bd7e-add-a-to-fac
- bd91-accumulate-digit-of-exponent
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $BD67
  address_end: $BDB0
  symbol: do-fac1-and-return
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BD67**: do - FAC1 do unsigned FAC1*10+number'
---

# $BD67 — do - FAC1 and return

## Disassemblatura
```assembly
.BD67  4C B4 BF JMP $BFB4   ; do - FAC1 do unsigned FAC1*10+number
.BD6A  48       PHA   ; save character
.BD6B  24 5F    BIT $5F   ; test decimal point flag
.BD6D  10 02    BPL $BD71   ; skip exponent increment if not set
.BD6F  E6 5D    INC $5D   ; else increment number exponent
.BD71  20 E2 BA JSR $BAE2   ; multiply FAC1 by 10
.BD74  68       PLA   ; restore character
.BD75  38       SEC   ; set carry for subtract
.BD76  E9 30    SBC #$30   ; convert to binary
.BD78  20 7E BD JSR $BD7E   ; evaluate new ASCII digit
.BD7B  4C 0A BD JMP $BD0A   ; go do next character evaluate new ASCII digit multiply FAC1 by 10 then (ABS) add in new digit
.BD7E  48       PHA   ; save digit
.BD7F  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.BD82  68       PLA   ; restore digit
.BD83  20 3C BC JSR $BC3C   ; save A as integer byte
.BD86  A5 6E    LDA $6E   ; get FAC2 sign (b7)
.BD88  45 66    EOR $66   ; toggle with FAC1 sign (b7)
.BD8A  85 6F    STA $6F   ; save sign compare (FAC1 EOR FAC2)
.BD8C  A6 61    LDX $61   ; get FAC1 exponent
.BD8E  4C 6A B8 JMP $B86A   ; add FAC2 to FAC1 and return evaluate next character of exponential part of number
.BD91  A5 5E    LDA $5E   ; get exponent count byte
.BD93  C9 0A    CMP #$0A   ; compare with 10 decimal
.BD95  90 09    BCC $BDA0   ; branch if less
.BD97  A9 64    LDA #$64   ; make all -ve exponents = -100 decimal (causes underflow)
.BD99  24 60    BIT $60   ; test exponent -ve flag
.BD9B  30 11    BMI $BDAE   ; branch if -ve
.BD9D  4C 7E B9 JMP $B97E   ; else do overflow error then warm start
.BDA0  0A       ASL   ; *2
.BDA1  0A       ASL   ; *4
.BDA2  18       CLC   ; clear carry for add
.BDA3  65 5E    ADC $5E   ; *5
.BDA5  0A       ASL   ; *10
.BDA6  18       CLC   ; clear carry for add
.BDA7  A0 00    LDY #$00   ; set index
.BDA9  71 7A    ADC ($7A),Y   ; add character (will be $30 too much!)
.BDAB  38       SEC   ; set carry for subtract
.BDAC  E9 30    SBC #$30   ; convert character to binary
.BDAE  85 5E    STA $5E   ; save exponent count byte
.BDB0  4C 30 BD JMP $BD30   ; go get next character
```


## Commenti

### Original Disassembly (—)
- **$BD67**: do - FAC1 do unsigned FAC1*10+number
- **$BD6A**: save character
- **$BD6B**: test decimal point flag
- **$BD6D**: skip exponent increment if not set
- **$BD6F**: else increment number exponent
- **$BD71**: multiply FAC1 by 10
- **$BD74**: restore character
- **$BD75**: set carry for subtract
- **$BD76**: convert to binary
- **$BD78**: evaluate new ASCII digit
- **$BD7B**: go do next character evaluate new ASCII digit multiply FAC1 by 10 then (ABS) add in new digit
- **$BD7E**: save digit
- **$BD7F**: round and copy FAC1 to FAC2
- **$BD82**: restore digit
- **$BD83**: save A as integer byte
- **$BD86**: get FAC2 sign (b7)
- **$BD88**: toggle with FAC1 sign (b7)
- **$BD8A**: save sign compare (FAC1 EOR FAC2)
- **$BD8C**: get FAC1 exponent
- **$BD8E**: add FAC2 to FAC1 and return evaluate next character of exponential part of number
- **$BD91**: get exponent count byte
- **$BD93**: compare with 10 decimal
- **$BD95**: branch if less
- **$BD97**: make all -ve exponents = -100 decimal (causes underflow)
- **$BD99**: test exponent -ve flag
- **$BD9B**: branch if -ve
- **$BD9D**: else do overflow error then warm start
- **$BDA0**: *2
- **$BDA1**: *4
- **$BDA2**: clear carry for add
- **$BDA3**: *5
- **$BDA5**: *10
- **$BDA6**: clear carry for add
- **$BDA7**: set index
- **$BDA9**: add character (will be $30 too much!)
- **$BDAB**: set carry for subtract
- **$BDAC**: convert character to binary
- **$BDAE**: save exponent count byte
- **$BDB0**: go get next character

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*