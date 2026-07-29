---
title: Current device
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
  address: $00BA
  symbol: FA
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Current file primary addr
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Entsprechend ist auch in dieser
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Current Device Number
  - name: Memory Map
    author: Jim Butterfield
    description: Current device
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location holds the number of the device that is currently being
  - name: Reference
    author: Joe Forster / STA
    description: Device number of current file
  - name: 64'er Magazin
    author: 64'er
    description: Jedes an den Computer anschließbare Gerät hat eine eigene Nummer,
      die zusammen
  - name: 64map
    author: —
    description: Current File - First Address (Device number). OPEN LA,FA,SA;  OPEN
      1,8,15,"I0...
---

# FA — Current device ($00BA)

## Panoramica
Il registro o area di memoria FA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BA` (`186` decimale)
- **Range**: `$00BA`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Current file primary addr

### Commodore-64-intern-Buch (Commodore)
Entsprechend ist auch in dieser
Speicherzelle die Gerätenummer zu
finden.

### C64 Programmer's Reference Guide (Commodore)
Current Device Number

### Memory Map (Jim Butterfield)
Current device

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the number of the device that is currently being
used.  Device number assignments are as follows:

|      |                    |
|------|--------------------|
| 0    | Keyboard           |
| 1    | Datasette Recorder |
| 2    | RS-232/User Port   |
| 3    | Screen             |
| 4-5  | Printer            |
| 8-11 | Disk               |

### Reference (Joe Forster / STA)
Device number of current file

### 64'er Magazin (64'er)
Jedes an den Computer anschließbare Gerät hat eine eigene Nummer, die zusammen
mit den Ein-/Ausgabe-Befehlen LOAD, SAVE, VERIFY und OPEN angegeben werden muß.
Wird keine Nummer angegeben, nimmt der Computer automatisch an, daß die
Datasette gemeint ist.

Alle von Commodore vorgegebenen Geräte-Nummern sind in der folgenden Tabelle 5 aufgelistet.

| Geräte-Nummer | angesprochenes Gerät             |
|---------------|----------------------------------|
| 0             | Tastatur                         |
| 1             | Datasette                        |
| 2             | RS232- (User-Port) Schnittstelle |
| 3             | Bildschirm                       |
| 4             | Drucker (normal)                 |
| 5             | Drucker (zusätzlich)             |
| 8             | Disketten-Laufwerk Nr. 0         |
| 9             | Disketten-Laufwerk Nr. 1         |
| 10, 11        | weitere Disketten-Laufwerke      |

Tabelle 5. Von Commodore vorgegebene Geräte-Nummern

Die normale Geräte-Nummer eines Druckers ist 4, die eines Disketten-Laufwerks
8. Die zusätzlichen Nummern müssen gesondert am betreffenden Gerät eingestellt
werden.

Nach der Ausführung eines der oben genannten Befehle steht die entsprechende
Geräte-Nummer in der Speicherzelle 186, aus der sie mit PEEK(186) ausgelesen
werden kann.

### 64map (—)
Current File - First Address (Device number). OPEN LA,FA,SA;  OPEN 1,8,15,"I0":CLOSE 1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*