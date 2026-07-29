---
title: Input vector
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0043
  address_end: $0044
  symbol: INPPTR
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: This remembers where input is coming from
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Der Zeiger zeigt auf die jeweilige
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: INPUT Routine'
  - name: Memory Map
    author: Jim Butterfield
    description: Input vector
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: READ, INPUT and GET all use this as a pointer to the address of the
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to input result during GET, INPUT and READ
  - name: 64'er Magazin
    author: 64'er
    description: INPUT und GET verlangen Angaben, die per Tastatur eingegeben werden.
      Tastatur-
  - name: 64map
    author: —
    description: 'Pointer: Temporary storage of Pointer during INPUT Routine'
---

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