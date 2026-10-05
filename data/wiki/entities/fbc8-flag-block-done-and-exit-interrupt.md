---
id: fbc8-flag-block-done-and-exit-interrupt
type: entity
title: flag block done and exit interrupt
aliases:
- flag block done and exit interrupt
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fbc8-flag-block-done-and-exit-interrupt.md
  sha256: f0734f25bf8e0de731c6058123458a28102ab085c4fb6ea61c62122cb31ab499
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fbc8-flag-block-done-and-exit-interrupt
---

# flag block done and exit interrupt



# $FBC8 — flag block done and exit interrupt

## Disassemblatura
```assembly
.FBC8  38       SEC   ; set carry flag
.FBC9  66 B6    ROR $B6   ; set buffer address high byte negative, flag all sync, data and checksum bytes written
.FBCB  30 3C    BMI $FC09   ; restore registers and exit interrupt, branch always
```


## Commenti

### Original Disassembly (—)
- **$FBC8**: set carry flag
- **$FBC9**: set buffer address high byte negative, flag all sync, data and checksum bytes written
- **$FBCB**: restore registers and exit interrupt, branch always

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fbc8-flag-block-done-and-exit-interrupt]]
