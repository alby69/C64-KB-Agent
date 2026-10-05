---
id: ae20-get-vector-execute-function-then-continue-evaluation
type: entity
title: get vector, execute function then continue evaluation
aliases:
- get vector, execute function then continue evaluation
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae20-get-vector-execute-function-then-continue-evaluation.md
  sha256: 08b0b2fa81b58c3ed38803914d770e6e49937fcc4ac53f559466ef323a331e1b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ae20-get-vector-execute-function-then-continue-evaluation
---

# get vector, execute function then continue evaluation



# $AE20 — get vector, execute function then continue evaluation

## Disassemblatura
```assembly
.AE20  B9 82 A0 LDA $A082,Y   ; get function vector high byte
.AE23  48       PHA   ; onto stack
.AE24  B9 81 A0 LDA $A081,Y   ; get function vector low byte
.AE27  48       PHA   ; onto stack now push sign, round FAC1 and put on stack
.AE28  20 33 AE JSR $AE33   ; function will return here, then the next RTS will call the function
.AE2B  A5 4D    LDA $4D   ; get comparison evaluation flag
.AE2D  4C A9 AD JMP $ADA9   ; continue evaluating expression
.AE30  4C 08 AF JMP $AF08   ; do syntax error then warm start
.AE33  A5 66    LDA $66   ; get FAC1 sign (b7)
.AE35  BE 80 A0 LDX $A080,Y   ; get precedence byte
```


## Commenti

### Original Disassembly (—)
- **$AE20**: get function vector high byte
- **$AE23**: onto stack
- **$AE24**: get function vector low byte
- **$AE27**: onto stack now push sign, round FAC1 and put on stack
- **$AE28**: function will return here, then the next RTS will call the function
- **$AE2B**: get comparison evaluation flag
- **$AE2D**: continue evaluating expression
- **$AE30**: do syntax error then warm start
- **$AE33**: get FAC1 sign (b7)
- **$AE35**: get precedence byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ae20-get-vector-execute-function-then-continue-evaluation]]
