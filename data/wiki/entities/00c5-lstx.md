---
id: 00c5-lstx
type: entity
title: Last key pressed
aliases:
- Last key pressed
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00c5-lstx.md
  sha256: 53bb3f8a2dba0bf8f3c7d647d021d075a8eea300ca08b2517441917c12afe0c2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00c5-lstx
---

# Last key pressed



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

## References
- Source: [[src-00c5-lstx]]
