---
id: f30f-find-a-file
type: entity
title: find a file
aliases:
- find a file
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f30f-find-a-file.md
  sha256: e11736fd00c672ef2de209deeabda9d0510ca5eeb2867fb61ae3a3b5ce1c6a8f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f30f-find-a-file
---

# find a file



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

## References
- Source: [[src-f30f-find-a-file]]
