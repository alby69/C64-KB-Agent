---
title: 'Pointer : Start-of-Variables'
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
  address: $002D
  address_end: $002E
  symbol: VARTAB
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Updated whenever the size of the
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieser Zeiger teilt dem Interpreter
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Start of BASIC Variables'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pointer : Start-of-Variables'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the address which marks the end of the BASIC
  - name: Reference
    author: Joe Forster / STA
    description: (End of program plus 1.)
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger, in der Low/High-Byte-Darstellung, gibt dem Basic-Interpreter
  - name: 64map
    author: —
    description: 'Pointer: Start of BASIC Variables'
---

# VARTAB — Pointer : Start-of-Variables ($002D)

## Panoramica
Il registro o area di memoria VARTAB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$002D` (`45` decimale)
- **Range**: `$002D`-`$002E`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Updated whenever the size of the
program changes, set to [TXTTAB]
by "SCRATCH" ("NEW").

### Commodore-64-intern-Buch (Commodore)
Dieser Zeiger teilt dem Interpreter
das BASIC-Ende mit, damit die
Variablen hinter dem Programm abgelegt
werden können.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Start of BASIC Variables

### Memory Map (Jim Butterfield)
Pointer : Start-of-Variables

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address which marks the end of the BASIC
program text area, and the beginning of the variable storage area.
All nonarray variables are stored here, as are string descriptors (for
the address of the area where the actual text of strings is stored,
see location 51 ($0033)).

Seven bytes of memory are allocated for each variable.  The first two
bytes are used for the variable name, which consists of the ASCII
value of the first two letters of the variable name.  If the variable
name is a single letter, the second byte will contain a zero.

The seventh bit of one or both of these bytes can be set (which would
add 128 to the ASCII value of the letter).  This indicates the
variable type.  If neither byte has the seventh bit set, the variable
is the regular floating point type.  If only the second byte has its
seventh bit set, the variable is a string.  If only the first byte
has its seventh bit set, the variable is a defined function (FN).  If
both bytes have the seventh bit set, the variable is an integer.

The use of the other five bytes depends on the type of variable.  A
floating point variable will use the five bytes to store the value of
the variable in floating point format.  An integer will have its value
stored in the third and fourth bytes, high byte first, and the other
three will be unused.

A string variable will use the third byte for its length, and the
fourth and fifth bytes for a pointer to the address of the string
text, leaving the last two bytes unused.  Note that the actual string
text that is pointed to is located either in the part of the BASIC
program where the string is first assigned a value, or in the string
text storage area pointed to by location 51 ($0033).

A function definition will use the third and fourth bytes for a
pointer to the address in the BASIC program text where the function
definition starts.  It uses the fifth and sixth bytes for a pointer to
the dependent variable (the X of FN A(X)).  The final byte is not
used.

Knowing something about how variables are created can help your BASIC
programming.  For example, you can see that nonarray integer variables
take up no less space than floating point variables, and since most
BASIC commands convert the integers to floating point, they do not
offer a speed advantage either, and in many cases will actually slow
the program down.  As will be seen below, however, integer arrays can
save a considerable amount of space.

Variables are stored in the order in which they are created.
Likewise, when BASIC goes looking for a variable, it starts its search
at the beginning of this area.  If commonly used variables are defined
at the end of the program, and are thus at the back of this area, it
will take longer to find them.  It may help program execution speed to
define the variables that will be used most frequently right at the
beginning of the program.

Also, remember that once created, variables do not go away during
program execution.  Even if they are never used again, they still take
up space in the variable storage area, and they slow down the routine
that is used to search for variables that are referenced.

Another point to consider about the order in which to define variables
is that arrays are created in a separate area of memory which starts
at the end of the nonarray variable area.  Therefore, every time a
nonarray variable is created, all of the arrays must be moved seven
bytes higher in memory in order to make room for the new variable.
Therefore, it may help performance to avoid defining nonarray
variables after defining arrays.

This pointer will be reset to one byte past the end of the BASIC
program text whenever you execute the statements CLR, NEW, RUN, or
LOAD.  Adding or modifying a BASIC statement will have the same
effect, because the higher numbered BASIC statements have to be moved
up into memory to make room for the new statements, and can therefore
overwrite the variable storage area.  This means that if you wish to
check the value of a variable after stopping a program, you can only
do so before modifying the program.

The exception to the above is when the LOAD command is issued from a
program.  The purpose of not resetting this pointer in such a case is
to allow the chaining of programs by having one program load and then
run the next (that is also why a LOAD issued from a program causes a
RUN from the beginning of the program).  This allows the second
program to share variables with the first.  There are problems with
this, however.  Some string variable descriptors and function
definitions have their pointers set to areas within the program text.
When this text is replaced by a load, these pointers are no longer
valid, which will lead to errors if the FN or string value is
referenced.  And if the second program text area is larger than that
of the first, the second program will overwrite some of the first
program's variables, and their values will be lost.

The ability to chain short programs is a holdover from the days of the
8K PET, for which this BASIC was written, but with the vastly
increased memory of the 64, program chaining should not be necessary.

You should also note that SAVE uses this pointer as the address of the
byte after the last byte to SAVE.

### Reference (Joe Forster / STA)
(End of program plus 1.)

### 64'er Magazin (64'er)
Dieser Zeiger, in der Low/High-Byte-Darstellung, gibt dem Basic-Interpreter
an, ab welcher Speicherzelle die Variablen eines Basic-Programms gespeichert
sind. Da die Variablen direkt an das Basic-Programm anschließen, zeigt dieser
Zeiger natürlich gleichzeitig auf das Ende des Basic-Programms.

Es muß betont werden, daß es sich nur um den Bereich der »normalen« Variablen
handelt, also nicht um Felder (Arrays). Anders als der Zeiger in 43 und 44, der
auf fest definierte Speicherzellen zeigt, liegt derZeiger für den Variablen-
Beginn nicht fest. Je nach Länge des Programms wandert er nach oben.

Sobald ein Programm eingetippt oder aus einem externen Speicher (Diskette,
Kassette) eingelesen ist, wird der Zeiger in 45 und 46 durch RUN auf ein Byte
hinter das Programmende gesetzt und alle Variablen werden in der Reihenfolge
ihres Auftretens gespeichert. Da normalerweise die Länge eines Basic-Programms
während des Ablaufs konstant bleibt, werden die Variablen in ihrer Position
auch nicht gestört.

Das bedeutet, daß sie sowohl vom Programm als auch vom Programmierer nach einer
Unterbrechung abgefragt werden können. Nur wenn das Programm modifiziert wird,
wandert der Zeiger zusammen mit den Variablen entsprechend weiter.

Denselben Effekt wie das oben erwähnte RUN haben übrigens auch die Befehle NEW,
CLR und LOAD. Eine Ausnahme bildet das LOAD innerhalb eines Programms, welches
den Zeiger nicht zurücksetzt. Dadurch wird ein Aneinanderhängen von mehreren
Programmen samt Variablen-Weiterverwendung unter bestimmten Voraussetzungen
ermöglicht.

Die Bearbeitung der Variablen durch das Basic-Programm und die daraus
resultierenden Kochrezepte für den Programmierer sind im Texteinschub Nr. 8
»Normale Variable in BASIC« separat erläutert.

Die verschiedenen Typen der Variablen und ihre Darstellung im Speicher finden
Sie im 64’er, Ausgabe 10/84, Seite 157 und noch ausführlicher in Ausgabe 11/84,
Seite 124, dargestellt und erklärt.

Für diejenigen Leser, welche kein Monitor- beziehungsweise Disassembler-
Programm haben oder benutzen können, ist im Texteinschub Nr. 9 »Darstellung der
normalen Variablen im Speicher« eine kleine Anleitung gegeben, wie sie die
Variablendarstellung mittels Basic anschauen können.

### 64map (—)
Pointer: Start of BASIC Variables

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*