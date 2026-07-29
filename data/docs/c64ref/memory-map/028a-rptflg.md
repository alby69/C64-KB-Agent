---
title: Repeat all keys
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
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
  address: $028A
  symbol: RPTFLG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Key repeat flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In dieser Speicherzelle wird dem
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: REPEAT Key Used, $80 = Repeat'
  - name: Memory Map
    author: Jim Butterfield
    description: Repeat all keys
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The flag at this location is used to determine whether to continue
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64'er Magazin
    author: 64'er
    description: Normalerweise steht in dieser Speicherzelle eine 0. Das bedeutet,
      daß die
  - name: 64map
    author: —
    description: 'Flag: Repeat keys; $00 = Cursors, INST/DEL & Space repeat, $40 no
      Keys repeat...'
---

# RPTFLG — Repeat all keys ($028A)

## Panoramica
Il registro o area di memoria RPTFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$028A` (`650` decimale)
- **Range**: `$028A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Key repeat flag

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle wird dem
Betriebssystem angegeben, welche Tasten
eine Repeat-Funktion haben und welche
nicht:

|     |                                           |
|-----|-------------------------------------------|
|   0 | nur Cursor-, Insert/Delete- und Leertaste |
|  64 | keine Taste                               |
| 128 | alle Tasten                               |

### C64 Programmer's Reference Guide (Commodore)
Flag: REPEAT Key Used, $80 = Repeat

### Memory Map (Jim Butterfield)
Repeat all keys

### Mapping the Commodore 64 (Sheldon Leemon)
The flag at this location is used to determine whether to continue
printing a character as long as its key is held down, or whether to
wait until the key is let up before allowing it to be printed again.
The default value here is 0, which allows only the cursor movement
keys, insert/delete key, and the space bar to repeat.

POKEing this location with 128 ($80) will make all keys repeating,
while a value of 64 ($40) will disable all keys from repeating.

### Reference (Joe Forster / STA)
Bits:

* Bits #6-#7:
    * %00 = Only cursor up/down, cursor left/right, Insert/Delete and Space repeat
    * %01 = No key repeats
    * %1x = All keys repeat.

### 64'er Magazin (64'er)
Normalerweise steht in dieser Speicherzelle eine 0. Das bedeutet, daß die
Funktion der Cursor-Tasten, der Leertaste und der INST/DEL-Taste wiederholt
wird, solange die entsprechende Taste gedrückt wird.

Durch Verändern der Zahl in der Speicherzelle 650 kann diese Wiederholfunktion
sowohl auf alle Tasten ausgedehnt als auch für alle Tasten gesperrt werden.

    POKE 650,0

ist der Normalzustand, Wiederholfunktion für Cursor-, Leer- und INST/DEL-Taste

    POKE 650,64

schaltet Wiederholfunktion für alle Tasten aus.

    POKE 650,128

erweitert Wiederholfunktion auf alle Tasten.

### 64map (—)
Flag: Repeat keys; $00 = Cursors, INST/DEL & Space repeat, $40 no Keys repeat, $80 all Keys repeat ($00)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*