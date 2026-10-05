---
id: src-ad8f-check-value-to-be-string
type: source
title: 'Source Summary: check value to be string'
aliases:
- check value to be string
- ad8f-check-value-to-be-string.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ad8f-check-value-to-be-string.md
  sha256: 9b2cc70201821ea2859f5d8ca3491e5d64e983132ba1f0d00a842e8fe7cc1e9a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check value to be string

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ad8f-check-value-to-be-string.md`
**SHA256**: `9b2cc70201821ea2859f5d8ca3491e5d64e983132ba1f0d00a842e8fe7cc1e9a`

## Summary



# $AD8F — check value to be string

## Disassemblatura
```assembly
.AD8F  38       SEC
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AD8F**: Flag für Test auf String
- **$AD90**: Typflag testen
- **$AD92**: gesetzt: $AD97
- **$AD94**: C=1: 'TYPE MISMATCH'
- **$AD96**: Rücksprung
- **$AD97**: C=1: RTS
- **$AD99**: Nummer für 'TYPE MISMATCH'
- **$AD9B**: Fehlermeldung ausgeben

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Ce...
