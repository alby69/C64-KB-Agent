---
title: Repeat speed counter
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
  address: $028B
  symbol: KOUNT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle dient als Zähler,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Repeat Speed Counter
  - name: Memory Map
    author: Jim Butterfield
    description: Repeat speed counter
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used as a delay counter to determine how long to
      wait
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Das Betriebssystem verwendet diese Speicherzelle als Zähler, der
      die
  - name: 64map
    author: —
    description: 'Repeat Key: Speed Counter ($04)'
---

# KOUNT — Repeat speed counter ($028B)

## Panoramica
Il registro o area di memoria KOUNT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$028B` (`651` decimale)
- **Range**: `$028B`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle dient als Zähler,
die die Repeat-Geschwindigkeit
festlegt.

### C64 Programmer's Reference Guide (Commodore)
Repeat Speed Counter

### Memory Map (Jim Butterfield)
Repeat speed counter

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used as a delay counter to determine how long to wait
while a key is being held down until the next repeat printing of that
key.

The value here starts at 6.  If location 652 ($028C) contains a 0, the
value in this location is counted down once every 1/60 second, so long
as the same key is held down.  When this counter gets to 0, and if the
repeat flag at 650 ($028A) allows that key to repeat, its ASCII
equivalent will once again be placed in the keyboard buffer.  A value
of 4 is then placed in location 651, allowing subsequent repeats to
occur at a rate of 15 per second.

### Reference (Joe Forster / STA)
Values:

* $00, 0: Must repeat key.
* $01-$04, 1-4: Delay repetition.

### 64'er Magazin (64'er)
Das Betriebssystem verwendet diese Speicherzelle als Zähler, der die
Geschwindigkeit bestimmt, mit der eine Taste wiederholt wird, wenn sie länger
gedrückt wird. Voraussetzung ist die durch Zelle 650 festgelegte
Wiederholbarkeit der Taste. Am Anfang steht in der Zelle 651 die Zahl 6. Sobald
eine wiederholbare Taste gedrückt wird, zählt das Betriebssystem diese Zahl
alle 0,0167 Sekunden (60mal in der Sekunde) um 1 zurück, bis die Zahl 1
erreicht ist. Dann erst wird das Zeichen der gedrückten Taste wieder auf den
Bildschirm gedruckt oder ihre Funktion wiederholt.

Bei jedem folgenden Lauf steht in Zelle 651 die Zahl 4. Entsprechend verkürzt
sich der Zählvorgang.

Am schnellsten würde die Wiederholung natürlich mit dem Wert 1 in der
Speicherzelle 651 sein. Von Basic aus mit POKE 651,1 geht das leider nicht.

Im Texteinschub Nr. 27 »Turbo-Tasten« wird ein Maschinenprogramm beschrieben,
welches dies kann.

### 64map (—)
Repeat Key: Speed Counter ($04)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*