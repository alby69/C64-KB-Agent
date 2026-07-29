---
title: Error message link
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
  address: $0300
  address_end: $0301
  symbol: IERROR
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: indirect ERROR (output error in .X)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $E38B Vektor für BASIC-Warmstart
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: Print BASIC Error Message'
  - name: Memory Map
    author: Jim Butterfield
    description: Error message link
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Several important BASIC routines are vectored through RAM.  This
      means
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the ERROR routine at 58251
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $E38B.'
  - name: 64'er Magazin
    author: 64'er
    description: Die nächsten 12 Speicherzellen enthalten 6 Vektoren, deren Bedeutung
      bei der
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Anfangsadresse der Basic-Routine, welche
      für die
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to BASIC Error Message, (X) points to Message
      ($E38B)'
---

# IERROR — Error message link ($0300)

## Panoramica
Il registro o area di memoria IERROR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0300` (`768` decimale)
- **Range**: `$0300`-`$0301`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
indirect ERROR (output error in .X)

### Commodore-64-intern-Buch (Commodore)
$E38B Vektor für BASIC-Warmstart

### C64 Programmer's Reference Guide (Commodore)
Vector: Print BASIC Error Message

### Memory Map (Jim Butterfield)
Error message link

### Mapping the Commodore 64 (Sheldon Leemon)
Several important BASIC routines are vectored through RAM.  This means
that the first instruction executed by the routine is an indirect jump
to a location pointed to by one of the vectors in this table.

On power up, the system sets these vectors to point to the next
instruction past the original JuMP instruction.  The routine then
continues with that instruction as if the jump never took place.  For
example, the BASIC error message routine starts at 42039 ($A437) with
the instruction JMP ($0300).  The indirect vector at 768 ($0300) points
to 42042 ($A43A), which is the instruction immediately following JMP
($0300).

Although this may seem like a fancy way of accomplishing nothing,
using these indirect vectors serves two important purposes.  First, it
allows you to use these important BASIC routines without knowing their
addresses in the BASIC ROM.

For example, the routine to LIST the ASCII text of the single-byte
BASIC program token that is currently in the Accumulator (.A) is
located at one address in the VIC, and another in the 64.  On future
Commodore computers it may be found at still another location.  Yet as
long as the routine is vectored in RAM at 774 ($0306), the statement
QP=PEEK(774)+256*PEEK(775) would find the address of that routine on
any of the machines.  Thus, entering such routines through RAM vectors
rather than a direct jump into the ROMs helps to keep your programs
compatible with different machines.

The other important effect of having these vectors in RAM is that you
can alter them.  In that way, you can redirect these important BASIC
routines to execute your own preprocessing routines first.

If you wanted to add commands to BASIC, for example, how would you go
about it?  First, you would need to change the BASIC routines that
convert ASCII program text to tokenized program format, so that when a
line of program text was entered, the new keyword would be stored as a
token.

Next, you would need to change the routine that executes tokens, so
that when the interpreter comes to your new keyword token, it will
take the proper action.

You would also have to change the routine that converts tokens back to
ASCII text, so that your program would LIST the token out correctly.
And you might want to alter the routine that prints error messages, to
add new messages for your keyword.

As you will see, vectors to all of these routines can be found in the
following indirect vector table.  Changing these vectors is a much
more elegant and efficient solution than the old wedge technique
discussed at location 115 ($0073)

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the ERROR routine at 58251
($E38B).

### Reference (Joe Forster / STA)
Default: $E38B.

### 64'er Magazin (64'er)
Die nächsten 12 Speicherzellen enthalten 6 Vektoren, deren Bedeutung bei der
Übersetzung von Basic-Programmen im Texteinschub Nr. 31 »Indirekte Sprung-
Vektoren« näher erklärt wird.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Anfangsadresse der Basic-Routine, welche für die
leidigen Fehlermeldungen zuständig ist. Beim C 64 zeigt der Vektor auf 58251
($E38B), beim VC 20 auf 50234 ($C438).

Diese Routine verwendet eine Tabelle im Basic-Übersetzer, in der alle
Fehlermeldungen gespeichert sind. Sie liegt im Speicherbereich 41374 bis 41767
(beim VC 20 49566 bis 49959). Die Routine verwendet den Inhalt des X-Registers
(siehe Speicherzelle 781), um die entsprechende Fehlermeldung ganz einfach
durch Abzählen der Reihenfolge aus der Tabelle auszulesen und auf dem
Bildschirm anzuzeigen.

Ein Verbiegen dieses Vektors ist für zwei Anwendungsfälle sinnvoll. Man kann
die Fehlermeldung abschalten, um zu prüfen, ob ein bestimmtes Peripherie-Gerät,
zum Beispiel das Floppylaufwerk, angeschlossen beziehungsweise eingeschaltet
ist. Die Fehlermeldung ist abschaltbar mit POKE 768,61. Wieder eingeschaltet
wird sie mit POKE 768,139. Ein Anwendungsbeispiel habe ich bereits im
Texteinschub Nr. 14 »ST-atus« gebracht.

Die zweite Anwendung einer Verbiegung zielt auf eine Übersetzung der
Fehlermeldungen. Wem der vorgegebene englische - und manchmal nicht gerade
einleuchtende - Text der Fehlermeldungen nicht gefällt, kann den Vektor auf
einen Speicherbereich legen, in dem er seine speziellen deutschen
Fehlermeldungen speichert. Eine genaue Kenntnis der Fehlermeldungsroutine ist
dazu allerdings erforderlich.

(Die nächsten 12 Speicherzellen enthalten 6 Vektoren, deren Bedeutung bei der
Übersetzung von Basic-Programmen im Texteinschub Nr. 31 »Indirekte Sprung-
Vektoren« näher erklärt wird.)

### 64map (—)
Vector: Indirect entry to BASIC Error Message, (X) points to Message ($E38B)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*