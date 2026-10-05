---
id: 0043-inpptr
type: entity
title: Input vector
aliases:
- Input vector
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0043-inpptr.md
  sha256: 2b2699e2485d3de4b4246f1ce8f8bad7b1d4a9f37afdd2dc7de3830da1aa0659
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0043-inpptr
---

# Input vector



# INPPTR — Input vector ($0043)

## Panoramica
Il registro o area di memoria INPPTR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0043` (`67` decimale)
- **Range**: `$0043`-`$0044`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
This remembers where input is coming from

### Commodore-64-intern-Buch (Commodore)
Der Zeiger zeigt auf die jeweilige
Adresse in diesem Eingabepufferspeicher.

### C64 Programmer's Reference Guide (Commodore)
Vector: INPUT Routine

### Memory Map (Jim Butterfield)
Input vector

### Mapping the Commodore 64 (Sheldon Leemon)
READ, INPUT and GET all use this as a pointer to the address of the
source of incoming data, such as DATA statements, or the text input
buffer at 512 ($0200).

### Reference (Joe Forster / STA)
Pointer to input result during GET, INPUT and READ

### 64'er Magazin (64'er)
INPUT und GET verlangen Angaben, die per Tastatur eingegeben werden. Tastatur-
Eingaben im direkten Modus, also wenn kein Programm läuft, werden im Eingabe-
Pufferspeicher des Editors (der Teil des Betriebssystems, welcher für die
Zeilendarstellung auf dem Bildschirm verantwortlich ist) ab Speicherzelle 512
bis 600 zwischengespeichert.

Der Zeiger in 67 und 68 zeigt auf die jeweilige Adresse in diesem Eingabe-
Pufferspeicher. Bei READ ist 67 und 68 identisch mit 65 und 66. Der Inhalt
dieser Speicherzellen kann mit PEEK ausgelesen werden.

### 64map (—)
Pointer: Temporary storage of Pointer during INPUT Routine

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0043-inpptr]]
