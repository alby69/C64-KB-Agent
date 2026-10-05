---
id: eb64-select-keyboard-table
type: entity
title: select keyboard table
aliases:
- select keyboard table
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eb64-select-keyboard-table.md
  sha256: c84e46dfc004a7ea9f8b276da9df77723a246de628bfbf7d83eb3f38abbda015
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-eb64-select-keyboard-table
---

# select keyboard table



# $EB64 — select keyboard table

## Disassemblatura
```assembly
.EB64  0A       ASL
.EB65  C9 08    CMP #$08
.EB67  90 02    BCC $EB6B
.EB69  A9 06    LDA #$06
.EB6B  AA       TAX
.EB6C  BD 79 EB LDA $EB79,X
.EB6F  85 F5    STA $F5
.EB71  BD 7A EB LDA $EB7A,X
.EB74  85 F6    STA $F6
.EB76  4C E0 EA JMP $EAE0
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-eb64-select-keyboard-table]]
