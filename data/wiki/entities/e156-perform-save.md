---
id: e156-perform-save
type: entity
title: perform SAVE
aliases:
- perform SAVE
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e156-perform-save.md
  sha256: 75408926bb50ba113f520421f56358e5cd5e3046989411b95f6c3140a86da574
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e156-perform-save
---

# perform SAVE



# $E156 — perform SAVE

## Disassemblatura
```assembly
.E156  20 D4 E1 JSR $E1D4   ; get parameters for LOAD/SAVE
.E159  A6 2D    LDX $2D   ; get start of variables low byte
.E15B  A4 2E    LDY $2E   ; get start of variables high byte
.E15D  A9 2B    LDA #$2B   ; index to start of program memory
.E15F  20 D8 FF JSR $FFD8   ; save RAM to device, A = index to start address, XY = end address low/high
.E162  B0 95    BCS $E0F9   ; if error go handle BASIC I/O error
.E164  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E156**: get parameters for LOAD/SAVE
- **$E159**: get start of variables low byte
- **$E15B**: get start of variables high byte
- **$E15D**: index to start of program memory
- **$E15F**: save RAM to device, A = index to start address, XY = end address low/high
- **$E162**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E156**: Parameter (Filenamen, Prim, und Sek. Adresse)
- **$E159**: Endadresse gleich
- **$E15B**: BASIC-Rücksprung
- **$E15D**: Startadresse gleich Zeiger auf BASIC Anfang
- **$E15F**: Save-Routine
- **$E162**: Fehler ?
- **$E164**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E156**: get SAVE parameters from text
- **$E159**: VARTAB, start of variables
- **$E15D**: <TXTTAB, start of BASIC text
- **$E15F**: execute SAVE
- **$E162**: if carry is set, handle I/O errors

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e156-perform-save]]
