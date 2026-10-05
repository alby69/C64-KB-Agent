---
id: 00cb-sfdx
type: entity
title: 'Which key :  64 if no key'
aliases:
- 'Which key :  64 if no key'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00cb-sfdx.md
  sha256: 57be43c1753fa92846e054bfa37e5e2941b8b1d9490b548a754e1baf95b2d346
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00cb-sfdx
---

# Which key :  64 if no key



# SFDX — Which key :  64 if no key ($00CB)

## Panoramica
Il registro o area di memoria SFDX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CB` (`203` decimale)
- **Range**: `$00CB`
- **Dimensione**: `1 byte`
- **Permessi**: `R`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
SHIFT mode on print

### Commodore-64-intern-Buch (Commodore)
Hier steht der jeweilige Code der
gedrückten Taste. (64= keine Taste).

### C64 Programmer's Reference Guide (Commodore)
Flag: Print Shifted Chars

### Memory Map (Jim Butterfield)
Which key :  64 if no key

### Mapping the Commodore 64 (Sheldon Leemon)
The keyscan interrupt routine uses this location to indicate which key
is currently being pressed.  The value here is then used as an index
into the appropriate keyboard table to determine which character to
print when a key is struck.

The correspondence between the key pressed and the number stored here
is as follows:

|    |                                    |
|----|------------------------------------|
| 0  | INST/DEL                           |
| 1  | RETURN                             |
| 2  | CRSR RIGHT                         |
| 3  | F7                                 |
| 4  | F1                                 |
| 5  | F3                                 |
| 6  | F5                                 |
| 7  | CRSR DOWN                          |
| 8  | 3                                  |
| 9  | W                                  |
| 10 | A                                  |
| 11 | 4                                  |
| 12 | Z                                  |
| 13 | S                                  |
| 14 | E                                  |
| 15 | NOT USED (WOULD BE LEFT SHIFT)     |
| 16 | 5                                  |
| 17 | R                                  |
| 18 | D                                  |
| 19 | 6                                  |
| 20 | C                                  |
| 21 | F                                  |
| 22 | T                                  |
| 23 | X                                  |
| 24 | 7                                  |
| 25 | Y                                  |
| 26 | G                                  |
| 27 | 8                                  |
| 28 | B                                  |
| 29 | H                                  |
| 30 | U                                  |
| 31 | V                                  |
| 32 | 9                                  |
| 33 | I                                  |
| 34 | J                                  |
| 35 | 0                                  |
| 36 | M                                  |
| 37 | K                                  |
| 38 | O                                  |
| 39 | N                                  |
| 40 | +                                  |
| 41 | P                                  |
| 42 | L                                  |
| 43 | -                                  |
| 44 | .                                  |
| 45 | :                                  |
| 46 | @                                  |
| 47 | ,                                  |
| 48 | LIRA (BRITISH POUND SIGN)          |
| 49 | *                                  |
| 50 | ;                                  |
| 51 | CLR/HOME                           |
| 52 | NOT USED (WOULD BE RIGHT SHIFT)    |
| 53 | =                                  |
| 54 | UP ARROW (EXPONENTATION SIGN)      |
| 55 | /                                  |
| 56 | 1                                  |
| 57 | LEFT ARROW                         |
| 58 | NOT USED (WOULD BE CTRL)           |
| 59 | 2                                  |
| 60 | SPACE BAR                          |
| 61 | NOT USED (WOULD BE COMMODORE LOGO) |
| 62 | Q                                  |
| 63 | RUN/STOP                           |
| 64 | NO KEY PRESSED                     |

The RESTORE key is not accounted for, because it is not part of the
normal keyboard matrix.  Instead, it is connected directly to the
microprocessor NMI line, and causes an NMI interrupt whenever it is
pressed.

### Reference (Joe Forster / STA)
Values:

* $00-$3F: Keyboard matrix code.
* $40: No key is currently pressed.

### 64'er Magazin (64'er)
Bei der Speicherzelle 145 habe ich beschrieben, wie die Tasten des Computers
abgefragt werden. Die dabei für jede der 64 Tasten (mit Ausnahme der RESTORE-
und der SHIFT-LOCK-Tasten) entstehende Dualzahl wird in eine Dezimalzahl (0 bis
63) umgewandelt und in der Speicherzelle 203 gespeichert, einige auch in der
Zelle 653. Diese Zahl steht auch in Speicherzelle 197, um sie mit der vorher
gedrückten Taste vergleichen zu können.

Die Codezahlen jeder Taste lassen sich mit folgendem Programm abfragen:

    10 PRINT PEEK (203)
    20 GOTO 10

Nach RUN sehen wir ein laufendes Zahlenband, zuerst mit der Zahl 64. Das ist
die Codezahl für »keine Taste gedrückt«. Die X-Taste ergibt 23 (26 beim VC 20),
die W-Taste ergibt 9. Auch die Funktionstasten haben ihren Tastencode. F1
ergibt 4 (39 beim VC 20) und so weiter.

Nur die Steuertasten CTRL, SHIFT, und C= (Commodore-Taste) zeigen keine
Reaktion. Deren Tastencode steht nämlich in Speicherzelle 653. Den Grund für
diesen Separatismus erfahren Sie bei der Besprechung dieser Zelle. Hier ist nur
interessant, daß nicht nur jede einzelne dieser drei Tasten einen eigenen Code
hat, sondern auch alle machbaren Kombinationen von gleichzeitig gedrückten
Steuertasten. Um das zu sehen, ändern Sie bitte die Zeile 10 so ab:

    10 PRINT PEEK (203), PEEK(653)

Tabelle 9 gibt Ihnen die volle Übersicht. Wenn Sie sich die Mühe machen, die
Zahlenreihen der Zelle 203 auf Vollständigkeit zu prüfen, dann werden Sie
feststellen, daß vier Zahlen fehlen. Es sind die Werte, die eigentlich den vier
Steuertasten CTRL, C=, rechte und linke SHIFT-Taste zugewiesen sind. Aber wie
gesagt, sie werden gleich nach 653 umgeleitet, wobei allerdings kein
Unterschied mehr zwischen der linken und rechten SHIFT-Taste gemacht wird.

Einige Anwendungsbeispiele der Tastencodes sowie der Kombinationen der drei

Steuertasten finden Sie im Texteinschub Nr. 21 »Abfrage der Tastencodes«. Wie
schon erwähnt, haben die RESTORE-Taste und die SHIFT-LOCK-Taste keinen eigenen
Code.

Die RESTORE-Taste ist überhaupt nicht an die Tastatur-Matrix angeschlossen,
sondern ist direkt mit der RESTORE-Leitung des Computers verbunden. Dort löst
sie einen sogenannten NMI-Interrupt aus. Die SHIFT-LOCK-Taste ist lediglich
eine mechanische Verriegelung der SHIFT-Taste.

### 64map (—)
Flag: Print shifted Characters

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00cb-sfdx]]
