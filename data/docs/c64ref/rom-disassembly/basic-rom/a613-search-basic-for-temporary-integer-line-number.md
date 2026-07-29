---
title: search BASIC for temporary integer line number
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
- a613-programmzeile-berechnen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A613
  address_end: $A615
  symbol: search-basic-for-temporary-integer-line-number
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A613**: get start of memory low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A613**: Zeiger auf BASIC-'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A613**: SEARCH FROM BEGINNING OF PROGRAM'
---

# $A613 — search BASIC for temporary integer line number

## Disassemblatura
```assembly
.A613  A5 2B    LDA $2B   ; get start of memory low byte
.A615  A6 2C    LDX $2C   ; get start of memory high byte
```


## Commenti

### Original Disassembly (—)
- **$A613**: get start of memory low byte
- **$A615**: get start of memory high byte

### Commodore-64-intern-Buch (Commodore)
- **$A613**: Zeiger auf BASIC-
- **$A615**: Programmstart laden
- **$A617**: Zähler setzen
- **$A619**: BASIC-Programmstart als
- **$A61B**: Zeiger nach $5F/60
- **$A61D**: Link-Adresse holen (HIGH)
- **$A61F**: gleich null: dann Ende
- **$A621**: Zähler 2 mal erhöhen ( LOW-
- **$A622**: Byte übergehen)
- **$A623**: gesuchte Zeilennummer (HIGH)
- **$A625**: mit aktueller vergleichen
- **$A627**: kleiner: dann nicht gefunden
- **$A629**: gleich: Nummer LOW prüfen
- **$A62B**: Zähler um 1 vermindern
- **$A62C**: unbedingter Sprung
- **$A62E**: gesuchte Zeilennummer (LOW)
- **$A630**: Zeiger um 1 vermindern
- **$A631**: Zeilennummer LOW vergleichen
- **$A633**: kleiner: Zeile nicht gefunden
- **$A635**: oder gleich: C=1 und RTS
- **$A637**: Y-Register auf 1 setzen
- **$A638**: Adresse der nächsten Zeile
- **$A63A**: in das X-Register laden
- **$A63B**: Register vermindern (auf 0)
- **$A63C**: Link-Adresse holen (LOW)
- **$A63E**: weiter suchen
- **$A640**: Carry löschen
- **$A641**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A613**: SEARCH FROM BEGINNING OF PROGRAM
- **$A617**: SEARCH FROM (X,A)
- **$A61F**: END OF PROGRAM, AND NOT FOUND
- **$A627**: IF NOT FOUND
- **$A633**: PAST LINE, NOT FOUND
- **$A635**: IF FOUND
- **$A63E**: ALWAYS
- **$A640**: RETURN CARRY = 0

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*