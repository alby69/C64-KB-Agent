---
id: ea1c-save-the-character-and-colour-to-the-screen-the-cursor
type: entity
title: save the character and colour to the screen @ the cursor
aliases:
- save the character and colour to the screen @ the cursor
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ea1c-save-the-character-and-colour-to-the-screen-the-cursor.md
  sha256: c3c47b9716987731f5edbee5f9fdc363d576f1e55c89b55312b1f628e1c3a937
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ea1c-save-the-character-and-colour-to-the-screen-the-cursor
---

# save the character and colour to the screen @ the cursor



# $EA1C — save the character and colour to the screen @ the cursor

## Disassemblatura
```assembly
.EA1C  A4 D3    LDY $D3   ; get the cursor column
.EA1E  91 D1    STA ($D1),Y   ; save the character from current screen line
.EA20  8A       TXA   ; copy the colour to A
.EA21  91 F3    STA ($F3),Y   ; save to colour RAM
.EA23  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EA1C**: get the cursor column
- **$EA1E**: save the character from current screen line
- **$EA20**: copy the colour to A
- **$EA21**: save to colour RAM

### Commodore-64-intern-Buch (Commodore)
- **$EA1C**: Spaltenposition
- **$EA1E**: Zeichen in Akku auf Bildschirm
- **$EA20**: Farb-Code von x in Akku
- **$EA21**: in Farb-RAM schreiben
- **$EA23**: Rücksprung zum Hauptprogramm

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ea1c-save-the-character-and-colour-to-the-screen-the-cursor]]
