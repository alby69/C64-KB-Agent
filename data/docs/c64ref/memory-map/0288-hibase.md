---
title: Screen memory page
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
  address: $0288
  symbol: HIBASE
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Base location of screen (top)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieses HIGH-Byte gibt dem Betriebssystem an,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Top of Screen Memory (Page)
  - name: Memory Map
    author: Jim Butterfield
    description: Screen memory page
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location contains the value used by the Operating System routines
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $04, $0400, 1024.'
  - name: 64'er Magazin
    author: 64'er
    description: In dieser Speicherzelle steht eine Zahl, die als High-Byte dem Betriebssystem
  - name: 64map
    author: —
    description: High Byte of Screen Memory Address ($04)
---

# HIBASE — Screen memory page ($0288)

## Panoramica
Il registro o area di memoria HIBASE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0288` (`648` decimale)
- **Range**: `$0288`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Base location of screen (top)

### Commodore-64-intern-Buch (Commodore)
Dieses HIGH-Byte gibt dem Betriebssystem an,
ab welcher Adresse das Video-RAM zu finden
ist.

### C64 Programmer's Reference Guide (Commodore)
Top of Screen Memory (Page)

### Memory Map (Jim Butterfield)
Screen memory page

### Mapping the Commodore 64 (Sheldon Leemon)
This location contains the value used by the Operating System routines
that print to the screen as the base address for screen RAM.  The top
of screen memory can be found by multiplying this location by 256.
The default value for screen RAM is set on power-up to location 1024
($0400), and this location therefore usually contains a 4.

Screen display memory on the Commodore 64 can be moved to start on any
1K boundary (location evenly divisible by 1024).  This is done by
manipulating the VIC-II chip memory bank select at location 56576
($DD00).

It is important to note, however, that while any area may be
displayed, the Operating System will look here to find out where it
should PRINT characters.  Therefore, if you change the screen location
by altering the contents of one of the two addresses listed above, the
Operating System will still not know where to PRINT characters unless
you also change this address as well.  The result will be that
characters entered from the keyboard or PRINTed will not appear on the
screen.

Examples of how to properly relocate the screen can be found at the
entries for location 53272 ($D018) and 43 ($002B).

Since the PRINT command in essence just POKEs a lot of values to
screen and color memory, by changing this pointer you can print a
string of characters to memory locations other than screen RAM.  For
example, you could PRINT a sprite shape to memory without having to
READ a lot of DATA statements.  The program below PRINTs different
sprite shapes into the sprite data area:

    10 SP=53248:POKESP,170:POKESP+1,125:POKESP+21,1:POKE 2040,13:PRINT CHR$(147)
    20 A$="THIS TEXT WILL BE PRINTED TO THE SPRITE SHAPE DATA AREA AND DISPLAYED"
    30 GOSUB 100
    40 A$="THIS IS SOME DIFFERENT TEXT TO BE PRINTED TO THE SPRITE SHAPE AREA"
    50 GOSUB 100
    60 COUNT=COUNT+1:IF COUNT<15 THEN 20
    70 END
    100 POKE 648,3:PRINT CHR$(19);CHR$(17);SPC$(24);A$;:POKE 648,4:RETURN

Since PRINTing also changes color memory, you can change the pointer
to print the characters harmlessly to ROM, while changing a lot of
screen RAM at one time, as the following program demonstrates:

    10 D$=CHR(94):FOR I=1 TO 4:D$=D$+D$:NEXT
    20 PRINT CHR$(147);:FOR I=1 TO 7:PRINT TAB(10) D$:NEXT:PRINT:PRINT:PRINT:PRINT
    30 PRINT TAB(9);CHR$(5);"HIT ANY KEY TO STOP"
    40 DIM C(15):FOR I=0TO14:READ A:C(I)=A:NEXT:DATA2,8,7,5,6,4,1,2,8,7,5,6,4,1,2
    50 POKE 53281,0:POKE 648,212:FOR J=0 TO 6:PRINT CHR$(19);
    60 FOR I=J TO J+6:POKE 646,C(I):PRINT TAB(10) D$:NEXT I,J
    70 GET A$:IF A$="" THEN 50
    80 POKE 648,4:POKE 646,1

### Reference (Joe Forster / STA)
Default: $04, $0400, 1024.

### 64'er Magazin (64'er)
In dieser Speicherzelle steht eine Zahl, die als High-Byte dem Betriebssystem
angibt, ab welcher Speicherzelle der Bildschirmspeicher beginnt.

Nach einem Kaltstart (nach dem Einschalten oder nach dem Drücken der
RESET-Taste) steht hier eine 4, das ergibt als Anfangsadresse 1024 (= 4*256).
Beim VC 20 ohne Erweiterung steht dort eine 30. Daraus folgt, daß die
Anfangsadresse bei 7680 (= 30*256) liegt.

Der Bildschirmspeicher hat keinen absolut festen Platz. Innerhalb gewisser
Grenzen kann er durch Verändern des Inhalts der Speicherzelle 53272 (36869 beim
VC 20) verschoben werden. Die Methode dazu ist im Texteinschub näher
beschrieben. Wichtig dabei ist, daß nach dem Verschieben der Inhalt der
Speicherzelle 648 entsprechend geändert wird, damit auch das Betriebssystem die
Verschiebung berücksichtigt.

Umgekehrt kann aber dem Betriebssystem durch Ändern der Zahl in der
Speicherzelle 648 mitgeteilt werden, daß es Zeichen in einen Speicherbereich
bringen soll, der außerhalb des »offiziellen«, durch die Speicherzelle 53272
(36869) festgelegten Bildschirmspeichers liegt.

Zwei Beispiele sollen das verdeutlichen. Der PRINT-Befehl macht letztlich
nichts anderes, als viele Zahlen in den Bildschirm- und den Farbspeicher zu
POKEn. Wenn nun der Zeiger in Zelle 648 verschoben wird, kann man mit einem

PRINT-Befehl eine beliebige Zeichenkette außerhalb des Bildschirmspeichers
speichern. Auf die gleiche Weise kann man beim C 64 Sprites mit einem PRINT-
Befehl speichern, ohne mit READ viele lästige DATA-Zeilen lesen zu müssen.

### 64map (—)
High Byte of Screen Memory Address ($04)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*