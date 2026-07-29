---
title: Input device, normally 0
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
  address: $0099
  symbol: DFLTN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Default input device #'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In dieser Speicherzelle wird
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Default Input Device (0)
  - name: Memory Map
    author: Jim Butterfield
    description: Input device, normally 0
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The default value of this location is 0, which designates the keyboard
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $00, keyboard.'
  - name: 64'er Magazin
    author: 64'er
    description: Das Betriebssystem verwendet diese Speicherzelle, um festzuhalten,
      welches
  - name: 64map
    author: —
    description: Default Input Device (0)
---

# DFLTN — Input device, normally 0 ($0099)

## Panoramica
Il registro o area di memoria DFLTN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0099` (`153` decimale)
- **Range**: `$0099`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Default input device #

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle wird
festgehalten, welches Gerät zur
Eingabe verwendet werden soll.
Die Nummern sind folgendermaßen
festgelegt:

|      |                     |
|------|---------------------|
| 0    | Tastatur            |
| 1    | Datasette           |
| 2    | RS232 und User-Port |
| 3    | Bildschirm          |
| 4-5  | Drucker             |
| 8-11 | Laufwerke           |

### C64 Programmer's Reference Guide (Commodore)
Default Input Device (0)

### Memory Map (Jim Butterfield)
Input device, normally 0

### Mapping the Commodore 64 (Sheldon Leemon)
The default value of this location is 0, which designates the keyboard
as the current input device.  That value can be changed by the Kernal
routine CHKIN (61966, $F20E), which uses this location to store the
device number of the device whose file it defines as an input channel.

BASIC calls CHKIN whenever the command INPUT# or GET# is executed, but
clears the channel after the input operation has been completed.

### Reference (Joe Forster / STA)
Default: $00, keyboard.

### 64'er Magazin (64'er)
Das Betriebssystem verwendet diese Speicherzelle, um festzuhalten, welches
Gerät zur Eingabe verwendet werden soll.

Die Nummern sind wie folgt festgelegt:

|      |                   |
|------|-------------------|
| 0    | Tastatur          |
| 1    | Datasette         |
| 2    | RS232 (User-)Port |
| 3    | Bildschirm        |
| 4,5  | Drucker           |
| 8-11 | Floppy-Laufwerke  |

Nach dem Einschalten oder nach RESET des Computers steht in 153 eine 0
(Tastatur). Nach jedem Einsatz eines anderen Gerätes wird diese Speicherzelle
wieder auf 0 gesetzt, so daß wir immer die Tastatur zur Verfügung haben.

Für Maschinenprogrammierer ist diese Adresse sicherlich wertvoll. Die Routine,
welche die Eingabegeräte festlegt, sobald der Befehl INPUT# beziehungsweise
GET# ausgeführt wird, heißt CHKIN und beginnt beim C 64 ab Adresse 61966
($F20E), beim VC 20 ab 62151 ($F2C7).

Für Basic-Programmierer habe ich in der Literatur nur eine Anwendung gefunden,
und die wurde bereits bei der Besprechung der Speicherzelle 19 angekündigt.

Es ist dies eine MERGE-Routine. Leider funktioniert dieses Verfahren nicht bei
dem 1541-Floppy-Laufwerk. Erfunden wurde die Routine von Brad Templeton und ist
von Jim Butterfield unter dem Namen »Magic Merge« für den VC 20/

C 64 adaptiert worden. Ich gebe zu, in der Zwischenzeit sind noch andere,
vielleicht auch kürzere MERGE-Routinen veröffentlicht worden. Aber diese hier
verwendet gleich drei interessante Ingredienzen, nämlich die Speicherzellen 19
und 153 und außerdem die sogenannte »Dynamische Tastenabfrage«. Wer die
letztere nicht kennt, sollte sich zum Verständnis den Texteinschub Nr. 15
gleichen Namens ansehen.

Ein MERGE (deutsch: zusammenführen, verschmelzen) besteht darin, ein auf Band
gespeichertes Programm zu einem im Computer stehenden anderen Programm so
dazuzuladen, daß dieses nicht überschrieben, sondern ergänzt wird. Wichtig ist
dabei, daß das Programm vom Band höhere Zeilennummern hat als das Programm im
Computer. Außerdem muß das Programm auf dem Band als Datei gespeichert sein.
Das wird so erreicht:

1. Programm eintippen
2. Direkt eingeben:

    OPEN 1,1,1, "Name*: CMD1:LIST

3. Erst wenn READY kommt, direkt eingeben PRINT #1:CLOSE1

Damit ist das Programm auf dem Band gespeichert. Nun kommt der eigentliche
MERGE-Vorgang.

4. Es steht ein Programm im Computer
5. Band mit dem Programm »Name« einlegen
6. Direkt eingeben:

    POKE 19,1:OPEN 1

7. Sobald READY erscheint, Bildschirm löschen (SHIFT-CLR).
8. Dreimal Cursor-Down
9. Direkt eingeben:

    PRINT CHR$(19):POKE 198,1:POKE 631,13:POKE 153,1

10. Das Band beendet den Ladevorgang mit einer Fehlermeldung, die wir
    ignorieren.
11. Nach CLOSE 1 sind beide Programme zusammengefügt.

Wie gesagt, Schritt 6 verwendet Zeile 19 (bitte dort nachlesen), Schritte 8 und
9 sind die »Dynamische Tastenabfrage«, und Schritt 9 verwendet zusätzlich die
hier zur Diskussion stehende Speicherzelle 153, um die Datasette als
Eingabegerät zu definieren.

### 64map (—)
Default Input Device (0)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*