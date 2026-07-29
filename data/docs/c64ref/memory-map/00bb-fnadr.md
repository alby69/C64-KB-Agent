---
title: Pointer to file name
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
  address: $00BB
  address_end: $00BC
  symbol: FNADR
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Addr current file name str
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Speicherzellen steht ein
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Current File Name'
  - name: Memory Map
    author: Jim Butterfield
    description: Pointer to file name
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location holds a pointer to the address of the current filename.
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to current file name or disk command; first parameter of
      LOAD, SAVE a...
  - name: 64'er Magazin
    author: 64'er
    description: Die Bedeutung eines Programm- oder Dateinamens - normalerweise kurz
      »File-Name«
  - name: 64map
    author: —
    description: 'Pointer: Current File name Address'
---

# FNADR — Pointer to file name ($00BB)

## Panoramica
Il registro o area di memoria FNADR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BB` (`187` decimale)
- **Range**: `$00BB`-`$00BC`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Addr current file name str

### Commodore-64-intern-Buch (Commodore)
In diesen Speicherzellen steht ein
Zeiger, der in LOW- und HIGH-Byte-
Darstellung auf den Filenamen zeigt.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Current File Name

### Memory Map (Jim Butterfield)
Pointer to file name

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds a pointer to the address of the current filename.
If an operation which OPENs a tape file does not specify a filename,
this pointer is not used.

When a disk filename contains a shifted space character, the remainder
of the name will appear outside the quotes in the directory, and may
be used for comments.  For example, if you SAVE "ML[shifted
space]SYS828", the directory entry will read "ML"SYS 828.  You may
reference the program either by the portion of the name that appears
within quotes, or by the full name, including the shifted space.  A
program appearing later in the directory as "ML"SYS 900 would not be
found just by reference to "ML", however.

A filename of up to four characters may be used when opening the
RS-232 device.  These four characters will be copied to 659-662
($0293-$0296), where they are used to control such parameters as baud
rate, parity, and word length.

### Reference (Joe Forster / STA)
Pointer to current file name or disk command; first parameter of LOAD, SAVE and VERIFY or fourth parameter of OPEN

### 64'er Magazin (64'er)
Die Bedeutung eines Programm- oder Dateinamens - normalerweise kurz »File-Name«
genannt - ist im Texteinschub Nr. 19 »File - Geräte - Namen - Nummern« näher
beschrieben. In den Speicherzellen 187 und 188 steht in der Low-/High-Byte-
Darstellung ein Zeiger auf diejenige Adresse im Programm-Speicher, wo dieser
Name gespeichert ist.

Eine Ausnahme ist hier der OPEN-Befehl der RS232-Schnittstelle. Ihr File-Name
wird in die Speicherzellen 659 bis 662 gebracht, wo er verschiedene Parameter
dieser Schnittstelle steuert.

### 64map (—)
Pointer: Current File name Address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*