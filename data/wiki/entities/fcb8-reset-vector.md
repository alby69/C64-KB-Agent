---
id: fcb8-reset-vector
type: entity
title: reset vector
aliases:
- reset vector
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fcb8-reset-vector.md
  sha256: ea5982d12de7fba831f461a415aaa1bf34ff2c10c56647ba3b4e775f69059210
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fcb8-reset-vector
---

# reset vector



# $FCB8 — reset vector

## Disassemblatura
```assembly
.FCB8  20 93 FC JSR $FC93   ; restore everything for STOP
.FCBB  F0 97    BEQ $FC54   ; restore registers and exit interrupt, branch always
```


## Commenti

### Original Disassembly (—)
- **$FCB8**: restore everything for STOP
- **$FCBB**: restore registers and exit interrupt, branch always

### Commodore-64-intern-Buch (Commodore)
- **$FCB8**: IRQ auf Standard
- **$FCBB**: Abschluß IRQ
- **$FCBD**: IRQ-Vektor
- **$FCC0**: aus Tabelle setzen
- **$FCC3**: lRQ-Vektor
- **$FCC6**: aus Tabelle setzen
- **$FCC9**: Rücksprung
- **$FCCA**: Rekorder-
- **$FCCC**: motor
- **$FCCE**: ausschalten
- **$FCD0**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fcb8-reset-vector]]
