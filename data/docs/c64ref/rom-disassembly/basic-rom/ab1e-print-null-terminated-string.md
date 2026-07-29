---
title: print null terminated string
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
- ab1e-string-ausgeben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AB1E
  address_end: $AB1E
  symbol: print-null-terminated-string
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AB1E**: print " terminated string to utility pointer'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AB1E**: Stringparameter holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AB1E**: MAKE (Y,A) PRINTABLE'
---

# $AB1E — print null terminated string

## Disassemblatura
```assembly
.AB1E  20 87 B4 JSR $B487   ; print " terminated string to utility pointer
```


## Commenti

### Original Disassembly (—)
- **$AB1E**: print " terminated string to utility pointer

### Commodore-64-intern-Buch (Commodore)
- **$AB1E**: Stringparameter holen
- **$AB21**: FRESTR
- **$AB24**: Stringlänge
- **$AB25**: Zeiger für Stringausgabe
- **$AB27**: erhöhen
- **$AB28**: vermindern
- **$AB29**: String zu Ende?
- **$AB2B**: Zeichen des Strings
- **$AB2D**: ausgeben
- **$AB30**: Zeiger erhöhen
- **$AB31**: 'CR' carriage return?
- **$AB33**: nein: weiter
- **$AB35**: Fehler ! Test auf LF-Ausgabe
- **$AB38**: und weitermachen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AB1E**: MAKE (Y,A) PRINTABLE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*