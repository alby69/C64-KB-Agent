---
title: ACCUMULATE A DIGIT INTO FAC
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
- 00a5-count
- bc5b-fac
- bc9b-integer
- bd6a-accumulate-a-digit-into-fac
- f5ed-save
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BD6A
  address_end: $BD7B
  symbol: accumulate-a-digit-into-fac
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BD6A**: SAVE DIGIT'
---

# $BD6A — ACCUMULATE A DIGIT INTO FAC

## Disassemblatura
```assembly
.BD6A  48       PHA   ; SAVE DIGIT
.BD6B  24 5F    BIT $5F   ; SEEN A DECIMAL POINT YET?
.BD6D  10 02    BPL $BD71   ; NO, STILL IN INTEGER PART
.BD6F  E6 5D    INC $5D   ; YES, COUNT THE FRACTIONAL DIGIT
.BD71  20 E2 BA JSR $BAE2   ; FAC = FAC * 10
.BD74  68       PLA   ; CURRENT DIGIT
.BD75  38       SEC   ; <<<SHORTER HERE TO JUST "AND #$0F">>>
.BD76  E9 30    SBC #$30   ; <<<TO CONVERT ASCII TO BINARY FORM>>>
.BD78  20 7E BD JSR $BD7E   ; ADD THE DIGIT
.BD7B  4C 0A BD JMP $BD0A   ; GO BACK FOR MORE
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BD6A**: SAVE DIGIT
- **$BD6B**: SEEN A DECIMAL POINT YET?
- **$BD6D**: NO, STILL IN INTEGER PART
- **$BD6F**: YES, COUNT THE FRACTIONAL DIGIT
- **$BD71**: FAC = FAC * 10
- **$BD74**: CURRENT DIGIT
- **$BD75**: <<<SHORTER HERE TO JUST "AND #$0F">>>
- **$BD76**: <<<TO CONVERT ASCII TO BINARY FORM>>>
- **$BD78**: ADD THE DIGIT
- **$BD7B**: GO BACK FOR MORE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*