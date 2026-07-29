---
title: perform DATA
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
- 00d7-data
- a8f8-basic-befehl-data
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A8F8
  address_end: $A8F8
  symbol: perform-data
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A8F8**: scan for next BASIC statement ([:] or [EOL])'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A8F8**: nächstes Statement suchen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A8F8**: MOVE TO NEXT STATEMENT'
---

# $A8F8 — perform DATA

## Disassemblatura
```assembly
.A8F8  20 06 A9 JSR $A906   ; scan for next BASIC statement ([:] or [EOL])
```


## Commenti

### Original Disassembly (—)
- **$A8F8**: scan for next BASIC statement ([:] or [EOL])

### Commodore-64-intern-Buch (Commodore)
- **$A8F8**: nächstes Statement suchen
- **$A8FB**: Offset
- **$A8FC**: Carry löschen (Addition)
- **$A8FD**: Programmzeiger addieren
- **$A8FF**: und wieder abspeichern
- **$A901**: Verminderung übergehen
- **$A903**: Programmzeiger vermindern
- **$A905**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A8F8**: MOVE TO NEXT STATEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*