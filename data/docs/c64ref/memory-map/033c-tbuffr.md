---
title: Cassette buffer
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
  address: $033C
  address_end: $03FB
  symbol: TBUFFR
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: cassette data b
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Bandpuffer
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Tape I/O Buffer
  - name: Memory Map
    author: Jim Butterfield
    description: Cassette buffer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This 192-byte buffer area is used to temporarily hold data that is
  - name: Reference
    author: Joe Forster / STA
    description: Datasette buffer (192 bytes)
  - name: 64'er Magazin
    author: 64'er
    description: Diese 192 Byte beherbergen den Kassettenpuffer. Der Name kennzeichnet
      diesen
  - name: 64map
    author: —
    description: Tape I/O Buffer
---

# TBUFFR — Cassette buffer ($033C)

## Panoramica
Il registro o area di memoria TBUFFR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$033C` (`828` decimale)
- **Range**: `$033C`-`$03FB`
- **Dimensione**: `192 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
cassette data b

### Commodore-64-intern-Buch (Commodore)
Bandpuffer

### C64 Programmer's Reference Guide (Commodore)
Tape I/O Buffer

### Memory Map (Jim Butterfield)
Cassette buffer

### Mapping the Commodore 64 (Sheldon Leemon)
This 192-byte buffer area is used to temporarily hold data that is
read from or written to the tape device (device number 1).

When not being used for tape I/O, the cassette buffer has long been a
favorite place for Commodore programmers to place short machine
language routines (although the 64 has 4K of unused RAM above the
BASIC ROM at 49152 ($C000) that would probably better serve the
purpose).

Of more practical interest to the 64 programmer is the possible use of
this area for VIC-II chip graphics memory (for example, sprite shape
data or text character dot data).  If the VIC-II chip is banked to the
lowest 16K of memory (as is the default selection), there is very
little memory space which can be used for such things as sprite shape
data without conflict.  If the tape is not in use, locations 832-895
($0340-$037F) can be used as sprite data block number 13, and locations
896-959 ($0380-$03BF) can be used as sprite data block number 14.

The types of tape blocks that can be stored here are program header
blocks, data header blocks, and data storage blocks.

The first byte of any kind of block (which is stored at location 828
($033C)) identifies the block type.  Header blocks follow this
identifier byte with the two-byte starting RAM address of the tape
data, the two-byte ending RAM address, and the filename, padded with
blanks so that the total length of the name portion equals 187 bytes.
Data storage blocks have 191 bytes of data following the identifier
byte.  The meanings of the various identifier blocks are as follows:

A value of 1 signifies that the block is the header for a relocatable
program file, while a value of 3 indicates that the block is the
header for a nonrelocatable program file.

A relocatable file is created when a program is SAVEd with a secondary
address of 0 (or any even number), while a nonrelocatable program file
is created if the secondary SAVE address is 1 (or any odd number).
The difference between the two types of files is that a nonrelocatable
program will always load at the address specified in the header.  A
relocatable program will load at the current start of BASIC address
unless the LOAD statement uses a secondary address of 1, in which case
it will also be loaded at the address specified in the header.

You should note that a program file uses the cassette buffer only to
store the header block.  Actual program data is transferred directly
to or from RAM, without first being buffered.

An identifier value of 4 means that the block is a data file header.
Such a header block is stored in the cassette buffer whenever a BASIC
program OPENs a tape data file for reading or writing.  Subsequent
data blocks start with an identifier byte of 2.  These blocks contain
the actual data byte written by the PRINT #1 command, and read by the
GET #1 and INPUT #1 commands.  Unlike the body of a program file,
these blocks are temporarily stored in the cassette buffer when being
written or read.

An identifier byte of 5 indicates that this block is the logical end
of the tape.  This signals the Kernal not to search past this point,
even if there are additional tape blocks physically present on the
tape.

### Reference (Joe Forster / STA)
Datasette buffer (192 bytes)

### 64'er Magazin (64'er)
Diese 192 Byte beherbergen den Kassettenpuffer. Der Name kennzeichnet diesen
Speicherbereich als Zwischenspeicher für Ein- und Ausgabe-Operationen von und
auf Band.

Dabei unterscheiden sich die normalen LOAD-, SAVE- und VERIFY-Befehle von den
Datei-Befehlen INPUT#, GET# und PRINT#.

Bei LOAD, SAVE und VERIFY steht im Kassettenpuffer lediglich der Vorspann, der
auf englisch »Tape Header« heißt. Die Funktion und Zusammensetzung des Tape
Headers habe ich schon bei den Speicherzellen 183 bis 187 und im Texteinschub
Nr. 20 »Tape Header« detailliert beschrieben. Die eigentlichen Daten berühren
den Kassettenpuffer nicht, sondern werden direkt von und in den RAM-Speicher
transferiert.

Bei GET#, INPUT# und PRINT# werden nicht nur der Tape Header, sondern auch alle
Daten im Kassettenpuffer zwischengespeichert. Dieser blockweise Transport ist
an den charakteristischen Unterbrechungen des Datasettenmotors leicht zu
erkennen.

Der Kassettenpuffer kann durch Verbiegen der Zeiger in Speicherzelle 178 und
179 auf beliebige Plätze des Speichers, aber nicht unterhalb 512, geschoben
werden. Normalerweise gibt das keinen Sinn, es sei denn, der Speicherbereich
828 bis 1019 wurde mit einem eigenen Maschinenprogramm belegt, und durch das
Verschieben des Kassettenpuffers in höhere Regionen möchte man das
Maschinenprogramm vor der Zerstörung durch ungeplante Datasetten-Operationen
schützen.

Die Kenntnis der Inhalte der Speicherzellen des Kassettenpuffers kann man
ausnutzen, um die ärgerlichen LOAD ERROR-Probleme zu lösen. Die Methode dazu
ist im Texteinschub Nr. 36 »Reparatur von LOAD ERROR« beschrieben.

Ist die Datasette nicht angeschlossen, oder wird sie nicht eingesetzt, kann der
Speicherbereich des Kassettenpuffers als freier Speicher benutzt werden.

### 64map (—)
Tape I/O Buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*