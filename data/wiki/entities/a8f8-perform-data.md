---
id: a8f8-perform-data
type: entity
title: perform DATA
aliases:
- perform DATA
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a8f8-perform-data.md
  sha256: 25c67c623702bf186cdc0eac66e7db10f79dc1cfb47afaa1602eeebfaec2329c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a8f8-perform-data
---

# perform DATA



# $A8F8 — perform DATA

## Disassemblatura
```assembly
.A8F8  20 06 A9 JSR $A906   ; scan for next BASIC statement ([:] or [EOL])
```


## Commenti

### Original Disassembly (—)
- **$A8F8**: scan for next BASIC statement ([:] or [EOL])

### Commodore-64-intern-Buch (Commodore)
- **$A8F8**: nächstes Statement suchen
- **$A8FB**: Offset
- **$A8FC**: Carry löschen (Addition)
- **$A8FD**: Programmzeiger addieren
- **$A8FF**: und wieder abspeichern
- **$A901**: Verminderung übergehen
- **$A903**: Programmzeiger vermindern
- **$A905**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A8F8**: MOVE TO NEXT STATEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a8f8-perform-data]]
