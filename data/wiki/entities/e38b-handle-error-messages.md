---
id: e38b-handle-error-messages
type: entity
title: handle error messages
aliases:
- handle error messages
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e38b-handle-error-messages.md
  sha256: 8e603d5919bd4f2d2c03489754f7f20661400ed8b7cba0312b0e2f843274f112
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e38b-handle-error-messages
---

# handle error messages



# $E38B — handle error messages

## Disassemblatura
```assembly
.E38B  8A       TXA
.E38C  30 03    BMI $E391
.E38E  4C 3A A4 JMP $A43A
.E391  4C 74 A4 JMP $A474
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e38b-handle-error-messages]]
