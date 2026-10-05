---
id: b8f7-clear-fac1-exponent-and-sign
type: entity
title: clear FAC1 exponent and sign
aliases:
- clear FAC1 exponent and sign
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b8f7-clear-fac1-exponent-and-sign.md
  sha256: 1293e380fee3a63479bb42f8c5cc073131ff3c9577102ceb930b71221537e91a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b8f7-clear-fac1-exponent-and-sign
---

# clear FAC1 exponent and sign



# $B8F7 — clear FAC1 exponent and sign

## Disassemblatura
```assembly
.B8F7  A9 00    LDA #$00   ; clear A
.B8F9  85 61    STA $61   ; set FAC1 exponent
```


## Commenti

### Original Disassembly (—)
- **$B8F7**: clear A
- **$B8F9**: set FAC1 exponent

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b8f7-clear-fac1-exponent-and-sign]]
