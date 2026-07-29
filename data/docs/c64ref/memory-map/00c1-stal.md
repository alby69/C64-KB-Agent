---
title: I/O start address
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
  address: $00C1
  address_end: $00C2
  symbol: STAL
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Registern ist in LOW- und
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: I/O Start Address
  - name: Memory Map
    author: Jim Butterfield
    description: I/O start address
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the beginning address of the area in RAM
      which
  - name: Reference
    author: Joe Forster / STA
    description: Start address during SAVE to serial bus, LOAD and VERIFY from datasette
      and S...
  - name: 64'er Magazin
    author: 64'er
    description: In diesen Speicherzellen steht in Low-/High-Byte-Darstellung die
      Adresse, ab
  - name: 64map
    author: —
    description: Start Address for LOAD and Cassette Write
---

# STAL — I/O start address ($00C1)

## Panoramica
Il registro o area di memoria STAL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C1` (`193` decimale)
- **Range**: `$00C1`-`$00C2`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
In diesen Registern ist in LOW- und
HIGH-Byte-Darstellung angegeben, ab
welcher Adresse ein Programm geladen
oder gespeichert wird.

### C64 Programmer's Reference Guide (Commodore)
I/O Start Address

### Memory Map (Jim Butterfield)
I/O start address

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the beginning address of the area in RAM which
is currently being LOADed or SAVEd.  For tape I/O, it will point to
the cassette buffer, and the rest of the data is LOADed or SAVEd
directly to or from RAM.  This location points to the beginning
address of the area of RAM to be used for the blocks of data that come
after the initial header.

### Reference (Joe Forster / STA)
Start address during SAVE to serial bus, LOAD and VERIFY from datasette and SAVE to datasette. Pointer to current byte during memory test

### 64'er Magazin (64'er)
In diesen Speicherzellen steht in Low-/High-Byte-Darstellung die Adresse, ab
der ein Programm gerade geladen oder gespeichert wird. Diese Adresse wird
übrigens von hier auch in die Speicherzellen 172 und 173gebracht, die wir schon
früher besprochen haben.

Bei LOAD und SAVE auf Band steht hier die Anfangsadresse des Bandpuffers (828).
Im Bandpuffer steht allerdings nur der sogenannte Bandvorspann (auf englisch
»Tape Header«), während der Hauptteil des Programms im Programmspeicher ab
einer Adresse steht, auf die der Zeiger in den Speicherzellen 195 und 196
hinweist.

### 64map (—)
Start Address for LOAD and Cassette Write

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*