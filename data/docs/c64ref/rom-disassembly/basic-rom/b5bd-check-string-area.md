---
title: check string area
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
  address: $B5BD
  address_end: $B5C6
  symbol: check-string-area
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B5BD**: Variablenname erstes Zeichen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B5BD — check string area

## Disassemblatura
```assembly
.B5BD  B1 22    LDA ($22),Y
.B5BF  30 35    BMI $B5F6
.B5C1  C8       INY
.B5C2  B1 22    LDA ($22),Y
.B5C4  10 30    BPL $B5F6
.B5C6  C8       INY
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B5BD**: Variablenname erstes Zeichen
- **$B5BF**: Integer o. Funktion ?
- **$B5C1**: Zähler erhöhen
- **$B5C2**: Variablenname zweites Zeichen
- **$B5C4**: wenn Real, dann $B5F6
- **$B5C6**: Zähler erhöhen
- **$B5C7**: holt Stringlänge
- **$B5C9**: wenn Stringlänge=0,dann $B5F6
- **$B5CB**: Zähler erhöhen
- **$B5CC**: holt Startadresse des Strings
- **$B5CE**: schiebt ins X-Reg
- **$B5CF**: Zähler erhöhen
- **$B5D0**: holt Sringzeiger
- **$B5D2**: Vergleich mit $34
- **$B5D4**: wenn gleich, dann $B5DC
- **$B5D6**: wenn größer, dann $B5F6
- **$B5D8**: mit $33 vergleichen
- **$B5DA**: wenn gleich, dann $B5F6
- **$B5DC**: Vergleich mit $60
- **$B5DE**: wenn gleich, dann $B5F6
- **$B5E0**: wenn größer, dann $B5E6
- **$B5E2**: Vergleich mit $5F
- **$B5E4**: wenn gleich, dann $B5F6
- **$B5E6**: Startadresse des
- **$B5E8**: Strings speichern
- **$B5EA**: Stringdescriptor
- **$B5EC**: laden
- **$B5EE**: und
- **$B5F0**: speichern
- **$B5F2**: Tabellen Schrittweite laden
- **$B5F4**: und speichern
- **$B5F6**: und zum
- **$B5F8**: Suchzeiger
- **$B5F9**: addieren
- **$B5FB**: und wieder
- **$B5FD**: speichern
- **$B5FF**: Zeiger erhöhen
- **$B601**: und laden
- **$B603**: Zähler löschen
- **$B605**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*