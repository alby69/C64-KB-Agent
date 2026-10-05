---
id: 009d-msgflg
type: entity
title: Direct = $80/RUN = 0 output control
aliases:
- Direct = $80/RUN = 0 output control
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/009d-msgflg.md
  sha256: 2dddada9b924d900b159250aeff99051b1ae28e77f4958b8a7c65bf773344829
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-009d-msgflg
---

# Direct = $80/RUN = 0 output control



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

## References
- Source: [[src-009d-msgflg]]
