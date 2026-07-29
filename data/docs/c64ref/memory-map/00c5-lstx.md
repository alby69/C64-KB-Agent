---
title: Last key pressed
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
  address: $00C5
  symbol: LSTX
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Key scan index
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird die Nummer der gedrückten
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Current Key Pressed: CHR$(n) 0 = No Key'
  - name: Memory Map
    author: Jim Butterfield
    description: Last key pressed
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: During every normal IRQ interrupt this location is set with the value
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Bei der Behandlung der Speicherzelle 145 habe ich Ihnen mit Wort
      und Bild
  - name: 64map
    author: —
    description: Matrix value of last Key pressed; No Key = $40
---

# LSTX — Last key pressed ($00C5)

## Panoramica
Il registro o area di memoria LSTX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C5` (`197` decimale)
- **Range**: `$00C5`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Key scan index

### Commodore-64-intern-Buch (Commodore)
Hier wird die Nummer der gedrückten
Taste gespeichert (64= keine Taste).

### C64 Programmer's Reference Guide (Commodore)
Current Key Pressed: CHR$(n) 0 = No Key

### Memory Map (Jim Butterfield)
Last key pressed

### Mapping the Commodore 64 (Sheldon Leemon)
During every normal IRQ interrupt this location is set with the value
of the last keypress, to be used in keyboard debouncing.  The
Operating System can check if the current keypress is the same as the
last one, and will not repeat the character if it is.

The value returned here is based on the keyboard matrix values as set
forth in the explanation of location 56320 ($DC00).  The values
returned for each key pressed are shown at the entry for location 203
($00CB).

### Reference (Joe Forster / STA)
Values:

* $00-$3F: Keyboard matrix code.
* $40: No key was pressed at the time of previous check.

### 64'er Magazin (64'er)
Bei der Behandlung der Speicherzelle 145 habe ich Ihnen mit Wort und Bild
beschrieben, wie die Tasten des Computers abgefragt werden. Die dabei für jede
Taste entstehende Dualzahl wird in eine Dezimalzahl (0 bis 63) umgewandelt und
zuerst in die Speicherzellen 203 beziehungsweise 653 gebracht. Zur Umwandlung
und Abfrage der Zellen 203 und 653 bringe ich bei diesen Speicherzellen mehr
Details. Nach der Prüfung, welche Taste gedrückt worden ist, wird die Codezahl
von 203 in die Speicherzelle 197 gebracht und dort »aufgehoben«. Diese
vermeintliche Verdoppelung wird vom Betriebssystem dafür gebraucht, um zu
erkennen, ob die nächste gedrückte Taste mit der vorhergehenden identisch ist.
Ist sie identisch, dann entscheidet der Inhalt der Speicherzelle 650, ob das
Zeichen dieser Taste mehrfach ausgedruckt wird. In 650 steht die sogenannte
Wiederholfunktion. Aber ich will nicht vorgreifen. Die Codezahlen der einzelnen
Tasten werde ich bei der Besprechung der Zelle 203 auflisten.

### 64map (—)
Matrix value of last Key pressed; No Key = $40

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*