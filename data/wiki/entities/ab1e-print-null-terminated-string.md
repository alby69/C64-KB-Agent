---
id: ab1e-print-null-terminated-string
type: entity
title: print null terminated string
aliases:
- print null terminated string
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab1e-print-null-terminated-string.md
  sha256: d0aba8b25d3d3894cd138a8a38717949da47f5e820e64055e4d8439bf82e202b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ab1e-print-null-terminated-string
---

# print null terminated string



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

## References
- Source: [[src-ab1e-print-null-terminated-string]]
