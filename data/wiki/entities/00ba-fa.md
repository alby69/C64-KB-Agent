---
id: 00ba-fa
type: entity
title: Current device
aliases:
- Current device
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00ba-fa.md
  sha256: 59425ea15544fc20026641f77e436d94ee4475c9c5ca9eaf361bb995615d44b0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00ba-fa
---

# Current device



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

## References
- Source: [[src-00ba-fa]]
