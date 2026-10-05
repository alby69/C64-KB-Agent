---
id: 004b-vartxt
type: entity
title: Y-save; op-save; Basic pointer save
aliases:
- Y-save; op-save; Basic pointer save
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/004b-vartxt.md
  sha256: a911d8261bf466ab8e7390360e621165dbbfdb295bebbad4bbfc9b071b8bb230
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-004b-vartxt
---

# Y-save; op-save; Basic pointer save



# VARTXT — Y-save; op-save; Basic pointer save ($004B)

## Panoramica
Il registro o area di memoria VARTXT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$004B` (`75` decimale)
- **Range**: `$004B`-`$004C`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to current op's entry in "OPTAB"

### Original Source Comments (Microsoft/Commodore)
Pointer into list of variables

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzellen dienen als
Zwischenspeicher für mathematische
Operationen. Außerdem werden die
Speicherzellen auch noch vom
READ-Befehl als Zwischenspeicher
verwendet.

### C64 Programmer's Reference Guide (Commodore)
Temp Pointer / Data Area

### C64 Programmer's Reference Guide (Commodore)
Temporary storage for TXTPTR during READ, INPUT and GET

### Memory Map (Jim Butterfield)
Y-save; op-save; Basic pointer save

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used during the evaluation of mathematical
expressions to hold the displacement of the current math operator in
an operator table.  It is also used as a save area for the pointer to
the address of program text which is currently being read.

### Reference (Joe Forster / STA)
Temporary area for saving original pointer to current BASIC instruction during GET, INPUT and READ

### 64'er Magazin (64'er)
Während der Auswertung eines mathematischen Ausdrucks durch die Routine FRMEVL
des Basic-Übersetzers, wird der Platz des betroffenen mathematischen Operators
in einer Tabelle, hier in 75 und 76, zwischengespeichert. Dieser Platz wird
dabei als Abstand zum Beginn der Tabelle dargestellt. Außerdem verwendet der
READ-Befehl diese Adressen als Zwischenspeicher für einen Programmzeiger. Die
Speicherzeilen 75 und 76 sind in Basic nicht verwendbar.

### 64map (—)
Temporary storage for TXTPTR during READ, INPUT and GET

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-004b-vartxt]]
