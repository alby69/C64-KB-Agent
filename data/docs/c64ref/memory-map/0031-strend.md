---
title: 'Pointer : End-of-Arrays'
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
  address: $0031
  address_end: $0032
  symbol: STREND
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Increased whenever a new array
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese beiden Speicherzellen zeigen auf
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Pointer End of BASIC Arrays (+1)
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pointer : End-of-Arrays'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the address of the end of BASIC array storage
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to end of array variable area
  - name: 64'er Magazin
    author: 64'er
    description: Der Inhalt dieser Speicherzellen zeigt auf die Adresse, wo der Speicherbereich
  - name: 64map
    author: —
    description: 'Pointer: End of BASIC Arrays + 1'
---

# STREND — Pointer : End-of-Arrays ($0031)

## Panoramica
Il registro o area di memoria STREND è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0031` (`49` decimale)
- **Range**: `$0031`-`$0032`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Increased whenever a new array
or simple variable is encountered.
set to [VARTAB] by "CLEARC".

### Commodore-64-intern-Buch (Commodore)
Diese beiden Speicherzellen zeigen auf
das Ende der Arrays. Zu beachten ist,
daß die Zeichenketten rückwärts
gespeichert werden.

### C64 Programmer's Reference Guide (Commodore)
Pointer End of BASIC Arrays (+1)

### Memory Map (Jim Butterfield)
Pointer : End-of-Arrays

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address of the end of BASIC array storage
space and the start of free RAM.  Since string text starts at the top
of memory and builds downwards, this location can also be thought of
as the last possible address of the string storage area.  Defining new
variables pushes this pointer upward, toward the last string text.

If a string for which space is being allocated would cross over this
boundary into the array storage area, garbage collection is performed,
and if there still is not enough room, an OUT OF MEMORY error occurs.
FRE performs garbage collection, and returns the difference between
the addresses pointed to here and the address of the end of string
text storage pointed to by location 51 ($0033).

### Reference (Joe Forster / STA)
Pointer to end of array variable area

### 64'er Magazin (64'er)
Der Inhalt dieser Speicherzellen zeigt auf die Adresse, wo der Speicherbereich
für Felder auf· hört. Wie aus Bild 5 hervorgeht, werden die Zeichenketten vorn
Ende des verfügbaren RAM· Speichers rückwärts gespeichert. Man kann also auch
sagen, daß der Zeiger in 49 und 50 die letzte mögliche Adresse für
Zeichenketten angibt. Wenn in einem Programm neue Variablen definiert werden,
rutscht diese Adresse weiter nach oben und nähert sich dem Ende der
Zeichenketten, die durch den Zeiger in 51 und 52 angegeben wird.

Wenn sich die Speicherbereiche der Felder und Zeichenketten berühren, bleibt
der Computer stehen und führt die »Garbage Collection« (Müllabfuhr) durch - ein
Prozeß, in dem nicht mehr gebrauchte Zeichenketten entfernt und der
Zeichenketten-Speicher reduziert wird. Ist danach immer noch kein Platz, wird
OUT OF MEMORY gegeben.

Der Befehl FRE löst immer eine solche Garbage Collection aus und gibt dann die
Differenz zwischen den Adressen in den Zeigern 49 und 50 und 51 und 52 als
verbleibenden, noch verfügbaren, Speicherbereich aus.

### 64map (—)
Pointer: End of BASIC Arrays + 1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*