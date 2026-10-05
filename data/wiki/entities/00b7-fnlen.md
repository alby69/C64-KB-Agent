---
id: 00b7-fnlen
type: entity
title: '# characters in file name'
aliases:
- '# characters in file name'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00b7-fnlen.md
  sha256: 91e693c1db4429323d6b8b12099b942aaefb860ef040412a63fff85e54c4bac8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00b7-fnlen
---

# # characters in file name



# FNLEN — # characters in file name ($00B7)

## Panoramica
Il registro o area di memoria FNLEN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B7` (`183` decimale)
- **Range**: `$00B7`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Length current file n str

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle wird
angegeben, aus wie vielen Zeichen der
Filename besteht.

### C64 Programmer's Reference Guide (Commodore)
Length of Current File Name

### Memory Map (Jim Butterfield)
# characters in file name

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the number of characters in the current filename.
Disk filenames may have from 1 to 16 characters, while tape filenames
range from 0 to 187 characters in length.

If the tape name is longer than 16 characters, the excess will be
truncated by the SEARCHING and FOUND messages, but will still be
present on the tape.  This means that machine language programs meant
to run in the cassette buffer may be saved as tape filenames.

A disk file is always referred to be a name, whether full or generic
(containing the wildcard characters * or ?).  This location will
always be greater than 0 if the current file is a disk file.  Tape
LOAD, SAVE, and VERIFY operations do not require that a name be
specified, and this location can therefore contain a 0.  If this is
the case, the contents of the pointer to the filename at 187 will be
irrelevant.

An RS-232 OPEN command may specify a filename of up to four
characters.  These characters are copied to locations 659-662
($0293-$0296), and determine baud rate, word length, and parity.

### Reference (Joe Forster / STA)
Values:

* $00: No parameter.
* $01-$FF: Parameter length.

### 64'er Magazin (64'er)
Die LOAD-, SAVE- und VERIFY-Befehle für Disketten verlangen die Angabe eines
Programm- oder Dateinamens, auf Computerdeutsch »File-Name«. Nähere Angaben
dazu finden Sie im Texteinschub Nr. 19 »Files - Geräte - Namen - Nummern«.

Auch der OPEN-Befehl kann einen File-Namen haben. Bei Kassettenoperationen kann
der File-Name weggelassen werden.

In der Speicherzelle 183 steht während und nach der Verwendung eines der oben
genannten Befehle eine Zahl, die angibt, aus wie vielen Zeichen der File-Name
besteht.

Bei Disketten sind File-Namen möglich, die aus maximal 16 Zeichen bestehen.

Bei Kassetten dagegen sind Namenslängen von maximal 187 Zeichen erlaubt.
Allerdings werden vom Computer auf dem Bildschirm nur 16 Zeichen ausgedruckt
(siehe dazu den Texteinschub 20 »Tape-Header«).

Für die Längenangabe in Zelle 183 gilt dabei nur die Anzahl derjenigen Zeichen,
die zwischen den Gänsefüßchen stehen.

Diese Zahl kann nach einer Ein-/Ausgabeoperation, auch nach einer ungültigen
oder abgebrochenen, durch PEEK (183) ausgelesen werden.

Ein File-Name wird übrigens auch bei einem OPEN-Befehi der RS232-Schnittstelle
angegeben. Dieser Name, der bis zu vier Zeichen lang sein kann, wird in die
Speicherzellen 659 bis 662 übertragen und gibt dort die Übertragungsrate,
Wortlänge und Parity-Prüfung an.

### 64map (—)
Number of Characters in Filename

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00b7-fnlen]]
