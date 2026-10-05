---
id: bbd0-pack-fac1-into-variable-pointer
type: entity
title: pack FAC1 into variable pointer
aliases:
- pack FAC1 into variable pointer
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbd0-pack-fac1-into-variable-pointer.md
  sha256: cda5e9f2952f0a3a43389813dff119982fc4bd3b7edf5eb8e471d9e6c66d6363
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bbd0-pack-fac1-into-variable-pointer
---

# pack FAC1 into variable pointer



# $BBD0 — pack FAC1 into variable pointer

## Disassemblatura
```assembly
.BBD0  A6 49    LDX $49   ; get destination pointer low byte
.BBD2  A4 4A    LDY $4A   ; get destination pointer high byte
```


## Commenti

### Original Disassembly (—)
- **$BBD0**: get destination pointer low byte
- **$BBD2**: get destination pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$BBD0**: Variablenadresse
- **$BBD2**: holen
- **$BBD4**: FAC runden
- **$BBD7**: Zeiger auf
- **$BBD9**: Zieladresse
- **$BBDB**: Zähler setzen
- **$BBDD**: LOW-Byte der Mantisse
- **$BBDF**: Den
- **$BBE1**: FAC
- **$BBE2**: in
- **$BBE4**: den
- **$BBE6**: Ziel-
- **$BBE7**: bereich
- **$BBE9**: über-
- **$BBEB**: tragen
- **$BBEC**: FAC-Vorzeichen
- **$BBEE**: Die Bits 0 bis 6 setzen
- **$BBF0**: Vorzeichen auf
- **$BBF2**: Speicherformat
- **$BBF4**: bringen
- **$BBF5**: FAC-Exponent
- **$BBF7**: übertragen
- **$BBF9**: FAC-Rundungsstelle löschen
- **$BBFB**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bbd0-pack-fac1-into-variable-pointer]]
