---
title: find a file
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f30f-in-x
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F30F
  address_end: $F313
  symbol: find-a-file
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F30F**: clear A'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F30F**: Status'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F311**: clear STATUS'
---

# $F30F — find a file

## Disassemblatura
```assembly
.F30F  A9 00    LDA #$00   ; clear A
.F311  85 90    STA $90   ; clear the serial status byte
.F313  8A       TXA   ; copy the logical file number to A
```


## Commenti

### Original Disassembly (—)
- **$F30F**: clear A
- **$F311**: clear the serial status byte
- **$F313**: copy the logical file number to A

### Commodore-64-intern-Buch (Commodore)
- **$F30F**: Status
- **$F311**: löschen
- **$F313**: Filenummer in Akku schieben
- **$F314**: Anzahl der offenen Files
- **$F316**: Anzahl um eins verringern
- **$F317**: verzweige wenn kein File offen oder Filenummer nicht gefunden
- **$F319**: sucht Eintrag in Tabelle
- **$F31C**: verzweige wenn noch nicht gefunden
- **$F31E**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F311**: clear STATUS
- **$F313**: file number to search for
- **$F314**: LDTND, number of open files
- **$F317**: end of table, return
- **$F319**: compare file number with LAT, table of open files
- **$F31C**: not equal, try next
- **$F31E**: back with Z flag set

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*