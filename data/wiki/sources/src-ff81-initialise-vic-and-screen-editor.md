---
id: src-ff81-initialise-vic-and-screen-editor
type: source
title: 'Source Summary: initialise VIC and screen editor'
aliases:
- initialise VIC and screen editor
- ff81-initialise-vic-and-screen-editor.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff81-initialise-vic-and-screen-editor.md
  sha256: 667f1ecc24523e38a684e88c6ccb33c594df8ac57269ed24f845163b32e59a4e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise VIC and screen editor

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ff81-initialise-vic-and-screen-editor.md`
**SHA256**: `667f1ecc24523e38a684e88c6ccb33c594df8ac57269ed24f845163b32e59a4e`

## Summary



# $FF81 — initialise VIC and screen editor

## Disassemblatura
```assembly
.FF81  4C 5B FF JMP $FF5B   ; initialise VIC and screen editor
```


## Commenti

### Original Disassembly (—)
- **$FF81**: initialise VIC and screen editor

### Commodore-64-intern-Buch (Commodore)
- **$FF81**: Video-Reset
- **$FF84**: CIAs initialisieren
- **$FF87**: RAM löschen bzw. testen
- **$FF8A**: I/O initialisieren
- **$FF8D**: I/O Vektoren initialisieren
- **$FF90**: Status setzen
- **$FF93**: Sekundäradresse ...
