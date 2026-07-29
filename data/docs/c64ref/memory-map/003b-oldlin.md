---
title: Previous Basic line number
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
  address: $003B
  address_end: $003C
  symbol: OLDLIN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Set up by ^C,"STOP"
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Falls eine Unterbrechung des
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Previous BASIC Line Number
  - name: Memory Map
    author: Jim Butterfield
    description: Previous Basic line number
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: When program execution ends, the last line number executed is stored
  - name: Reference
    author: Joe Forster / STA
    description: Current BASIC line number for CONT
  - name: 64'er Magazin
    author: 64'er
    description: Immer dann, wenn ein Programmablauf durch die Befehle END oder STOP
      oder aber
  - name: 64map
    author: —
    description: Previous BASIC Line number
---

# OLDLIN — Previous Basic line number ($003B)

## Panoramica
Il registro o area di memoria OLDLIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$003B` (`59` decimale)
- **Range**: `$003B`-`$003C`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Set up by ^C,"STOP"
or "END" in a program.

### Commodore-64-intern-Buch (Commodore)
Falls eine Unterbrechung des
Programmablaufs durch den Befehl STOP
oder über die STOP-Taste erfolgt,
wird in den Speicheradressen $003B-$003C
die Zeilennummer gespeichert, die
gerade abgearbeitet wurde.

### C64 Programmer's Reference Guide (Commodore)
Previous BASIC Line Number

### Memory Map (Jim Butterfield)
Previous Basic line number

### Mapping the Commodore 64 (Sheldon Leemon)
When program execution ends, the last line number executed is stored
here, and restored to location 57 ($0039) by CONT.

### Reference (Joe Forster / STA)
Current BASIC line number for CONT

### 64'er Magazin (64'er)
Immer dann, wenn ein Programmablauf durch die Befehle END oder STOP oder aber
mit der STOP-Taste abgebrochen wird, wird die Nummer der gerade ausgeführten
Programmzeile nach 59 und 60 gebracht und bleibt dort solange, bis eine neue
Unterbrechung erfolgt.

Das läßt sich am besten mit der STOP-Taste und nachfolgendem CONT zeigen.
Nehmen Sie bitte dazu das kleine Demo-Programm der Zellen 57 und 58 und ändern
Sie alle PEEK-Adressen in 59 und 60 um. Fügen Sie außerdem noch eine Zeile 50
hinzu:

    50 GOTO 10

Den dadurch erzeugten kontinuierlichen Laufdes Programms bremsen Sie dann mit
der STOP-Taste und lassen ihn danach mit CONT weiterlaufen.

Auf der rechten Seite erscheint jetzt die Zeilennummer, bei der das Programm
vorher unterbrochen worden ist.

### 64map (—)
Previous BASIC Line number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*