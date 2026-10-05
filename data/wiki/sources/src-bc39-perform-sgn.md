---
id: src-bc39-perform-sgn
type: source
title: 'Source Summary: perform SGN()'
aliases:
- perform SGN()
- bc39-perform-sgn.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc39-perform-sgn.md
  sha256: bf7cb277434eebcffa803786ae7224587e549eeb0281b614480f5cb6550db8f5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform SGN()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc39-perform-sgn.md`
**SHA256**: `bf7cb277434eebcffa803786ae7224587e549eeb0281b614480f5cb6550db8f5`

## Summary



# $BC39 — perform SGN()

## Disassemblatura
```assembly
.BC39  20 2B BC JSR $BC2B   ; get FAC1 sign, return A = $FF -ve, A = $01 +ve
```


## Commenti

### Original Disassembly (—)
- **$BC39**: get FAC1 sign, return A = $FF -ve, A = $01 +ve

### Commodore-64-intern-Buch (Commodore)
- **$BC39**: Vorzeichen holen
- **$BC3C**: und in FAC speichern
- **$BC3E**: $63
- **$BC40**: löschen
- **$BC42**: Exponent
- **$BC44**: Vorzeichen
- **$BC46**: invertieren
- **$BC48**: und nach links rollen
- **$BC...
