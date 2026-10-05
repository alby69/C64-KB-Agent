---
id: fcbd-set-tape-vector
type: entity
title: set tape vector
aliases:
- set tape vector
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fcbd-set-tape-vector.md
  sha256: 1f2d428e4de578c40c8ee86f8cd7535392c9a8a2ab6c625453c1234ecba53e5a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fcbd-set-tape-vector
---

# set tape vector



# $FCBD — set tape vector

## Disassemblatura
```assembly
.FCBD  BD 93 FD LDA $FD93,X   ; get tape IRQ vector low byte
.FCC0  8D 14 03 STA $0314   ; set IRQ vector low byte
.FCC3  BD 94 FD LDA $FD94,X   ; get tape IRQ vector high byte
.FCC6  8D 15 03 STA $0315   ; set IRQ vector high byte
.FCC9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCBD**: get tape IRQ vector low byte
- **$FCC0**: set IRQ vector low byte
- **$FCC3**: get tape IRQ vector high byte
- **$FCC6**: set IRQ vector high byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fcbd-set-tape-vector]]
