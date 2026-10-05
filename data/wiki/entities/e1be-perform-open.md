---
id: e1be-perform-open
type: entity
title: perform OPEN
aliases:
- perform OPEN
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e1be-perform-open.md
  sha256: 3c4838be0dc57f792a47e96db6a9674fb8bd6305497d6f0857e3a4488ac04445
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e1be-perform-open
---

# perform OPEN



# $E1BE — perform OPEN

## Disassemblatura
```assembly
.E1BE  20 19 E2 JSR $E219   ; get parameters for OPEN/CLOSE
.E1C1  20 C0 FF JSR $FFC0   ; open a logical file
.E1C4  B0 0B    BCS $E1D1   ; branch if error
.E1C6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E1BE**: get parameters for OPEN/CLOSE
- **$E1C1**: open a logical file
- **$E1C4**: branch if error

### Commodore-64-intern-Buch (Commodore)
- **$E1BE**: Parameter holen
- **$E1C1**: OPEN-Routine
- **$E1C4**: Fehler ?
- **$E1C6**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E1BE**: get parameters from text
- **$E1C1**: execute OPEN
- **$E1C4**: if carry set, handle error

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e1be-perform-open]]
