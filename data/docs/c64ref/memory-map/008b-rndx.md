---
title: RND seed value
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
  address: $008B
  address_end: $008F
  symbol: RNDX
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Registern wird der letzte
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Floating RND Function Seed Value
  - name: Memory Map
    author: Jim Butterfield
    description: RND seed value
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location holds the five-byte floating point value returned by
      the
  - name: Reference
    author: Joe Forster / STA
    description: Previous result of RND()
  - name: 64'er Magazin
    author: 64'er
    description: Mit dem Befehl RND(X) kann bekanntlich eine Zufallszahl erzeugt werden.
      Was das
  - name: 64map
    author: —
    description: Floating RND Function Seed Value
---

# RNDX — RND seed value ($008B)

## Panoramica
Il registro o area di memoria RNDX è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$008B` (`139` decimale)
- **Range**: `$008B`-`$008F`
- **Dimensione**: `5 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
In diesen Registern wird der letzte
RND-Wert im Fließkommaformat abgelegt.

### C64 Programmer's Reference Guide (Commodore)
Floating RND Function Seed Value

### Memory Map (Jim Butterfield)
RND seed value

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the five-byte floating point value returned by the
RND function.  It is initially set to a seed value copied from ROM
(the five bytes are 128, 79, 199, 82, 88--$80, $4F, $C7, $52, $58).

When the function RND(X) is called, the numeric value of X does not
affect the number returned, but its sign does.  If X is equal to 0,
RND generates a seed value from chip-level hardware timers.  If X is a
positive number, RND(X) will return the next number in an arithmetic
sequence.  This sequence continues for such a long time without
repeating itself, and gives such an even distribution of numbers, that
it can be considered random.  If X is negative, the seed value is
changed to a number that corresponds to a scrambled floating point
representation of the number X itself.

Given a particular seed value, the same pseudorandom series of numbers
will always be returned.  This can be handy for debugging purposes,
but not where you wish to have truly random numbers.

The traditional Commodore method of selecting a random seed is by
using the expression RND(-TI), mostly because RND(0) didn't function
correctly on early PETs.  While the RND(0) form doesn't really work
right on the 64 either (see location 57495 ($E097)), the expression
RND(-RND(0)) may produce a more random seed value.

### Reference (Joe Forster / STA)
Previous result of RND()

### 64'er Magazin (64'er)
Mit dem Befehl RND(X) kann bekanntlich eine Zufallszahl erzeugt werden. Was das
bedeutet und wie »zufällig« diese Zahlen sind, können Sie dem Texteinschub Nr.
13 »Wie zufällig sind Zufallszahlen?« entnehmen.

Beim Einschalten des Computers werden die Zahlen 128, 79, 199, 82 und 88 in
diese Speicherzellen geschrieben. Mit der folgenden Zeile können Sie das gleich
nach dem Einschalten des Computers leicht überprüfen.

    FOR X=139 TO 143:PRINT PEEK(X):NEXT

Nach den Manipulationen des RND-Befehls wird das Resultat wieder in die Zellen
139 bis 143 als neuer Ausgangswert (seed) für den nächsten RND-Befehl gebracht.

Diese fünf Zahlen stellen eine Gleitkommazahl dar. Ihre Form entspricht dabei
der Aufteilung, wie sie auch im Gleitkomma-Akkumulator (97 bis 101) verwendet
wird.

Eine Abfrage dieser Zahlen aus den Zellen 139 bis 143 ist natürlich möglich,
aber nicht ergiebig, weil das Resultat von RND(X) direkt als Zahl verfügbar
ist, während die 5 Byte erst in eine brauchbare Zahl umgerechnet werden müßten.
Eine Änderung durch POKEn neuer Werte in diese Speicherzellen geht leider
nicht.

### 64map (—)
Floating RND Function Seed Value

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*