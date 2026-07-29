---
title: 'Pointer : Start-of-Arrays'
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
  address: $002F
  address_end: $0030
  symbol: ARYTAB
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Incremented by 6 whenever
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Das LOW- und HIGH-Byte der Adressen
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Start of BASIC Arrays'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pointer : Start-of-Arrays'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the address of the end of nonarray variable
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to beginning of array variable area
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger, in der Low-/High-Byte-Darstellung, gibt dem Basic-Übersetzer
  - name: 64map
    author: —
    description: 'Pointer: Start of BASIC Arrays'
---

# ARYTAB — Pointer : Start-of-Arrays ($002F)

## Panoramica
Il registro o area di memoria ARYTAB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$002F` (`47` decimale)
- **Range**: `$002F`-`$0030`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Incremented by 6 whenever
a new simple variable is found, and
set to [VARTAB] by "CLEARC".

### Commodore-64-intern-Buch (Commodore)
Das LOW- und HIGH-Byte der Adressen
geben dem BASIC-Interpreter die
Information, ab welcher Speicherzelle
die Arrays eines BASIC-Programms
gespeichert sind.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Start of BASIC Arrays

### Memory Map (Jim Butterfield)
Pointer : Start-of-Arrays

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address of the end of nonarray variable
storage, and the beginning of array variable storage.  The format for
array storage is as follows:

The first two bytes hold the array name.  The format and high-bit
patterns are the same as for nonarray variables (see 45 ($002D) above),
except that there is no equivalent to the function definition.

Next comes a two-byte offset to the start of the next array, low byte
first.  Then there is a one-byte value for the number of array
dimensions (e.g., 2 for a two-dimensional array like A(x,y)).  That
byte is followed by pairs of bytes which hold the value of each array
dimension+1 (DIMensioning an array always makes space for 0, so A(0)
can be used).

Finally come the values of the variables themselves.  The format for
these values is the same as with nonarray values, but each value only
takes up the space required; that is, floating point variables use
five bytes each, integers two bytes, and string descriptors three
bytes each.

Remember that as with nonarray string, the actual string text is
stored elsewhere, in the area which starts at the location pointed to
in 51-52 ($0033-$0034).

### Reference (Joe Forster / STA)
Pointer to beginning of array variable area

### 64'er Magazin (64'er)
Dieser Zeiger, in der Low-/High-Byte-Darstellung, gibt dem Basic-Übersetzer
(Interpreter) an, ab welcher Speicherzelle die Felder (Arrays) eines Basic-
Programms gespeichert sind. Was Felder sind und wozu sie gebraucht werden, ist
im Texteinschub Nr. 10 kurz erläutert. Da die Felder direkt nach den normalen
Variablen gespeichert werden, zeigt dieser Zeiger natürlich gleichzeitig auf
das Ende des Speichers für normale Variablen.

Durch POKEn einer Adresse in die Speicherzellen 47 und 48 kann der
Speicherbereich am Anfang eines Programms beinahe beliebig verschoben werden.
Beinahe deswegen, weil die Verschiebung im Zusammenhang mit den anderen
Bereichen (siehe Bild 5) einen Sinn haben muß. Im übrigen gilt für diesen
Zeiger dasselbe, was schon für den Zeiger in 45 und 46 gesagt worden ist. Die
Darstellung der Feld-Variablen selbst kann mit der Methode angesehen werden,
die im Texteinschub Nr. 11 erklärt ist.

Wie aus den Erklärungen hervorgeht, wird bei Feldern mit Zeichenketten
(Strings) in dem von Zeiger 47 und 48 bezeichneten Speicherbereich nur die
Definition beziehungsweise die Dimensionierung gespeichert. Die eigentlichen
Zeichenketten stehen wie bei den normalen Variablen im vierten Block, vorn
Speicherende rückwärts angeordnet.

### 64map (—)
Pointer: Start of BASIC Arrays

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*