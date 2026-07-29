---
title: Screen line link table
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
  address: $00D9
  address_end: $00F2
  symbol: LDTB1
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Line flags+endspace
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Alle 25 Speicherzellen enthalten
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Screen Line Link Table / Editor Temps
  - name: Memory Map
    author: Jim Butterfield
    description: Screen line link table
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This table contains 25 entries, one for each row of the screen
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese 26 Speicherzellen enthalten Angaben für jede Zeile des Bildschirms.
      Jedes
  - name: 64map
    author: —
    description: Screen Line link Table/Editor temporaries. High Byte of Line Screen
      Memory Lo...
---

# LDTB1 — Screen line link table ($00D9)

## Panoramica
Il registro o area di memoria LDTB1 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D9` (`217` decimale)
- **Range**: `$00D9`-`$00F2`
- **Dimensione**: `26 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Line flags+endspace

### Commodore-64-intern-Buch (Commodore)
Alle 25 Speicherzellen enthalten
Informationen über die Zeilen des
Bildschirms.

### C64 Programmer's Reference Guide (Commodore)
Screen Line Link Table / Editor Temps

### Memory Map (Jim Butterfield)
Screen line link table

### Mapping the Commodore 64 (Sheldon Leemon)
This table contains 25 entries, one for each row of the screen
display.  Each entry has two functions.  Bits 0-3 indicate on which of
the four pages of screen memory  the first byte of memory for that row
is located.  This is used in calculating the pointer to the starting
address of a screen line at 209 ($00D1).

While earlier PETs used one table for the low bytes of screen rows and
another for the high bytes, this is not possible on the 64, where
screen memory is not fixed in any one spot.  Therefore, the Operating
System uses a table of low bytes at 60656 ($ECF0), but calculates the
high byte by adding the value of the starting page of screen memory
held in 648 ($0288) to the displacement page held here.

The other function of this table is to establish the makeup of logical
lines on the screen.  While each screen line is only 40 characters
long, BASIC allows the entry of program lines that contain up to 80
characters.  Therefore, some method must be used to determine which
pairs of physical lines are linked into a longer logical line, so that
this longer logical line may be edited as a unit.

The high bit of each byte here is used as a flag by the screen editor.
That bit is set (leaving the value of the byte over 128 ($80)) when a
line is the first or only physical line in a logical line.  The high
bit is reset to 0 only when a line is the second half of a logical
line.

### Reference (Joe Forster / STA)
Values:

* $00-$7F: Pointer high byte.
* $80-$FF: No pointer, line is an extension of previous line on screen.

### 64'er Magazin (64'er)
Diese 26 Speicherzellen enthalten Angaben für jede Zeile des Bildschirms. Jedes
dieser Bytes hat zwei Funktionen.

Die ersten 4 Bit, also Bit 0 bis 3, geben an, in welchem Speicherblock, man
sagt auch »page« dazu, das erste Byte der betreffenden Bildschirmzeile sich
befindet. Diese Angabe wird zur Berechnung des Zeigers in der Speicherzelle 209
(siehe dort) verwendet. Sie ist in dieser Form notwendig, da der
Bildschirmspeicher beim C 64 überall in den Arbeitsspeicher gelegt werden kann.
Um die Position eines Zeichens oder besser gesagt eines Bytes davon im
Bildschirmspeicher genau positionieren zu können, braucht das Betriebssystem
noch die genaue Lage innerhalb des Speicherblocks. Das Low-Byte dieser Zahl
steht in einer Tabelle ab Speicherzelle 60656 (60952 beim VC 20). Das High-Byte
wird berechnet, und zwar durch Addition des Wertes der Speicherzelle 648 mit
dem Wert der ersten 4 Bit in Tabelle 217 bis 242. Der Wert in Zelle 648 gibt
die Anfangsadresse des Bildschirmspeichers an.

Der zweite Teil jedes Bytes in der Tabelle 217 bis 242 hat eine andere
Funktion. Wie im Texteinschub 23 beschrieben ist, kann eine logische Zeile aus
ein oder zwei (beim VC 20 sogar bis zu 4) echten Zeilen bestehen. Das
Betriebssystem braucht daher eine Angabe, welche echten Zeilen zu einer
logischen Zeile verbunden sind. Dieses Verbinden heißt auf englisch »link«,
daher heißt der Speicherbereich 217 bis 242 »Link-Tabelle«. Diese oberen 4 Bit
zeigen mit irgendeinem Wert über 0 an, daß die betreffende echte Zeile die
erste oder einzige einer logischen Zeile ist. Sind die 4 Bit alle 0, dann ist
sie eine 2., 3. und 4. Zeile der logischen Zeile.

### 64map (—)
Screen Line link Table/Editor temporaries. High Byte of Line Screen Memory Location

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*