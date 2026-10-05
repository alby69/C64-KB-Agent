---
id: src-e4da-save-the-current-colour-to-the-colour-ram
type: source
title: 'Source Summary: save the current colour to the colour RAM'
aliases:
- save the current colour to the colour RAM
- e4da-save-the-current-colour-to-the-colour-ram.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4da-save-the-current-colour-to-the-colour-ram.md
  sha256: f4caabfae879acab5dbd1d9d82a7acd3ad667576f5e01a509a89f409b1303bc6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save the current colour to the colour RAM

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e4da-save-the-current-colour-to-the-colour-ram.md`
**SHA256**: `f4caabfae879acab5dbd1d9d82a7acd3ad667576f5e01a509a89f409b1303bc6`

## Summary



# $E4DA — save the current colour to the colour RAM

## Disassemblatura
```assembly
.E4DA  AD 21 D0 LDA $D021   ; get the current colour code
.E4DD  91 F3    STA ($F3),Y   ; save it to the colour RAM
.E4DF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E4DA**: get the current colour code
- **$E4DD**: save it to the colour RAM

### Commodore-64-intern-Buch (Commodore)
- **$E4DA**: Farbe holen
- **$E4DD**: ins Farbram schreiben
- **$E4DF**: Rücksprung

### Marko Mäkelä (Marko...
