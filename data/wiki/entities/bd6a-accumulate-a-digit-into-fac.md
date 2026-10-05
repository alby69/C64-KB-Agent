---
id: bd6a-accumulate-a-digit-into-fac
type: entity
title: ACCUMULATE A DIGIT INTO FAC
aliases:
- ACCUMULATE A DIGIT INTO FAC
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bd6a-accumulate-a-digit-into-fac.md
  sha256: 94191af68c2ebd679d53cf16580f30d0b34f80905fb4bbefa629ccf3f092c26e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bd6a-accumulate-a-digit-into-fac
---

# ACCUMULATE A DIGIT INTO FAC



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

## References
- Source: [[src-bd6a-accumulate-a-digit-into-fac]]
