---
title: 'Accum#l : Exponent'
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
  address: $0061
  symbol: FACEXP
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: The floating accumulator
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: This is where temp descs are built
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Register werden für die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Floating-Point Accumulator #1: Exponent'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Accum#l : Exponent'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The Floating Point Accumulator is central to the execution of any
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This exponent represents the closest power of two to the number,
      with
  - name: Reference
    author: Joe Forster / STA
    description: 'FAC, arithmetic register #1 (5 bytes)'
  - name: 64'er Magazin
    author: 64'er
    description: »Akkumulator« heißt seit der Zeit der mechanischen Rechenmaschinen
      eine
  - name: 64map
    author: —
    description: Main Floating point Accumulator
  - name: 64map
    author: —
    description: FAC Exponent
---

# FACEXP — Accum#l : Exponent ($0061)

## Panoramica
Il registro o area di memoria FACEXP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0061` (`97` decimale)
- **Range**: `$0061`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
The floating accumulator

### Original Source Comments (Microsoft/Commodore)


### Original Source Comments (Microsoft/Commodore)
This is where temp descs are built

### Commodore-64-intern-Buch (Commodore)
Diese Register werden für die
Berechnung von Fließkommazahlen
verwendet.

### C64 Programmer's Reference Guide (Commodore)
Floating-Point Accumulator #1: Exponent

### Memory Map (Jim Butterfield)
Accum#l : Exponent

### Mapping the Commodore 64 (Sheldon Leemon)
The Floating Point Accumulator is central to the execution of any
BASIC mathematical operation.  It is used in the conversion of
integers to floating point numbers, strings to floating point numbers,
and vice versa.  The results of most evaluations are stored in this
location.

The internal format of floating point numbers is not particularly easy
to understand (or explain).  Generally speaking, the number is broken
into the normalized mantissa, which represents a number between 1 and
1.99999..., and an exponent value, which represents a power of 2.
Multiplying the mantissa by 2 raised to the value of the exponent
gives you the value of the floating point number.

Fortunately, the BASIC interpreter contains many routines for the
manipulation and conversion of floating point number, and these
routines can be called by the user.  See the entries for locations 3
and 5

Floating Point Accumulator #1 can be further divided into the
following locations:

### Mapping the Commodore 64 (Sheldon Leemon)
This exponent represents the closest power of two to the number, with
129 added to take care of the sign problem for negative exponents.  An
exponent of 128 is used for the value 0; an exponent of 129 represents
2 to the 0 power, or 1; an exponent of 130 represents 2 to the first
power, or 2; 131 is 2 squared, or 4; 132 is 2 cubed, or 8; and so on.

### Reference (Joe Forster / STA)
FAC, arithmetic register #1 (5 bytes)

### 64'er Magazin (64'er)
»Akkumulator« heißt seit der Zeit der mechanischen Rechenmaschinen eine
Speicherzelle, welche bei Rechenoperationen dadurch im Mittelpunkt steht, daß
laufend Daten in sie hineingeschrieben beziehungsweise aus ihr herausgelesen
werden.

Normalerweise trägt diesen Namen das zentrale Rechenregister des
Mikroprozessors. Leser des Assembler-Kurses kennen diesen Akkumulator
inzwischen zur Genüge.

Die Speicherzellen 97 bis 102 werden deswegen ebenfalls Akkumulator genannt,
weil sie bei der Verarbeitung von Gleitkommazahlen eine ähnliche zentrale Rolle
spielen.

Zelle 97 enthält den Exponenten. Die Zellen 98 bis 101 enthalten die Mantisse.

Zelle 102 enthält das Vorzeichen der Gleitkommazahl. Eine 0 bedeutet ein
positives, die Zahl 255 ein negatives Vorzeichen.

Mit dem Gleitkomma-Akkumulator Nr. 1 sind zwei weitere Speicherzellen eng
verbunden, nämlich 104 ($0068) und 112 ($0070).

Ganz zum Schluß ist noch erwähnenswert, daß nach der Umwandlung einer
Gleitkommazahl in eine ganze Zahl diese als Low-/High-Byte in den beiden
Speicherzellen 98 und 99 steht, was für Maschinenprogramme vielleicht recht
nützlich sein kann.

### 64map (—)
Main Floating point Accumulator

### 64map (—)
FAC Exponent

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*