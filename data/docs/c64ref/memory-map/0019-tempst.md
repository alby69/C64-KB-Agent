---
title: Stack for temporary strings
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
  address: $0019
  address_end: $0021
  symbol: TEMPST
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Storage for NUMTMP temp descriptors
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Angaben im Stringstack enthalten
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Stack for Temporary Strings
  - name: Memory Map
    author: Jim Butterfield
    description: Stack for temporary strings
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The temporary string descriptor stack contains information about
  - name: Reference
    author: Joe Forster / STA
    description: String stack, temporary area for processing string expressions (9
      bytes, 3 en...
  - name: 64'er Magazin
    author: 64'er
    description: Das ist also der Speicherbereich, von dem in den beiden vorigen Abschnitten
  - name: 64map
    author: —
    description: Stack for temporary Strings
---

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