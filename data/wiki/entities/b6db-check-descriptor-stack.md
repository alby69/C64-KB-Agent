---
id: b6db-check-descriptor-stack
type: entity
title: check descriptor stack
aliases:
- check descriptor stack
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b6db-check-descriptor-stack.md
  sha256: 7906fbe688720ee8da2be8353d46cb9d23fab7f1e88459079ba27e76ccef6352
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b6db-check-descriptor-stack
---

# check descriptor stack



# $B6DB — check descriptor stack

## Disassemblatura
```assembly
.B6DB  C4 18    CPY $18
.B6DD  D0 0C    BNE $B6EB
.B6DF  C5 17    CMP $17
.B6E1  D0 08    BNE $B6EB
.B6E3  85 16    STA $16
.B6E5  E9 03    SBC #$03
.B6E7  85 17    STA $17
.B6E9  A0 00    LDY #$00
.B6EB  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B6DB**: Zeiger auf Stringdescriptor
- **$B6DD**: identisch mit $18, nicht? RTS
- **$B6DF**: identisch mit 17
- **$B6E1**: wenn nicht, dann RTS
- **$B6E3**: Zeiger nach $16 speichern
- **$B6E5**: Von Adresse $17
- **$B6E7**: 3 abziehen
- **$B6E9**: Zähler auf Null
- **$B6EB**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b6db-check-descriptor-stack]]
