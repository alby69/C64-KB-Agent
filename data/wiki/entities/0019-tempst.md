---
id: 0019-tempst
type: entity
title: Stack for temporary strings
aliases:
- Stack for temporary strings
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0019-tempst.md
  sha256: c8ff379410253adf5da5d72ad30159be7a40c9b752e6ae31b06a92c6ac443ce8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0019-tempst
---

# Stack for temporary strings



# TEMPST — Stack for temporary strings ($0019)

## Panoramica
Il registro o area di memoria TEMPST è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0019` (`25` decimale)
- **Range**: `$0019`-`$0021`
- **Dimensione**: `9 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Storage for NUMTMP temp descriptors

### Commodore-64-intern-Buch (Commodore)
Die Angaben im Stringstack enthalten
die Stringlänge sowie die Anfangs-
und Endadressen des vorherigen
Strings.

### C64 Programmer's Reference Guide (Commodore)
Stack for Temporary Strings

### Memory Map (Jim Butterfield)
Stack for temporary strings

### Mapping the Commodore 64 (Sheldon Leemon)
The temporary string descriptor stack contains information about
temporary strings which have not yet been assigned to a string
variable.  An examples of such a temporary string is the literal
string "HELLO" in the statement PRINT "HELLO".

Each three-byte descriptor in this stack contains the length of the
string, and its starting and ending locations, expresses as
displacements within the BASIC storage area.

### Reference (Joe Forster / STA)
String stack, temporary area for processing string expressions (9 bytes, 3 entries)

### 64'er Magazin (64'er)
Das ist also der Speicherbereich, von dem in den beiden vorigen Abschnitten
dauernd die Rede war. Ich gebe zu, »Descriptor Stack for Temporary Strings«
drückt die Sache präziser aus als der deutsche Text.

Die Bedeutung eines »vorläufigen« Strings habe ich oben in der Beschreibung der
Speicherzelle 22 erklärt.

Was ein Stapelspeicher (Stack) ist, entnehmen Sie bitte dem Texteinschub 6.
Jeder der 3 Byte langen Angaben im Stack von 22 bis 33 enthält die Länge sowie
die Anfangs- und Endadressen eines vorläufigen Strings, ausgedruckt als
Verschiebung im Basic-Speicherbereich.

### 64map (—)
Stack for temporary Strings

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0019-tempst]]
