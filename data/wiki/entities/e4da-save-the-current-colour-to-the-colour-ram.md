---
id: e4da-save-the-current-colour-to-the-colour-ram
type: entity
title: save the current colour to the colour RAM
aliases:
- save the current colour to the colour RAM
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4da-save-the-current-colour-to-the-colour-ram.md
  sha256: f4caabfae879acab5dbd1d9d82a7acd3ad667576f5e01a509a89f409b1303bc6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e4da-save-the-current-colour-to-the-colour-ram
---

# save the current colour to the colour RAM



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

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E4DA**: get COLOR
- **$E4DD**: and store in current screen position

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e4da-save-the-current-colour-to-the-colour-ram]]
