---
title: print tokens routine
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a717-umwandlen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $A717
  address_end: $A717
  symbol: print-tokens-routine
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A717**: JMP $A71A'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A717**: normally A71A'
---

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