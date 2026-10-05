---
id: bf71-perform-sqr
type: entity
title: perform SQR()
aliases:
- perform SQR()
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bf71-perform-sqr.md
  sha256: 8163b0f4700bca9fca41547a87bc809ba05db9f45061460822a231c685a7021e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bf71-perform-sqr
---

# perform SQR()



# $BF71 — perform SQR()

## Disassemblatura
```assembly
.BF71  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.BF74  A9 11    LDA #$11   ; set 0.5 pointer low address
.BF76  A0 BF    LDY #$BF   ; set 0.5 pointer high address
.BF78  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
```


## Commenti

### Original Disassembly (—)
- **$BF71**: round and copy FAC1 to FAC2
- **$BF74**: set 0.5 pointer low address
- **$BF76**: set 0.5 pointer high address
- **$BF78**: unpack memory (AY) into FAC1

### Commodore-64-intern-Buch (Commodore)
- **$BF71**: FAC runden und nach ARG
- **$BF74**: Zeiger auf
- **$BF76**: Konstante 0.5

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BF74**: SET UP POWER OF 0.5

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bf71-perform-sqr]]
