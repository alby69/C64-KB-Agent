---
title: OPEN vector ($F34A)
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- f34a-open
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
  address: $031A
  address_end: $031B
  symbol: IOPEN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Conforms to KERNAL spec 8/19/80
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F34A OPEN-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL OPEN Routine Vector
  - name: Memory Map
    author: Jim Butterfield
    description: OPEN vector ($F34A)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: There are 39 Kernal routines for which there are vectors in the jump
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal OPEN Routine (Currently at 62282 ($F34A))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F34A.'
  - name: 64'er Magazin
    author: 64'er
    description: Die Routine beginnt ab Adresse 62282 ($F34A) - beim VC 20 ab 62474
      ($FEAD).
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal OPEN Routine ($F34A)'
---

# IOPEN — OPEN vector ($F34A) ($031A)

## Panoramica
Il registro o area di memoria IOPEN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$031A` (`794` decimale)
- **Range**: `$031A`-`$031B`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Conforms to KERNAL spec 8/19/80

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F34A OPEN-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL OPEN Routine Vector

### Memory Map (Jim Butterfield)
OPEN vector ($F34A)

### Mapping the Commodore 64 (Sheldon Leemon)
There are 39 Kernal routines for which there are vectors in the jump
table located at the top of the ROM (65409, $FF81).  For ten of these
routines, the jump table entry contains a machine language instruction
to jump to the address pointed to by the RAM vector in this table.
The addresses in this table are initialized to point to the
corresponding routines in the Kernal ROM.  Since these addresses are
in RAM, however, any entry in this table may be changed.  This enables
the user to add to these routines, or to replace them completely.

You will notice, for example, that many of these routines involve
Input/ Output functions.  By changing the vectors  to these routines,
it is possible to support new I/O devices, such as an IEEE disk drive
used through an adapter.

The user should be cautioned that since some of these routines are
interrupt-driven, it is dangerous to change these vectors without
first turning off all interrupts.  For a safe method of changing all
of these vectors at one time, along with the interrupt vectors above,
see the entry for the Kernal VECTOR routine at 64794 ($FD1A).

More specific information about the individual routines can be found
in the descriptions given for their ROM locations.

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal OPEN Routine (Currently at 62282 ($F34A))

### Reference (Joe Forster / STA)
Default: $F34A.

### 64'er Magazin (64'er)
Die Routine beginnt ab Adresse 62282 ($F34A) - beim VC 20 ab 62474 ($FEAD).
Diese Routine prüft, ob eine Datei (File) eröffnet werden kann. Das geht immer
dann, wenn die File-Nummer nicht 0 ist und wenn weniger als 10 andere Dateien
bereits eröffnet sind. Für die serielle Schnittstelle (Geräte-Nummer 4, 5, 8
bis 11) wird an das angewählte Gerät zuerst der Befehl »Listen« gegeben und
dann die Sekundär-Adresse des OPEN-Befehls.

Beim Bandgerät (Geräte-Nummer 1) prüft die Routine den Tape Header einer
sequentiellen Datei beziehungsweise schreibt einen Tape Header auf das Band.

Bei Anwahl der RS232-Schnittstelle (Geräte-Nummer 2) aktiviert die Routine
einige Leitungen und reserviert je einen Ein- und Ausgabe-Pufferspeicheram
oberen Ende des Basic-Programmspeichers.

### 64map (—)
Vector: Indirect entry to Kernal OPEN Routine ($F34A)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*