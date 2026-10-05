---
id: 0286-color
type: entity
title: Current color code
aliases:
- Current color code
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0286-color.md
  sha256: 4065d00c75148963503e84eb4ba7146c4aec336262e7a8b545c323a2eed17258
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0286-color
---

# Current color code



# COLOR — Current color code ($0286)

## Panoramica
Il registro o area di memoria COLOR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0286` (`646` decimale)
- **Range**: `$0286`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Active color nybble

### Commodore-64-intern-Buch (Commodore)
Hier wird die augenblickliche
Zeichenfarbe festgelegt:

|    |            |
|----|------------|
|  0 | schwarz    |
|  1 | weiß       |
|  2 | rot        |
|  3 | lila       |
|  4 | purpur     |
|  5 | grün       |
|  6 | blau       |
|  7 | gelb       |
|  8 | orange     |
|  9 | braun      |
| 10 | hellrot    |
| 11 | dunkelgrau |
| 12 | mittelgrau |
| 13 | hellgrün   |
| 14 | hellblau   |
| 15 | hellgrau   |

### C64 Programmer's Reference Guide (Commodore)
Current Character Color Code

### Memory Map (Jim Butterfield)
Current color code

### Mapping the Commodore 64 (Sheldon Leemon)
The process of PRINTing a character to the screen consists of both
placing the screen code value for the character in screen memory and
placing a foreground color value in the corresponding location in
color RAM.  Whenever a character is PRINTed, the Operating System
fetches the value to be put in color RAM from this location.

The foreground color may be changed in a number of ways.  Pressing the
CTRL or Commodore logo key and numbers 1-8 at the same time will
change the value stored here, and thus the color being printed.
PRINTing the PETASCII equivalent character with the CHR$ command will
have the same effect.  But probably the easiest method is to POKE the
color value directly to this location.  The table below lists the
possible colors that may be produced, and shows how to produce them
using all three methods.

POKE

| COLOR # | COLOR     | CHR$ | KEYS TO PRESS |
|---------|-----------|------|---------------|
|  0      | Black     | 144  | CTRL-1        |
|  1      | White     |   5  | CTRL-2        |
|  2      | Red       |  28  | CTRL-3        |
|  3      | Cyan      | 159  | CTRL-4        |
|  4      | Purple    | 156  | CTRL-5        |
|  5      | Green     |  30  | CTRL-6        |
|  6      | Blue      |  31  | CTRL-7        |
|  7      | Yellow    | 158  | CTRL-8        |
|  8      | Orange    | 129  | Logo-1        |
|  9      | Brown     | 149  | Logo-2        |
| 10      | Lt Red    | 150  | Logo-3        |
| 11      | Dark Gray | 151  | Logo-4        |
| 12      | Med Gray  | 152  | Logo-5        |
| 13      | Lt Green  | 153  | Logo-6        |
| 14      | Lt Blue   | 154  | Logo-7        |
| 15      | Lt Gray   | 155  | Logo-8        |

### Reference (Joe Forster / STA)
Values: $00-$0F, 0-15.

### 64'er Magazin (64'er)
Um ein bestimmtes Zeichen auf den Bildschirm zu drucken, muß vom Betriebssystem
erstens der Bildschirmcode des Zeichens in den Bildschirmspeicher und zweitens
der Codewert der gewünschten Farbe in den Farbspeicher gebracht werden.

In der Speicherzelle 646 steht immer der Codewert derjenigen Farbe, die gerade
eingestellt ist. Immer wenn ein PRINT-Befehl gegeben wird, holt das
Betriebssystem den Farbwert aus der Zelle 646 und bringt ihn in den
Farbspeicher, und zwar an den entsprechenden Platz, wo gerade gePRINTet werden
soll. Der Codewert in der Zelle 646 kann auf drei Arten eingestellt werden:

* Drücken der CTRL-Taste gleichzeitig mit einer der Farbtasten 1 bis 8. Beim C
  64 kommen noch weitere acht Farben dazu durch Drücken der Commodore-Taste
  anstelle der CTRL-Taste.
* PRINT-Befehl gefolgt vom ASCII-Codewert der Farbe Innerhalb von Gänsefüßen.
* POKEn der Farbcodes 0 bis 7 (beim C 64 0 bis 15) direkt in die Speicherzelle.

Innerhalb eines Programms Ist das POKEn in Zelle 646 wohl die eleganteste
Methode (Tabelle 10).

Als Beispiel möge dieses kleine Programm dienen:

    10 FOR X=0 TO 7
    20 POKE 646,X
    30 PRINT "A";
    40 NEXT X
    50 GOTO 10

Wer mehr über Vordergrund- und Hintergrundfarben erfahren will, der lese den
Texteinschub Nr. 26 »Bunte Zeichen und bunter Hintergrund«.

### 64map (—)
Current Character Colour code

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0286-color]]
