---
id: 00d6-tblx
type: entity
title: Row where cursor lives
aliases:
- Row where cursor lives
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00d6-tblx.md
  sha256: 9fb2f8f92b03164117b154aa4cb9bc44de86df28b96b8c07cd3814ddeae1dae3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00d6-tblx
---

# Row where cursor lives



# TBLX — Row where cursor lives ($00D6)

## Panoramica
Il registro o area di memoria TBLX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D6` (`214` decimale)
- **Range**: `$00D6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier wird die Zeilenposition des
Cursors festgehalten.

### C64 Programmer's Reference Guide (Commodore)
Current Cursor Physical Line Number

### Memory Map (Jim Butterfield)
Row where cursor lives

### Mapping the Commodore 64 (Sheldon Leemon)
This location contains the current physical screen line position of
the cursor (0-24).  It can be used in a fashion to move the cursor
vertically, by POKEing the target screen line (1-25) minus 1 here,
followed by a PRINT command.  For example,

    POKE 214,9:PRINT:PRINT "WE'RE ON LINE ELEVEN"

prints the message on line 11.  The first PRINT statement allows the
system to update the other screen editor variables so that they will
also show the new line.  The cursor can also be set or read using the
Kernal PLOT routine (58634, $E50A) as explained in the entry from
locations 780-783 ($030C-$030F).

### Reference (Joe Forster / STA)
Current cursor row. Values: $00-$18, 0-24

### 64'er Magazin (64'er)
Diese Speicherzelle ist zusammen mit der Speicherzelle 211 beschrieben.

### 64map (—)
Current Screen Line number of Cursor

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00d6-tblx]]
