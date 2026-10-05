---
id: b7f1-evaluate-expression
type: entity
title: EVALUATE ",EXPRESSION"
aliases:
- EVALUATE ",EXPRESSION"
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b7f1-evaluate-expression.md
  sha256: d82ada53fba374c9c398347a96e11c77d2b72dd5f89bcd7e2bf8bd9e4810dbb2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b7f1-evaluate-expression
---

# EVALUATE ",EXPRESSION"



# $B7F1 — EVALUATE ",EXPRESSION"

## Disassemblatura
```assembly
.B7F1  20 FD AE JSR $AEFD   ; MUST HAVE COMMA FIRST
.B7F4  4C 9E B7 JMP $B79E   ; CONVERT EXPRESSION TO BYTE IN X-REG
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B7F1**: MUST HAVE COMMA FIRST
- **$B7F4**: CONVERT EXPRESSION TO BYTE IN X-REG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b7f1-evaluate-expression]]
