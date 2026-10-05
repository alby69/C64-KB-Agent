---
id: 028a-rptflg
type: entity
title: Repeat all keys
aliases:
- Repeat all keys
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/028a-rptflg.md
  sha256: 7939ce98035d78c84a90cc573e0813fc68e6576cbca15410a3066850fd30c94b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-028a-rptflg
---

# Repeat all keys



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

## References
- Source: [[src-028a-rptflg]]
