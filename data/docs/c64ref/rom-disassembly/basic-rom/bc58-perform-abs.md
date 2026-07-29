---
title: perform ABS()
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bc58-basic-funktion-abs
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BC58
  address_end: $BC5A
  symbol: perform-abs
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC58**: clear FAC1 sign, put zero in b7'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BC58**: Vorzeichenbit löschen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC58**: CHANGE SIGN TO +'
---

# $BC58 — perform ABS()

## Disassemblatura
```assembly
.BC58  46 66    LSR $66   ; clear FAC1 sign, put zero in b7
.BC5A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BC58**: clear FAC1 sign, put zero in b7

### Commodore-64-intern-Buch (Commodore)
- **$BC58**: Vorzeichenbit löschen
- **$BC5A**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC58**: CHANGE SIGN TO +

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*