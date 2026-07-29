---
title: check value to be string
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
  address: $AD8F
  address_end: $AD8F
  symbol: check-value-to-be-string
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AD8F**: Flag für Test auf String'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $AD8F — check value to be string

## Disassemblatura
```assembly
.AD8F  38       SEC
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AD8F**: Flag für Test auf String
- **$AD90**: Typflag testen
- **$AD92**: gesetzt: $AD97
- **$AD94**: C=1: 'TYPE MISMATCH'
- **$AD96**: Rücksprung
- **$AD97**: C=1: RTS
- **$AD99**: Nummer für 'TYPE MISMATCH'
- **$AD9B**: Fehlermeldung ausgeben

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*