---
title: Current I/O prompt flag
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
  address: $0013
  symbol: CHANNL
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Holds channel number
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Speicherzelle $0013 wird als Zeiger
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: INPUT Prompt'
  - name: Memory Map
    author: Jim Butterfield
    description: Current I/O prompt flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Whenever BASIC inputs or outputs data, it looks here to determine
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $00, keyboard for input and screen for output.'
  - name: 64'er Magazin
    author: 64'er
    description: Immer dann, wenn von Basic Daten ein- oder ausgegeben werden, schaut
      die
  - name: 64map
    author: —
    description: File number of current Input Device
---

# CHANNL — Current I/O prompt flag ($0013)

## Panoramica
Il registro o area di memoria CHANNL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0013` (`19` decimale)
- **Range**: `$0013`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Holds channel number

### Commodore-64-intern-Buch (Commodore)
Die Speicherzelle $0013 wird als Zeiger
für die Peripheriegeräte wie Tastatur,
Datasette, RS232, User-Port,
Bildschirm, Drucker und Floppy
verwendet.

### C64 Programmer's Reference Guide (Commodore)
Flag: INPUT Prompt

### Memory Map (Jim Butterfield)
Current I/O prompt flag

### Mapping the Commodore 64 (Sheldon Leemon)
Whenever BASIC inputs or outputs data, it looks here to determine
which I/O device is currently active for the purpose of prompting or
output control.  It uses location 184 ($00B8) for purposes of deciding
what device actually to put input from or output to.

When the default input device (number 0, the keyboard) or output
device (number 3, the display screen) is used, the value here will be
a zero, and the format of prompting and output will be the standard
screen output format.

When another device is used, the logical file number (CMD channel
number) will be placed here.  This lets the system now that it may
have to make some subtle changes in the way it performs the I/O
operation.  For example, if TAB is used with the PRINT command, cursor
right characters are used if the device PRINTed to is the screen.
Otherwise, spaces are output when the number here is other than zero
(the assumption being that you can't tab a printer like you can the
screen).

Likewise, the ? prompt for INPUT is suppressed if the file number here
is nonzero, as is the EXTRA IGNORED message, and input of a carriage
return by itself is ignored, rather than being treated as a null
string ("").  Therefore, by OPENing the screen as a device, and
issuing the CMD statement, you can force the suppression of the ?
prompt, and the other effects above.

CMD places the new output file number here, and calls the Kernal to
open the device for output, leaving it LISTENing for output (such as
the READY prompt, which is diverted to the new device).

Many routines reset this location and UNLISTEN the device, defeating
the CMD and once again sending the output to the screen.  If an error
message has to be displayed, for example, this location will be reset
and the message will be displayed on the screen.  GET, GET#, INPUT,
INPUT#, and PRINT# all will reset this location after the I/O is
completed, effectively redirecting output back to the screen.  PRINT
and LIST are the only I/O operations that will not undo the CMD.

This location can also be used to fool BASIC into thinking that data
it is reading from the tape is actually being entered into the
keyboard in immediate mode.

For a look at a technique that uses a different approach to accomplish
the same thing for disk or tape users, see location 512 ($0200), the
keyboard buffer.

### Reference (Joe Forster / STA)
Default: $00, keyboard for input and screen for output.

### 64'er Magazin (64'er)
Immer dann, wenn von Basic Daten ein- oder ausgegeben werden, schaut die
entsprechende Routine des Übersetzers in Zelle 19 nach, um welches
Peripheriegerät es sich handelt. Zur Debatte stehen Tastatur, Datasette, RS232-
User-Port, Bildschirm, Drucker und Floppy-Laufwerk.

Die Flagge ihrerseits ist ausschlaggebend für die feinen Unterschiede, wie zum
Beispiel das Fragezeichen, bei Eingabe von der Tastatur (INPUT) oder die
Anweisung »Press Play on Tape« bei Eingabe von der Datasette.

Beim Einschalten des Rechners setzt die Initialisierungsroutine des
Betriebssystems, die beim VC 20 ab Adresse 58276 ($E3A4), beim C 64 ab 58303
($E3BF) beginnt, die Flagge in Zelle 19auf 0. Die Null bedeutet Eingabe über
Tastatur und Ausgabe über Bildschirm.

Wenn Sie einen Disassembler haben, drucken Sie doch einmal das Assemblerlisting
aus. Sie werden in Adresse 58324/58325 ($E3D4/$E3D5), beim C 64 in 58354/58355
($E3F2/$E3F3) den Befehl finden, der eine Null nach Zelle 19 ($0013) bringt.

Immer dann, wenn ein Programm nicht Tastatur und Bildschirm, sondern eines der
oben genannten anderen Peripheriegeräte anspricht (indem mit OPEN.... eine
Datei = Logical File eröffnet wird), wird in Zelle 19 die Nummer der gerade
bearbeiteten Datei eingetragen, mit den bereits beschriebenen Konsequenzen.

Ich will hier nicht weiter darauf eingehen, da wir den Inhalt von Zelle 19
selbst nicht auslesen können. Er wird nämlich immer gleich wieder auf Null
gesetzt.

Wir können ihn aber durch POKE verändern. Durch POKE 19,1 gaukeln wir dem
Rechner vor, daß Ein- und Ausgabe über »externe« Geräte läuft, selbst wenn nur
die Tastatur und der Bildschirm betrieben werden.

Wenn zum Beispiel der Rechner der Meinung ist, daß ein INPUT von der Datasette
kommt, druckt er kein Fragezeichen aus; auch kein EXTRA IGNORED als
Fehlermeldung bei zu zahlreicher Eingabe und das alleinige Drücken der RETURN-
Taste ignoriert er auch, im Gegensatz zum »normalen« INPUT Probieren Sie es
aus:

    10 INPUT "TEST"; A$
    20 PRINT A$

In diesem Normalfall erscheint nach RUN darunter die Aufforderung TEST?

Eine Eingabe, zum Beispiel XX, erscheint mit einem Abstand daneben, und nach
RETURN wird XX an den Anfang der nächsten Zeile gedruckt. Alle falschen
Eingaben werden mit den üblichen Fehlermeldungen quittiert.

Jetzt fügen wir ein:

    5 POKE 19,1

Nach RUN erscheint wieder die Aufforderung TEST, aber ohne Fragezeichen. Die
Eingabe XX wird ohne Abstand daneben gesetzt und nach RETURN mit einem Abstand
in derselben Zeile weitergeschrieben.

Das Drücken der RETURN-Taste setzt den Cursor nicht wie üblich in die nächste
Zeile, sondern schiebt ihn in derselben Zeile weiter.

Diesen zusätzlichen Effekt muß man beachten, da er sehr störend für den Verlauf
eines Programms sein kann.

Man kann ihn natürlich auch nutzbringend einsetzen, hat er doch die Eigenschaft
eines automatischen »Cursor UP«. Eine pfiffige Anwendung dieser Art wurde von
Brad Templeton für den PET erfunden und ist von Jim Butterfield für eine MERGE-
Routine mit dem Namen »Magic Merge« veröffentlicht worden.

Da diese Routine aber primär auf der Eigenschaft der Speicherzelle 153 basiert,
werde ich sie dann erläutern, sobald wir bei der Zelle 153 angelangt sind.

Zurück zur Flagge in Zelle 19.

Umgekehrt können wir POKE 19,0 leider nicht nutzen, da die betroffenen Befehle
GET, GET#, INPUT, INPUT# und PRINT # die Flagge sofort auf den richtigen Wert
setzen. Nur PRINT und LIST tun das nicht, wie wir bei dem PRINT-Befehl oben ja
gesehen haben.

### 64map (—)
File number of current Input Device

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*