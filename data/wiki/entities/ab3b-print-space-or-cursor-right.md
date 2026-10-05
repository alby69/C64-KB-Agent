---
id: ab3b-print-space-or-cursor-right
type: entity
title: print [SPACE] or [CURSOR RIGHT]
aliases:
- print [SPACE] or [CURSOR RIGHT]
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab3b-print-space-or-cursor-right.md
  sha256: ee77d2b420e72f8935138bd8e02e4daac4562ff0dbd3b3706cd32c071311802e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ab3b-print-space-or-cursor-right
---

# print [SPACE] or [CURSOR RIGHT]



# $AB3B — print [SPACE] or [CURSOR RIGHT]

## Disassemblatura
```assembly
.AB3B  A5 13    LDA $13   ; get current I/O channel
.AB3D  F0 03    BEQ $AB42   ; if default channel go output [CURSOR RIGHT]
.AB3F  A9 20    LDA #$20   ; else output [SPACE]
.AB41  2C       .BYTE $2C   ; makes next line BIT $1DA9
.AB42  A9 1D    LDA #$1D   ; set [CURSOR RIGHT]
.AB44  2C       .BYTE $2C   ; makes next line BIT $3FA9
```


## Commenti

### Original Disassembly (—)
- **$AB3B**: get current I/O channel
- **$AB3D**: if default channel go output [CURSOR RIGHT]
- **$AB3F**: else output [SPACE]
- **$AB41**: makes next line BIT $1DA9
- **$AB42**: set [CURSOR RIGHT]
- **$AB44**: makes next line BIT $3FA9

### Commodore-64-intern-Buch (Commodore)
- **$AB3B**: Ausgabe in File?
- **$AB3D**: Bildschirm: dann Cursor right
- **$AB3F**: ' ' Leerzeichencode laden
- **$AB42**: Cursor right Code laden
- **$AB45**: '?' Fragezeichencode laden
- **$AB47**: Code ausgeben
- **$AB4A**: Flags setzen
- **$AB4C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$AB3F**: space
- **$AB42**: csr right
- **$AB45**: question mark

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ab3b-print-space-or-cursor-right]]
