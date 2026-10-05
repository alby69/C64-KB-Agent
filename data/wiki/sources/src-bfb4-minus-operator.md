---
id: src-bfb4-minus-operator
type: source
title: 'Source Summary: minus operator'
aliases:
- minus operator
- bfb4-minus-operator.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bfb4-minus-operator.md
  sha256: 171e44f04bdf2e0bd4c413b5e51884b9588cd9dcc967657b764193fec4e71804
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: minus operator

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bfb4-minus-operator.md`
**SHA256**: `171e44f04bdf2e0bd4c413b5e51884b9588cd9dcc967657b764193fec4e71804`

## Summary



# $BFB4 — minus operator

## Disassemblatura
```assembly
.BFB4  A5 61    LDA $61
.BFB6  F0 06    BEQ $BFBE
.BFB8  A5 66    LDA $66
.BFBA  49 FF    EOR #$FF
.BFBC  85 66    STA $66
.BFBE  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$BFB4**: Exponent
- **$BFB6**: Zahl gleich null, dann fertig
- **$BFB8**: Vorzeichen
- **$BFBA**: invertieren und
- **$BFBC**: speichern
- **$BFBE**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sa...
