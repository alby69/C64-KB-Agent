---
title: return the x,y organization of the screen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e505-spalten
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E505
  address_end: $E509
  symbol: return-the-xy-organization-of-the-screen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E505**: get the x size'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E505**: 40 Spalten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E505**: 40 columns'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E505**: 40 columns'
---

# $E505 — return the x,y organization of the screen

## Disassemblatura
```assembly
.E505  A2 28    LDX #$28   ; get the x size
.E507  A0 19    LDY #$19   ; get the y size
.E509  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E505**: get the x size
- **$E507**: get the y size

### Commodore-64-intern-Buch (Commodore)
- **$E505**: 40 Spalten
- **$E507**: 25 Zeilen
- **$E509**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E505**: 40 columns
- **$E507**: 25 rows

### Magnus Nyman (Magnus Nyman)
- **$E505**: 40 columns
- **$E507**: 25 rows

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*