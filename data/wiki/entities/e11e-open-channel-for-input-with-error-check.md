---
id: e11e-open-channel-for-input-with-error-check
type: entity
title: open channel for input with error check
aliases:
- open channel for input with error check
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e11e-open-channel-for-input-with-error-check.md
  sha256: 1ebc08054104d3aa92c1318c08770b914054657a309ed931e1677a2b6b981726
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e11e-open-channel-for-input-with-error-check
---

# open channel for input with error check



# $E11E — open channel for input with error check

## Disassemblatura
```assembly
.E11E  20 C6 FF JSR $FFC6   ; open channel for input
.E121  B0 D6    BCS $E0F9   ; if error go handle BASIC I/O error
.E123  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E11E**: open channel for input
- **$E121**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E11E**: Eingabegerät setzen
- **$E121**: Fehler ?
- **$E123**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E11E**: open input channel via CHKIN
- **$E121**: if carry set, handle I/O error
- **$E123**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e11e-open-channel-for-input-with-error-check]]
