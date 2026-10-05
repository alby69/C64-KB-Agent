---
id: f80d-bump-tape-pointer
type: entity
title: bump tape pointer
aliases:
- bump tape pointer
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f80d-bump-tape-pointer.md
  sha256: 04c5bd39ee81f0d1ba22078a3985b4179b731aba8c494e2e169a7fa1d7681561
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f80d-bump-tape-pointer
---

# bump tape pointer



# $F80D — bump tape pointer

## Disassemblatura
```assembly
.F80D  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F810  E6 A6    INC $A6   ; increment tape buffer index
.F812  A4 A6    LDY $A6   ; get tape buffer index
.F814  C0 C0    CPY #$C0   ; compare with buffer length
.F816  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F80D**: get tape buffer start pointer in XY
- **$F810**: increment tape buffer index
- **$F812**: get tape buffer index
- **$F814**: compare with buffer length

### Commodore-64-intern-Buch (Commodore)
- **$F80D**: Bandpufferadresse holen
- **$F810**: Zeiger erhöhen
- **$F812**: und laden um
- **$F814**: mit Maximalwert (192) zu vergleichen
- **$F816**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f80d-bump-tape-pointer]]
