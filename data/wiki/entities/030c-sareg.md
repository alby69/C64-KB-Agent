---
id: 030c-sareg
type: entity
title: SYS A-reg save
aliases:
- SYS A-reg save
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/030c-sareg.md
  sha256: 2b0b5fb53c16c0568e43e5f8020f8af05795439f8b8f34751b638f3ccb738701
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-030c-sareg
---

# SYS A-reg save



# SAREG — SYS A-reg save ($030C)

## Panoramica
Il registro o area di memoria SAREG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$030C` (`780` decimale)
- **Range**: `$030C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
.A reg

### Commodore-64-intern-Buch (Commodore)
Akku für SYS-Befehl

### C64 Programmer's Reference Guide (Commodore)
Storage for 6502 .A Register

### Memory Map (Jim Butterfield)
SYS A-reg save

### Mapping the Commodore 64 (Sheldon Leemon)
The BASIC SYS command uses this area to store 6510 internal
registers--the Accumulator (.A), the .X and .Y index registers, and
the status register, .P.

Before every SYS command, each of the registers is loaded with the
value found in the corresponding storage address.  After the ML
program finished executing, and returns to BASIC with an RTS
instruction, the new value of each register is stored in the
appropriate storage address.  This is only true of SYS, not of the
similar USR command.

This feature allows you to place the necessary preentry values into
the registers from BASIC before you SYS to a Kernal or BASIC ML
routine.  It also enables you to examine the resulting effect of the
routine on the registers, and to preserve the condition of the
registers on exit for subsequent SYS calls.

An extremely practical application comes immediately to mind.
Although the 64's BASIC 2 has many commands for formatting printed
characters on the monitor screen (for example, TAB, SPC, PRINT A$,B),
there is none to adjust the vertical cursor position.

There is a Kernal routine, PLOT (58634, $E50A), which will allow you
to position the cursor anywhere on the screen.  In order to use it,
you must first clear the carry flag (set it to 0), and then place the
desired horizontal column number in the .Y register and the vertical
row number in the .X register before entering the routine with a SYS
65520.  Using the register storage area, we can print the work HELLO
at row 10, column 5 with the following BASIC line:

    POKE 781,10:POKE 782,5:POKE 783,0:SYS 65520:PRINT "HELLO"

You can also use these locations to help you take advantage of Kernal
routines that return information in the register.  For example, the
SCREEN routine (58629,$E505) returns the number of screen rows in the
.Y register, and the number of columns in the .X register.  Using this
routine, a BASIC program could be written to run on machines with
different screen formats (for example, the 64 and the VIC-20).  Just
PEEK(781) after a SYS 65517 to see how many screen columns the
computer display has.

### Mapping the Commodore 64 (Sheldon Leemon)
Storage Area for .A Register (Accumulator)

### Reference (Joe Forster / STA)
Default value of register A for SYS. Value of register A after SYS

### 64'er Magazin (64'er)
Der SYS-Befehl holt aus den nächsten vier Speicherzellen alle notwendigen
Parameter, die für ein mit SYS zu startendes Maschinenprogramm notwendig sind.
Er speichert sie in die vier Register des Mikroprozessors 6510 (beim VC 20
heißt er 6502). Es sind dies:

* der Akkumulator
* das X-Register
* das Y-Register
* das P-(Status-)Register

Die Bedeutung der Register ist im Assembler-Kurs erklärt worden.

Normalerweise funktioniert der SYS-Befehl nur, wenn vorher schon alle Parameter
des aufgerufenen Maschinenprogramms richtig vorhanden sind, was meistens nicht
der Fall ist.

So können Sie zum Beispiel mit Aufrufen der Load-Routine durch SYS 62622 nichts
ausrichten, weil die für LOAD erforderlichen Parameter, nämlich Gerätenummer,
File-Namen, Anfangs- und Endadresse, nicht festgelegt sind.

Wie dies mit Hilfe der vier folgenden Register-Speicherzellen erreichbar ist,
hat Rolf Zweifel schon in der Ausgabe 7/84, Seite 131 erklärt. Weil das aber
schon lange her ist und weil es hier so schön in den Kurs paßt, wiederhole ich
dieses Thema im Texteinschub Nr. 33 »Der vorbereitete SYS-Befehl«.

### 64'er Magazin (64'er)
Speicher für den Akkumulator

### 64map (—)
Storage for 6510 Accumulator during SYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-030c-sareg]]
