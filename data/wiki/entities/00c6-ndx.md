---
id: 00c6-ndx
type: entity
title: '# chars in keybd buffer'
aliases:
- '# chars in keybd buffer'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00c6-ndx.md
  sha256: db08f80b1be2fceef3872fe4aed5e34077f3e6e32c8b55d999cacbd69baf5ea0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00c6-ndx
---

# # chars in keybd buffer



# NDX — # chars in keybd buffer ($00C6)

## Panoramica
Il registro o area di memoria NDX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C6` (`198` decimale)
- **Range**: `$00C6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Index to keyboard q

### Commodore-64-intern-Buch (Commodore)
Hier steht die jeweilige Anzahl der
Zeichen, die im Tastaturpuffer
gespeichert sind.

### C64 Programmer's Reference Guide (Commodore)
No. of Chars. in Keyboard Buffer (Queue)

### Memory Map (Jim Butterfield)
# chars in keybd buffer

### Mapping the Commodore 64 (Sheldon Leemon)
The value here indicates the number of characters waiting in the
keyboard buffer at 631 ($0277).  The maximum number of characters in
the keyboard buffer at any one time is determined by the value in
location 649 ($0289), which defaults to 10.

If INPUT or GET is executed while there are already characters in the
buffer, those characters will be read as part of the data stream.  You
can prevent this by POKEing a 0 to this location before those
operations, which will always cause any character in the buffer to be
ignored.  This technique can be handy when using the joystick in
Controller Port #1, which sometimes causes fake keypresses to be
registered, placing unwanted characters in the keyboard buffer.

Not only is this location handy for taking unwanted characters out of
the keyboard buffer, but it can also be used to put desired characters
into the buffer, and thus to program the keyboard buffer.  This
technique (dynamic keyboard) allows you to simulate keyboard input in
direct mode from a program.

The dynamic keyboard technique is an extremely useful one, as it
enables you to add, delete, or modify program lines while the program
is running.  The basic scheme is to POKE the PETASCII character values
that you wish to be printed (including cursor control characters and
carriage returns) into the buffer.  Then, when an END statement is
executed, the characters in the buffer will be printed, and entered by
the carriage return.

This technique can help with the problem of trying to use data
separation and terminator characters with INPUT statements.  If you
try to INPUT a string that has a comma or colon, the INPUT will read
only up to that character and issue an EXTRA IGNORED error message.
You can avoid this by entering the input string in quotes, but this
places on the user the burden of remembering the quote marks.  One
solution is to use the statements:

    POKE 198,3:POKE 631,34: POKE 632,34: POKE 633,20

before the input.  This will force two quote marks and a delete into
the buffer.  The first quote mark allows the comma or colon to be
INPUT, the second is used to get the editor out of quote mode, and the
delete removes that second quote.

For more specific information and programming examples, see the
description of location 631 ($0277), the keyboard buffer.

### Reference (Joe Forster / STA)
Values:

* $00, 0: Buffer is empty.
* $01-$0A, 1-10: Buffer length.

### 64'er Magazin (64'er)
Die Funktion des Tastaturpuffers, zu dem wir bei den Speicherzellen 631 und 640
noch kommen werden, habe ich bereits in diesem Kurs, und zwar im Texteinschub
Nr. 15 »Dynamische Tastenabfrage« erklärt. Dabei habe ich damals schon
sozusagen im Vorgriff die Zelle 198 verwendet.

In dieser Speicherzelle steht die jeweilige Anzahl der Zeichen, die im
Tastaturpuffer gespeichert sind und darauf warten, weiterverarbeitet zu werden.

Das folgende kleine Programm zeigt es.

    10 GET A$
    20 PRINT PEEK (198);A$
    30 FOR J=1 3000:NEXT J
    40 GOTO 10

Der GET-Befehl holt ein Zeichen aus dem Tastaturpuffer - sofern eines dort zu
finden ist. Die Zeile 20 druckt die Anzahl derZeichen im Pufferaus, daneben das
erste dieser Zeichen. Dann folgt eine Warteschleife, die uns erlaubt, ganz
schnell ein paarTasten zu drücken. Danach springt das Programm an den Anfang
zurück und arbeitet diese eingegebenen Zeichen ab. Es ist dabei deutlich zu
sehen, wie durch den GET-Befehl bereits ein Zeichen aus dem Puffer genommen und
dadurch der Inhalt der Zelle 198 sofort um 1 reduziert wird.

Der Inhalt der Speicherzelle 198 kann mit POKE auch verändert werden.

Eine sinnvolle Anwendung dieser Beeinflussung erlaubt der nicht gerade sehr
populäre WAIT-Befehl.

Ersetzen Sie bitte im obigen Programm die Warteschleife der Zeile 30 durch:

    30 POKE 198,0: WAIT 198,1

Zuerst wird dem Computer vorgegaukelt, daß der Tastaturpuffer leer sei. Durch
den WAIT-Befehl wartet das Programm danach so iange, bis ein Zeichen im
Tastaturpuffer erscheint und springt erst dann auf die nächste Zeile 40.

Wenn Sie nach dem WAIT-Befehl statt der 1 eine 2 eingeben, wartet diese Zeile
entsprechend auf zwei Tasteneingaben. Allerdings wird in der Zeile 20 dann nur
jedes zweite Zeichen ausgedruckt.

### 64map (—)
Number of Characters in Keyboard Buffer queue

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00c6-ndx]]
