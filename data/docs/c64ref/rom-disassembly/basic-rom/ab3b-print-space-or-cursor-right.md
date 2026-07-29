---
title: print [SPACE] or [CURSOR RIGHT]
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ab3b-bzw-cursor-right
- bit
- cursor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AB3B
  address_end: $AB44
  symbol: print-space-or-cursor-right
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AB3B**: get current I/O channel'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AB3B**: Ausgabe in File?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AB3F**: space'
---

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