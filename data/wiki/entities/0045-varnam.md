---
id: 0045-varnam
type: entity
title: Current variable name
aliases:
- Current variable name
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0045-varnam.md
  sha256: 513cdbdb0fbb369cd04ceea91062abc03fa39eb29c9ea54dbd51a20a79b41837
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0045-varnam
---

# Current variable name



# VARNAM — Current variable name ($0045)

## Panoramica
Il registro o area di memoria VARNAM è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0045` (`69` decimale)
- **Range**: `$0045`-`$0046`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Variable's name is stored here

### Commodore-64-intern-Buch (Commodore)
Falls während des Ablaufs eines
Programms eine Variable auftaucht,
wird deren Name hier zwischengespeichert.

### C64 Programmer's Reference Guide (Commodore)
Current BASIC Variable Name

### Memory Map (Jim Butterfield)
Current variable name

### Mapping the Commodore 64 (Sheldon Leemon)
The current variable name being searched for is stored here, in the
same two- byte format as in the variable value storage area located at
the address pointed to by 45 ($002D).  See that location for an
explanation of the format.

### Reference (Joe Forster / STA)
Bits:

* $0045 bits #0-#6: First character of variable name.
* $0046 bits #0-#6: Second character of variable name; $00 = Variable name consists of only one character.
* $0045 bit #7 and $0046 bit #7:
    * %00: Floating-point variable.
    * %01: String variable.
    * %10: FN function, created with DEF FN.
    * %11: Integer variable.

### 64'er Magazin (64'er)
Wenn beim Ablauf eines Programms eine Variable auftaucht, muß ihr derzeitiger
Wert im Variablen-Speicher gesucht werden. Während dieses Suchvorgangs wird der
Name der Variablen in 69 und 70 zwischengespeichert. Die Form der
Zwischenspeicherung ist dieselbe 2-Byte-Darstellung wie im Variablenspeicher,
beschrieben bei der Behandlung der Speicherzellen 45 und 46.

### 64map (—)
Name of Variable being sought in Variable Table

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0045-varnam]]
