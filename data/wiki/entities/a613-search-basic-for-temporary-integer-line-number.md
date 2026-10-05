---
id: a613-search-basic-for-temporary-integer-line-number
type: entity
title: search BASIC for temporary integer line number
aliases:
- search BASIC for temporary integer line number
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a613-search-basic-for-temporary-integer-line-number.md
  sha256: eeaa82dd5fb429c4fa22306ecc5e74f75999833c7ccb3d30d7b01a461e164d67
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a613-search-basic-for-temporary-integer-line-number
---

# search BASIC for temporary integer line number



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

## References
- Source: [[src-a613-search-basic-for-temporary-integer-line-number]]
