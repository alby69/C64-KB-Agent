---
title: assign to string
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
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
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $A9D9
  address_end: $A9DE
  symbol: assign-to-string
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A9D9**: Akku vom Stapel holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $A9D9 — assign to string

## Disassemblatura
```assembly
.A9D9  68       PLA
.A9DA  A4 4A    LDY $4A
.A9DC  C0 BF    CPY #$BF
.A9DE  D0 4C    BNE $AA2C
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A9D9**: Akku vom Stapel holen
- **$A9DA**: Variablenadresse (HIGH) holen
- **$A9DC**: ist Variable TI$?
- **$A9DE**: nein: $AA2C
- **$A9E0**: FRESTR
- **$A9E3**: Stringlänge gleich 6
- **$A9E5**: nein: 'illegal quantity'
- **$A9E7**: Wert holen
- **$A9E9**: und damit FAC
- **$A9EB**: initialisieren
- **$A9ED**: (Akku, Vorzeichen und Zeiger)
- **$A9EF**: prüft nächstes Z. auf Ziffer
- **$A9F2**: FAC = FAC * 10
- **$A9F5**: Stellenzähler erhöhen
- **$A9F7**: und ins Y-Reg. bringen
- **$A9F9**: prüft nächstes Z. auf Ziffer
- **$A9FC**: FAC nach ARG kopieren
- **$A9FF**: FAC gleich 0?
- **$AA00**: ja: $AA07
- **$AA02**: Exponent von FAC erhöhen
- **$AA03**: (FAC *2) und in den Akku
- **$AA04**: FAC = FAC + ARG
- **$AA07**: Stellenzähler
- **$AA09**: erhöhen
- **$AA0A**: schon 6 Stellen?
- **$AA0C**: nein: nächstes Zeichen
- **$AA0E**: FAC = FAC * 10
- **$AA11**: FAC rechtsbündig machen
- **$AA14**: Werte für
- **$AA16**: eingegebene Uhrzeit
- **$AA18**: holen und
- **$AA1A**: Time setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*