---
id: a717-print-tokens-routine
type: entity
title: print tokens routine
aliases:
- print tokens routine
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a717-print-tokens-routine.md
  sha256: 21c11cf2982c016a98f43ffdb406116779f2dff716db969e4dec0cdac8f0899a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a717-print-tokens-routine
---

# print tokens routine



# $A717 — print tokens routine

## Disassemblatura
```assembly
.A717  6C 06 03 JMP ($0306)   ; normally A71A
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A717**: JMP $A71A
- **$A71A**: kein Interpretercode:ausgeben
- **$A71C**: Code für Pi?
- **$A71E**: Ja: so ausgeben
- **$A720**: Hochkommamodus ?
- **$A722**: dann Zeichen so ausgeben
- **$A724**: Carry setzen (Subtraktion)
- **$A725**: Offset abziehen
- **$A727**: Code nach X
- **$A728**: Zeichenzeiger merken
- **$A72A**: Zeiger auf Befehlstabelle
- **$A72C**: erstes Befehlswort?
- **$A72D**: Ja: ausgeben
- **$A72F**: Zeiger erhöhen
- **$A730**: Offset für X-tes Befehlswort
- **$A733**: alle Zeichen bis zum letzen
- **$A735**: überlesen (Bit 7 gesetzt)
- **$A737**: Zeiger erhöhen
- **$A738**: Befehlswort aus Tabelle holen
- **$A73B**: letzter Buchstabe: fertig
- **$A73D**: Zeichen ausgeben
- **$A740**: nächsten Buchstaben ausgeben

### Marko Mäkelä (Marko Mäkelä)
- **$A717**: normally A71A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a717-print-tokens-routine]]
