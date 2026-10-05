---
id: 028d-shflag
type: entity
title: Keyboard Shift/Control flag
aliases:
- Keyboard Shift/Control flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/028d-shflag.md
  sha256: cff40e91b5e4805ffa2894d0abb02ed3a6363dbb03de5dd057c8720728a866c0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-028d-shflag
---

# Keyboard Shift/Control flag



# SHFLAG — Keyboard Shift/Control flag ($028D)

## Panoramica
Il registro o area di memoria SHFLAG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$028D` (`653` decimale)
- **Range**: `$028D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
SHIFT flag byte

### Commodore-64-intern-Buch (Commodore)
In diesem Register stehen die
Tastencodes der Steuertasten:

|   |                           |
|---|---------------------------|
| 1 | SHIFT                     |
| 2 | Commodore                 |
| 3 | SHIFT und Commodore       |
| 4 | CTRL                      |
| 5 | SHIFT und CTRL            |
| 6 | Commodore und CTRL        |
| 7 | SHIFT, Commodore und CTRL |

### C64 Programmer's Reference Guide (Commodore)
Flag: Keyboard SHIFT Key/CTRL Key/C= Key

### Memory Map (Jim Butterfield)
Keyboard Shift/Control flag

### Mapping the Commodore 64 (Sheldon Leemon)
This flag signals which of the SHIFT, CTRL, or Commodore logo keys are
currently being pressed, if any.

A value of 1 signifies that one of the SHIFT keys is being pressed, a
2 shows that the Commodore logo key is down, and 4 means that the CTRL
key is being pressed.  If more than one key is held down, these values
will be added; for example, a 3 indicates that SHIFT and logo are both
held down.

The value here is used by the Operating System when determining how to
convert a keypress into a PETASCII character.  There are four
different tables used to translate one of the 64 keys on the keyboard
matrix into a PETASCII character, and the combination of special SHIFT
keys determines which of these tables will be used (see the entry for
location 245 ($00F5) for more details on the keyboard tables).

Pressing the SHIFT and Commodore logo keys at the same time will
toggle the character set that is presently being used between the
uppercase/graphics set, and the lowercase/uppercase set (provided that
the flag at 657 ($0291) has not been set to disable this switch).

This changes the appearance of all of the characters on the screen at
once.  It has nothing whatever to do with the keyboard shift tables,
however, and should not be confused with the printing of SHIFTed
characters, which affects only one character at a time.  Rather, it is
the result of the value of the character dot data table base address
in 53272 ($D018) being changed.  The came result may be obtained by
POKEing that address directly.

### Reference (Joe Forster / STA)
Bits:

* Bit #0: 1 = One or more of left Shift, right Shift or Shift Lock is currently being pressed or locked.
* Bit #1: 1 = Commodore is currently being pressed.
* Bit #2: 1 = Control is currently being pressed.

### 64'er Magazin (64'er)
In der Speicherzelle 203 stehen die Codes aller Tasten, die gedrückt werden,
außer die der drei Steuertasten SHIFT, CTRL und Commodore (oft auch CBM-, Logo-
oder C=-Taste genannt). Diese drei Ausnahmen haben ihr eigenes Code-Register,
eben 653.

Der Grund dafür liegt in der Bedeutung der drei Tasten. Sie können ja
bekanntlich verschiedene Zeichensätze einschalten:

* SHIFT schaltet das Zeichen vorne rechts auf einerTaste ein
* C= schaltet das Zeichen vorne links auf einer Taste ein
* CTRL schaltet die Farben vorn auf den Zahlentasten ein
* SHIFT + C= schaltet von dem normalen Zeichensatz auf die Groß-/
  Kleinschreibung um.

Ich habe diese Zusammenhänge auch bei der Behandlung der Speicherzellen 245 und
246 erwähnt.

Die Codezahlen selbst sind auch in der Tabelle 9 enthalten. Der Vollständigkeit
halber sind sie hier noch einmal angegeben:

|                       |   |
|-----------------------|---|
| SHIFT                 | 1 |
| C=                    | 2 |
| CTRL                  | 4 |
| SHIFT und C=          | 3 |
| SHIFT und CTRL        | 5 |
| C= und CTRL           | 6 |
| SHIFT und C= und CTRL | 7 |

Mit dem folgenden kleinen Programm und mit ein wenig Fingerfertigkeit können
Sie diese Codewerte nachvollziehen:

    10 PRINT PEEK(653)
    20 GOTO 10

Eine interessante Anwendung habe ich im Texteinschub Nr. 21 »Abfrage der
Tastencodes oder 476 Funktionstasten« gegeben.

### 64map (—)
Flag: Shift Keys: Bit 1 = Shift, Bit 2 = CBM, Bit 3 = CTRL; ($00 = None, $01 = Shift, etc.)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-028d-shflag]]
