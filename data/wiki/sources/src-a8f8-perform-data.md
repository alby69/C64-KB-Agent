---
id: src-a8f8-perform-data
type: source
title: 'Source Summary: perform DATA'
aliases:
- perform DATA
- a8f8-perform-data.md
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
links_out: []
---

# Source Summary: perform DATA

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a8f8-perform-data.md`
**SHA256**: `25c67c623702bf186cdc0eac66e7db10f79dc1cfb47afaa1602eeebfaec2329c`

## Summary



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
- **$A903**: P...
