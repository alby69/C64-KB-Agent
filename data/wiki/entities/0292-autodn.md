---
id: 0292-autodn
type: entity
title: 0 = scroll enable
aliases:
- 0 = scroll enable
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0292-autodn.md
  sha256: 672b8527afa5839c7b64b0f75ac926e63a08bac08d52653f36f603d85ca79bb6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0292-autodn
---

# 0 = scroll enable



# AUTODN — 0 = scroll enable ($0292)

## Panoramica
Il registro o area di memoria AUTODN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0292` (`658` decimale)
- **Range**: `$0292`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Auto scroll down flag(=0 on,<>0 off)

### Commodore-64-intern-Buch (Commodore)
Wenn in dieser Speicherzelle eine 0
steht, setzt der Scroll-Vorgang ein.
Bei einem größeren Wert setzt dieser
Vorgang nicht ein.

### C64 Programmer's Reference Guide (Commodore)
Flag: Auto Scroll Down, 0 = ON

### Memory Map (Jim Butterfield)
0 = scroll enable

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to determine whether moving the cursor past the
fortieth column of a logical line will cause another physical line to
be added to the logical line.

A value of 0 enables the screen to scroll the following lines down in
order to add that line; any nonzero value will disable the scroll.
This flag is set to disable the scroll temporarily when there are
characters waiting in the keyboard buffer (these may include cursor
movement characters that would eliminate the need for a scroll).

### Reference (Joe Forster / STA)
Values:

* $00: Insertion of line before current line, current line and all lines below it must be scrolled 1 line downwards.
* $01-$FF: Bottom of screen reached, complete screen must be scrolled 1 line upwards.

### 64'er Magazin (64'er)
Die Flagge in dieser Speicherzelle legt fest, ob eine weitere echte Zeile zu
einer logischen Zeile hinzugefügt wird, sobald der Cursor über das 40ste
Zeichen der Zeile (22ste Zeichen beim VC 20) hinausläuft.

Steht in 658 eine 0, dann werden alle Zeilen hochgeschoben (man nennt das
»scrollen«), um der neuen Zeile Platz zu machen.

Wenn in der Zeile irgendein Wert größer als Null steht, unterbleibt dieses
Scrollen. Die Flagge wird immer dann auf den höheren Wert gesetzt, wenn Zeichen
im Tastaturpuffer (631 bis 640) stehen und darauf warten, am Ende des Programms
ausgedruckt beziehungsweise ausgeführt zu werden. Diese Verriegelung wird
deshalb eingesetzt, weil im Tastaturpuffer Zeichen wie zum Beispiel Cursor-
Bewegungen stehen können.

Von Basic aus kann diese Speicherzelle nicht beeinflußt werden.

### 64map (—)
Flag: Auto scroll down: $00 = Disabled ($00)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0292-autodn]]
