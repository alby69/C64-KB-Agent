---
title: assign to float
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $A9D6
  address_end: $A9D6
  symbol: assign-to-float
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A9D6**: FAC nach Variable bringen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $A9D6 — assign to float

## Disassemblatura
```assembly
.A9D6  4C D0 BB JMP $BBD0
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A9D6**: FAC nach Variable bringen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*