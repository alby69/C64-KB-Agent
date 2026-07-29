---
title: 0 = flash cursor
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
  address: $00CC
  symbol: BLNSW
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Cursor blink enab
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Der Cursor wird ausgeschaltet, wenn
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Cursor Blink enable: 0 = Flash Cursor'
  - name: Memory Map
    author: Jim Butterfield
    description: 0 = flash cursor
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: When this flag is set to a nonzero value, it indicates to the routine
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Ein Wert größer 0 in dieser Speicherzelle schaltet das Blinken des
      Cursors ab.
  - name: 64map
    author: —
    description: 'Flag: Cursor blink; $00 = Enabled, $01 = Disabled'
---

# BLNSW — 0 = flash cursor ($00CC)

## Panoramica
Il registro o area di memoria BLNSW è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CC` (`204` decimale)
- **Range**: `$00CC`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cursor blink enab

### Commodore-64-intern-Buch (Commodore)
Der Cursor wird ausgeschaltet, wenn
in dieser Speicherzelle ein größerer
Wert als Null steht.

### C64 Programmer's Reference Guide (Commodore)
Cursor Blink enable: 0 = Flash Cursor

### Memory Map (Jim Butterfield)
0 = flash cursor

### Mapping the Commodore 64 (Sheldon Leemon)
When this flag is set to a nonzero value, it indicates to the routine
that normally flashes the cursor not to do so.  The cursor blink is
turned off when there are characters in the keyboard buffer, or when
the program is running.

You can use this location to turn the cursor on during a program (for
a series of GET operations, for example, to show the user that input
is expected) by using the statement POKE 204,0.

### Reference (Joe Forster / STA)
Values:

* $00: Cursor is on.
* $01-$FF: Cursor is off.

### 64'er Magazin (64'er)
Ein Wert größer 0 in dieser Speicherzelle schaltet das Blinken des Cursors ab.
Diese Abschaltung erfolgt durch das Betriebssystem immer dann, wenn sich
Zeichen im Tastaturpuffer befinden und wenn ein Programm ausgeführt wird.

Im folgenden Beispiel einer Eingabe mit dem GET-Befehl, bei dem bekannterweise
der Cursor nicht blinkt, wird demonstriert, daß durch POKE 204,0 der Cursor
trotzdem blinkt. Das kann für selbstgeschriebene Eingabe-Routinen interessant
sein.

    10 PRINT"JA/NEIN?";
    20 POKE 204,0
    30 GET A$: IF A$=""THEN 30
    40 PRINT A$

Umgekehrt kann man durch POKE 204,1 das Blinken des Cursors abschalten. Es
bleibt dabei allerdings dem Zufall überlassen, ob er in der Einoder Aus-Phase
abgeschaltet wird. Wenn Sie Pech haben, dann bleibt der Cursor bewegungslos
stehen.

### 64map (—)
Flag: Cursor blink; $00 = Enabled, $01 = Disabled

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*