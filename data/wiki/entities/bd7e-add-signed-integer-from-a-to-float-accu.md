---
id: bd7e-add-signed-integer-from-a-to-float-accu
type: entity
title: add signed integer from A to float accu
aliases:
- add signed integer from A to float accu
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bd7e-add-signed-integer-from-a-to-float-accu.md
  sha256: 3568a987ba25175fd7f8f5520c97c605b781460e303107ab7bdc0abbf4ffe433
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bd7e-add-signed-integer-from-a-to-float-accu
---

# add signed integer from A to float accu



# $BD7E — add signed integer from A to float accu

## Disassemblatura
```assembly
.BD7E  48       PHA
.BD7F  20 0C BC JSR $BC0C
.BD82  68       PLA
.BD83  20 3C BC JSR $BC3C
.BD86  A5 6E    LDA $6E
.BD88  45 66    EOR $66
.BD8A  85 6F    STA $6F
.BD8C  A6 61    LDX $61
.BD8E  4C 6A B8 JMP $B86A
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BD7E**: SAVE ADDEND
- **$BD82**: GET ADDEND AGAIN
- **$BD83**: CONVERT TO FP VALUE IN FAC
- **$BD8C**: TO SIGNAL IF FAC=0
- **$BD8E**: PERFORM THE ADDITION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bd7e-add-signed-integer-from-a-to-float-accu]]
