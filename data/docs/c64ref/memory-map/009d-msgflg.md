---
title: Direct = $80/RUN = 0 output control
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
related:
- ecec-run
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
  address: $009D
  symbol: MSGFLG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: OS message flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In dieser Speicherzelle wird
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: $80 = Direct Mode, $00 = Program'
  - name: Memory Map
    author: Jim Butterfield
    description: Direct = $80/RUN = 0 output control
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This flag is set by the Kernal routine SETMSG (65048, $FE18), and
      it
  - name: Reference
    author: Joe Forster / STA
    description: 'Bits:'
  - name: 64'er Magazin
    author: 64'er
    description: 'Man muß zwischen zwei Arten von Meldungen unterscheiden:'
  - name: 64map
    author: —
    description: 'Flag: $00 = Program mode: Suppress Error Messages, $40 = Kernal
      Error Message...'
---

# MSGFLG — Direct = $80/RUN = 0 output control ($009D)

## Panoramica
Il registro o area di memoria MSGFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$009D` (`157` decimale)
- **Range**: `$009D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
OS message flag

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle wird
angegeben, welche Fehlermeldungen
zugelassen werden und welche nicht.
$00 unterdrückt alle Fehlermeldungen,
$80 kommt dem normalen Eingabemodus
gleich und $C0 läßt alle Fehlermeldungen
zu. Diese Zustände können
alle künstlich erzeugt werden.

### C64 Programmer's Reference Guide (Commodore)
Flag: $80 = Direct Mode, $00 = Program

### Memory Map (Jim Butterfield)
Direct = $80/RUN = 0 output control

### Mapping the Commodore 64 (Sheldon Leemon)
This flag is set by the Kernal routine SETMSG (65048, $FE18), and it
controls whether or not Kernal error messages or control messages will
be displayed.

A value of 192 ($C0) here means that both Kernal error and control
messages will be displayed.  This will never normally occur when using
BASIC, which prefers its own plain text error messages over the
Kernal's perfunctory I/O ERROR (number).  The Kernal error messages
might be used, however, when you are SAVEing or LOADing with a machine
language monitor.

A 128 ($80) means that control messages only will be displayed.  Such
will be the case when you are in the BASIC direct or immediate mode.
These messages include SEARCHING, SAVING, FOUND, etc.

A value of 64 means that Kernal error messages only are on.  A 0 here
suppresses the display of all Kernal messages.  This is the value
placed here when BASIC enters the program or RUN mode.

### Reference (Joe Forster / STA)
Bits:

* Bit #6: 0 = Suppress I/O error messages; 1 = Display them.
* Bit #7: 0 = Suppress system messages; 1 = Display them.

### 64'er Magazin (64'er)
Man muß zwischen zwei Arten von Meldungen unterscheiden:

Meldungen des Betriebssystems Meldungen des Basic-Übersetzers Die Meldungen des
Betriebssystems kennen wir als Angaben zum Ablauf, wie SEARCHING FOR, FOUND,
PRESS PLAY ON TAPE und so weiter. Normalerweise nicht bekannt ist die Meldung
I/O ERROR #, wobei nach dem Zeichen # Zahlen von 0 bis 29 stehen können. Diese
Zahlen beziehen sich auf Meldungen des Übersetzers (Interpreter), die
ausschließlich Fehlermeldungen sind. Das mag verwirrend klingen, klärt sich
aber sofort. Die Flagge in 157 kann vier Werte annehmen: 0,64,128 und 192.

1. Der Wert 0 unterdrückt alle Meldungen des Betriebssystems. Dieser Modus
   tritt nach RUN beim Ablauf eines Programms ein.
2. Der Wert 64 läßt nur Fehlermeldungen des Betriebssystems zu. Dieser Modus
   ist normalerweise nicht vorgesehen, kann aber künstlich erzeugt werden.
3. Der Wert 128 unterdrückt die Fehlermeldung des Betriebssystems. Dieser Modus
   entspricht dem Normalfall.
4. Der Wert 192 läßt alle Meldungen zu. Auch dieser Modus ist nur künstlich
   herzustellen.

Das folgende Beispiel macht das deutlich. Geben Sie direkt ein:

    POKE 157,0:LOAD"$",9

Wir versuchen, vom Gerät mit der Nummer 9, das ist eine zweite Floppy, die
Directory zu laden. Wir erhalten entsprechend Punkt 1 nur die Meldung des
Übersetzers

    ?DEVICE NOT PRESENT

Verändern wir den POKE-Befehl für Punkt 2:

    POKE 157,64:LOAD"$",9

Wir erhalten jetzt

    I/O ERROR #5
    ?DEVICE NOT PRESENT

    POKE 157,128:LOAD"$",9

ergibt die Meldung

    SEARCHING FOR $
    ?DEVICE NOT PRESENT

Schließlich nehmen wir noch den letzten Fall:

    POKE 157,192: LOAD"$",9

Jetzt erhalten wir alles:

    SEARCHING FOR $
    I/O ERROR #5
    ?DEVICE NOT PRESENT

Da die Fehlermeldung des Betriebssystems und die zugehörigen Nummern in keinem
Handbuch erwähnt sind, habe ich sie interessehalber in der folgenden Tabelle
zusammengefaßt.

| #  | MELDUNG (ERROR)       |
|----|-----------------------|
| 1  | TOO MANY FILES        |
| 2  | FILE OPEN             |
| 3  | FILE NOT OPEN         |
| 4  | FILE NOT FOUND        |
| 5  | DEVICE NOT PRESENT    |
| 6  | NOT INPUT FILE        |
| 7  | NOT OUTPUT FILE       |
| 8  | MISSING FILE NAME     |
| 9  | ILLEGAL DEVICE NUMBER |
| 10 | NEXT WITHOUT FOR      |
| 11 | SYNTAX                |
| 12 | RETURN WITHOUT GOSUB  |
| 13 | OUT OF DATA           |
| 14 | ILLEGAL QUANTITY      |
| 15 | OVERFLOW              |
| 16 | OUT OF MEMORY         |
| 17 | UNDEF'D STATEMENT     |
| 18 | BAD SUBSCRIPT         |
| 19 | REDIM'D ARRAY         |
| 20 | DIVISION BY ZERO      |
| 21 | ILLEGAL DIRECT        |
| 22 | TYPE MISMATCH         |
| 23 | STRING TOO LONG       |
| 24 | FILE DATA             |
| 25 | FORMULA TOO COMPLEX   |
| 26 | CAN'T CONTINUE        |
| 27 | UNDEF'D FUNCTION      |
| 28 | VERIFY                |
| 29 | LOAD                  |

### 64map (—)
Flag: $00 = Program mode: Suppress Error Messages, $40 = Kernal Error Messages only, $80 = Direct mode: Full Error Messages

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*