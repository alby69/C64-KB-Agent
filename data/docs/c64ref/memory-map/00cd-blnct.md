---
title: Cursor timing countdown
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
  address: $00CD
  symbol: BLNCT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Count to toggle cur
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle dient als Zähler
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Timer: Countdown to Toggle Cursor'
  - name: Memory Map
    author: Jim Butterfield
    description: Cursor timing countdown
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The interrupt routine that blinks the cursor uses this location to
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Das Blinken des Cursors besorgt die Interrupt-Routine. 60mal in jeder
      Sekunde
  - name: 64map
    author: —
    description: 'Timer: Count down for Cursor blink toggle'
---

# BLNCT — Cursor timing countdown ($00CD)

## Panoramica
Il registro o area di memoria BLNCT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CD` (`205` decimale)
- **Range**: `$00CD`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Count to toggle cur

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle dient als Zähler
für die Cursor-Blinkphase. Wenn der
Wert 20 in dieser Speicherzelle
abgezählt ist, wird der Cursor eingeschaltet.

### C64 Programmer's Reference Guide (Commodore)
Timer: Countdown to Toggle Cursor

### Memory Map (Jim Butterfield)
Cursor timing countdown

### Mapping the Commodore 64 (Sheldon Leemon)
The interrupt routine that blinks the cursor uses this location to
tell when it's time for a blink.  First the number 20 is put here, and
every jiffy (1/60 second) the value here is decreased by one, until it
reaches zero.  Then the cursor is blinked, the number 20 is put back
here, and the cycle starts all over again.  Thus, under normal
circumstances, the cursor blinks three times per second.

### Reference (Joe Forster / STA)
Values:

* $00, 0: Must change cursor phase.
* $01-$14, 1-20: Delay.

### 64'er Magazin (64'er)
Das Blinken des Cursors besorgt die Interrupt-Routine. 60mal in jeder Sekunde
unterbricht sie den normalen Programmablauf. Während dieser Zeit führt sie
mehrere »Haushalt«-Arbeiten durch. So wird hier die Tastatur abgefragt und das
Cursorblinken gesteuert.

Dazu wird die Zahl 20 in die Speicherzelle 205 geschrieben und bei jeder
Unterbrechung dann um 1 reduziert. Wenn die Zahl in 205 den Wert 0 erreicht
hat, wird der Cursor eingeschaltet. Nach Adam Riese erfolgt das also 60/20 =
3mal pro Sekunde. Im Texteinschub Nr. 22 »Cursor-Spiele oder der INPUT-Befehl
einmal etwas anders« wird mit diesem Zähler für die Blinkfrequenz
experimentiert.

### 64map (—)
Timer: Count down for Cursor blink toggle

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*