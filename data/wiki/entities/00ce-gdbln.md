---
id: 00ce-gdbln
type: entity
title: Character under cursor
aliases:
- Character under cursor
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00ce-gdbln.md
  sha256: 176d8e944720f8975bccc8950d4da75e2120ee5597025023ebee202fb1d17367
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00ce-gdbln
---

# Character under cursor



# GDBLN — Character under cursor ($00CE)

## Panoramica
Il registro o area di memoria GDBLN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CE` (`206` decimale)
- **Range**: `$00CE`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Char before cursor

### Commodore-64-intern-Buch (Commodore)
Hier ist jeweils der Bildschirmcode
eines Zeichens angegeben, das sich
gerade unter dem Cursor befindet.

### C64 Programmer's Reference Guide (Commodore)
Character Under Cursor

### Memory Map (Jim Butterfield)
Character under cursor

### Mapping the Commodore 64 (Sheldon Leemon)
The cursor is formed by printing the inverse of the character that
occupies the cursor position.  If that characters is the letter A, for
example, the flashing cursor merely alternates between printing an A
and a reverse-A.  This location keeps track of the normal screen code
of the character that is located at the cursor position, so that it
may be restored when the cursor moves on.

### Reference (Joe Forster / STA)
Screen code of character under cursor

### 64'er Magazin (64'er)
Im Prinzip ist der Cursor nichts anderes als das wiederholte Drucken eines
Zeichens in reverser Form, das gerade unter dem Cursor steht. Normalerweise ist
dies das Leerzeichen, deshalb sehen wir meistens das ausgefüllte Viereck.
Fahren Sie aber mit dem Cursor auf einen Buchstaben, dann erscheint dieser
wechselweise normal und revers. In Speicherzelle 206 steht jeweils der
Bildschirmcode des Zeichens unter dem Cursor. Geben Sie die folgende Anweisung
direkt ein, fahren aber noch vor dem Drücken der RETURN-Taste mit dem Cursor
zurück auf eines der Zeichen, zum Beispiel auf ein P:

    PRINT PEEK(206)

Nach RETURN erscheint die Zahl 16. Das ist also der Bildschirmcode des
Zeichens, auf dem der Cursor saß, als die RETURN-Taste gedrückt wurde. Sie
können das mit allen anderen Zeichen dieser Zeile wiederholen.

Ich kann mir vorstellen, daß eine derartige Abfrage in einem Programm, welches
mit dem Bildschirm arbeitet, sinnvoll sein kann. Die Speicherzelle 206 wird
allerdings nach jedem Blinken auf den neuesten Stand gebracht.

### 64map (—)
Character under Cursor while Cursor Inverted

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00ce-gdbln]]
