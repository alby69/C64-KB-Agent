---
title: '# of INSERTs outstanding'
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
  address: $00D8
  symbol: INSRT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Insert mode flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird die Anzahl der Inserts
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Insert Mode, >0 = # INSTs'
  - name: Memory Map
    author: Jim Butterfield
    description: '# of INSERTs outstanding'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: When the INST key is pressed, the screen editor shifts the line to
      the
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Immer wenn die geSHIFTete INST/DEL-Taste gedrückt wird, um in einer
      Zeile Platz
  - name: 64map
    author: —
    description: Count of number of inserts outstanding
---

# INSRT — # of INSERTs outstanding ($00D8)

## Panoramica
Il registro o area di memoria INSRT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D8` (`216` decimale)
- **Range**: `$00D8`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Insert mode flag

### Commodore-64-intern-Buch (Commodore)
Hier wird die Anzahl der Inserts
festgelegt.

### C64 Programmer's Reference Guide (Commodore)
Flag: Insert Mode, >0 = # INSTs

### Memory Map (Jim Butterfield)
# of INSERTs outstanding

### Mapping the Commodore 64 (Sheldon Leemon)
When the INST key is pressed, the screen editor shifts the line to the
right, allocates another physical line to the logical line if
necessary (and possible), updates the screen line length in 213 ($00D5),
and adjusts the screen line link table at 217 ($00D9).  This location is
used to keep track of the number of spaces that has been opened up in
this way.

Until the spaces that have been opened up are filled, the editor acts
as if in quote mode (see location 212 ($00D4), the quote mode flag).
This means that cursor control characters that are normally
nonprinting will leave a printed equivalent on the screen when
entered, instead of having their normal effect on cursor movement,
etc.  The only difference between insert and quote mode is that the
DELETE key will leave a printed equivalent in insert mode, while the
INST key will insert spaces as normal.

### Reference (Joe Forster / STA)
Values:

* $00: No insertions made, normal mode, control codes change screen layout or behavior.
* $01-$FF: Number of insertions, when inputting this many character next, those must be turned into control codes, similarly to quotation mode.

### 64'er Magazin (64'er)
Immer wenn die geSHIFTete INST/DEL-Taste gedrückt wird, um in einer Zeile Platz
für ein einzufügendes Zeichen zu schaffen, wird der Inhalt der Speicherzelle
216 um 1 erhöht. Dann wird die Zeile ab dem Freiplatz nach rechts verschoben,
der Inhalt der Speicherzelle 213 erhöht und schließlich der entsprechende Wert
der Link-Tabelle für Bildschirmzeilen ab Speicherzelle 217 bis 242 verändert.

Bei jedem Tippen eines Zeichens in den freigewordenen Platz wird der Inhalt von
216 wieder um 1 reduziert, bis mit der 0 das Ende des INSERT-Modus angezeigt
wird.

### 64map (—)
Count of number of inserts outstanding

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*