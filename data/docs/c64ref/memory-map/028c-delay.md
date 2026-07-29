---
title: Repeat delay counter
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
  address: $028C
  symbol: DELAY
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird angegeben, wie lange eine
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Repeat Delay Counter
  - name: Memory Map
    author: Jim Butterfield
    description: Repeat delay counter
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used as a delay counter to determine how long a
      key
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird vom Betriebssystem als Zähler verwendet,
      der festlegt,
  - name: 64map
    author: —
    description: 'Repeat Key: First repeat delay Counter ($10)'
---

# DELAY — Repeat delay counter ($028C)

## Panoramica
Il registro o area di memoria DELAY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$028C` (`652` decimale)
- **Range**: `$028C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier wird angegeben, wie lange eine
Taste gedrückt sein muß, bis die
Repeat-Funktion einsetzt.

### C64 Programmer's Reference Guide (Commodore)
Repeat Delay Counter

### Memory Map (Jim Butterfield)
Repeat delay counter

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used as a delay counter to determine how long a key
must be held down before the entry of that key should be repeated.

The initial value of 16 is counted down every 1/60 second, as long as
the same key remains pressed.  When the value gets to 0, location 651
($028B) is counted down from 6, and the key is repeated when the value
there reaches 0.  Thus a total of 22/60, or approximately 1/3, second
will elapse before the first repeat of a key.  The value here will be
held to 0 after the first repeat, so that subsequent keystroke
repetitions occur much more quickly.

### Reference (Joe Forster / STA)
Values:

* $00, 0: Must start repeat sequence.
* $01-$10, 1-16: Delay repeat sequence.

### 64'er Magazin (64'er)
Diese Speicherzelle wird vom Betriebssystem als Zähler verwendet, der festlegt,
wie lange eine wiederholbare Taste gedrückt sein muß, bis die Wiederholfunktion
einsetzt.

Am Anfang steht in der Zelle 652 die Zahl 16. Diese Zahl wird alle 0,0167
Sekunden um 1 reduziert, bis die Zahl 0 erreicht ist. Dann wird das Zeichen der
Taste auf den Bildschirm gebracht oder ihre Funktion wiederholt. Anschließend
wird die Zahl 4 in die Speicherzelle 651 geschrieben (siehe dort), während die
Zelle 652 so lange auf 0 stehen bleibt, bis eine andere Taste gedrückt wird.
Wie diese anfängliche Verzögerung reduziert werden kann, steht im Texteinschub
Nr. 27 »Turbo-Tasten«.

### 64map (—)
Repeat Key: First repeat delay Counter ($10)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*