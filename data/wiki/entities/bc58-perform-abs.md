---
id: bc58-perform-abs
type: entity
title: perform ABS()
aliases:
- perform ABS()
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc58-perform-abs.md
  sha256: 8021c57d5971f8734b44eb741bf1a07891f9750d6993de8eb08a4fc94b4ce5b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bc58-perform-abs
---

# perform ABS()



# $BC58 — perform ABS()

## Disassemblatura
```assembly
.BC58  46 66    LSR $66   ; clear FAC1 sign, put zero in b7
.BC5A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BC58**: clear FAC1 sign, put zero in b7

### Commodore-64-intern-Buch (Commodore)
- **$BC58**: Vorzeichenbit löschen
- **$BC5A**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC58**: CHANGE SIGN TO +

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bc58-perform-abs]]
