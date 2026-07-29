---
title: autostart ROM signature
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
- fd10-cbm80
- fd10-rom-modul-identifizierung
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FD10
  address_end: $FD10
  symbol: autostart-rom-signature
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FD10**: ''CBM80’'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FD10**: ''CBM80’'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FD10**: CBM80'
---

# $FD10 — autostart ROM signature

## Disassemblatura
```assembly
.FD10  C3 C2 CD 38 30   ; 'CBM80’
```


## Commenti

### Original Disassembly (—)
- **$FD10**: 'CBM80’

### Commodore-64-intern-Buch (Commodore)
- **$FD10**: 'CBM80’

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FD10**: CBM80

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*