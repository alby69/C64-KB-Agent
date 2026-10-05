---
id: src-e5ca-write-character-and-wait-for-key
type: source
title: 'Source Summary: write character and wait for key'
aliases:
- write character and wait for key
- e5ca-write-character-and-wait-for-key.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e5ca-write-character-and-wait-for-key.md
  sha256: d1bd40ec7f801131b907992ce81a7ab69ead9c6696f30eef8cca1a0394bc6b06
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: write character and wait for key

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e5ca-write-character-and-wait-for-key.md`
**SHA256**: `d1bd40ec7f801131b907992ce81a7ab69ead9c6696f30eef8cca1a0394bc6b06`

## Summary



# $E5CA — write character and wait for key

## Disassemblatura
```assembly
.E5CA  20 16 E7 JSR $E716   ; output character
```


## Commenti

### Original Disassembly (—)
- **$E5CA**: output character

### Commodore-64-intern-Buch (Commodore)
- **$E5CA**: Zeichen auf Bildschirm ausgeben
- **$E5CD**: Anzahl der
- **$E5CF**: gedrückten
- **$E5D1**: Tasten
- **$E5D4**: keine Taste gedrückt ?, dann warten
- **$E5D6**: Interrupt verhindern
- **$E5D7**: Cursor in Blink-Phase ?
- **$E5D9**: nein
- **$...
