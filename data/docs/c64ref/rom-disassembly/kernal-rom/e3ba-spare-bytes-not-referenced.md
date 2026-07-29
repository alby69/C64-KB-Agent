---
title: spare bytes, not referenced
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e3ba-anfangswert-fr-rnd-funktion
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  - marko_mäkelä.txt
  - bob_sander-cederlof.txt
  - magnus_nyman.txt
  address: $E3BA
  address_end: $E3BA
  symbol: spare-bytes-not-referenced
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E3BA**: 0.811635157'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E3BA**: .811635157'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E3BA**: APPROX. = .811635157'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

# $E3BA — spare bytes, not referenced

## Disassemblatura
```assembly
.E3BA  80 4F C7 52 58   ; 0.811635157
```


## Commenti

### Original Disassembly (—)
- **$E3BA**: 0.811635157

### Commodore-64-intern-Buch (Commodore)
- **$E3BA**: .811635157

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E3BA**: APPROX. = .811635157
- **$E3D8**: POINT "USR" TO ILLEGAL QUANTITY
- **$E3DA**: ERROR, UNTIL USER SETS IT UP

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*