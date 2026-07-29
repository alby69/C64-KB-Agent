---
title: 'Pointer : Start-of-Basic'
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
  address: $002B
  address_end: $002C
  symbol: TXTTAB
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Doesn't change after being
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Der Anfangsbereich des BASIC ist in
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Start of BASIC Text'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pointer : Start-of-Basic'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This two-byte pointer lets BASIC know where program text is stored.
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $0801, 2049.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger, in der Low-/High-Byte-Darstellung, gibt dem Basic-Übersetzer
      an,
  - name: 64map
    author: —
    description: 'Pointer: Start of BASIC Text Area ($0801)'
---

# TXTTAB — Pointer : Start-of-Basic ($002B)

## Panoramica
Il registro o area di memoria TXTTAB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$002B` (`43` decimale)
- **Range**: `$002B`-`$002C`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Doesn't change after being
setup by "INIT".

### Commodore-64-intern-Buch (Commodore)
Der Anfangsbereich des BASIC ist in
Low- und Highbyte angegeben. Man kann
durch die beiden Bytes den BASIC-Start
abfragen oder verändern.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Start of BASIC Text

### Memory Map (Jim Butterfield)
Pointer : Start-of-Basic

### Mapping the Commodore 64 (Sheldon Leemon)
This two-byte pointer lets BASIC know where program text is stored.
Ordinarily, such text is located beginning at 2049 ($0801).  Using this
pointer, it is possible to change the program text area.  Typical
reasons for doing this include:

1.  Conforming the memory configuration to that of other Commodore
computers.  On 32K PET and CBM computers, for example, screen memory
starts at 32768 ($8000), and BASIC text begins at 1025 ($0401).  You
can emulate this configuration with the 64 with the following short
program:

        10 POKE 55,0:POKE 56,128: CLR: REM LOWER TOP OF MEMORY TO 32768
        20 POKE 56576,PEEK(56576) AND 253: REM ENABLE BANK 2
        30 POKE 53272,4: REM TEXT DISPLAY MEMORY NOW STARTS AT 32768
        40 POKE 648,128:REM OPERATING SYSTEM PRINTS TO SCREEN AT 32768 (128*256)
        50 POKE 44,4:POKE 1024,0: REM MOVE START OF BASIC TO 1025 (4*256+1)
        60 POKE 792,193: REM DISABLE RESTORE KEY
        70 PRINT CHR$(147);"NOW CONFIGURED LIKE PET":NEW
        80 REM ALSO SEE ENTRIES FOR LOCATION 55, 56576, AND 648

Such reconfiguring can be helpful in transferring programs from the 64
to the PET, or vice versa.  Since the 64 automatically relocates BASIC
program text, it can load and list PET programs even though the
program file indicates a loading address that is different from the
64 start of BASIC.  The PET does not have this automatic relocation
feature, however, and it loads all BASIC programs at the two-byte
address indicated at the beginning of the disk or tape file.

So if the PET loads a 64 program at its normal starting address of
2049 ($0801), it will not recognize its presence because it expects a
BASIC program to start at 1025 ($0401).  Therefore, if you want to let
a PET and 64 share a program, you must either reconfigure the 64 to
start BASIC where the PET does, or reconfigure the PET to start BASIC
where the 64 does (with a POKE 41,8:POKE 2048,0).

2.  Raising the lowest location used for BASIC text in order to create
a safe area in low memory.  For example, if you wish to use the
high-resolution graphics mode, you may want to put the start of screen
memory at 8192 ($2000).  The high-resolution mode requires 8K of
memory, and you cannot use the lowest 8K for this purpose because it
is already being used for the zero-page assignments.

Since BASIC program text normally starts at 2048 ($0801), this means
that you only have 6k for program text before your program runs over
into screen memory.  One way around this is by moving the start of
basic to 16385 ($4001) by typing in direct entry mode:

    POKE 44,64: POKE 64*256,0:NEW

Other uses might include setting aside a storage area for sprite shape
data, or user-defined character sets.

3.  Keeping two or more programs in memory simultaneously.  By
changing this pointer, you can keep more than one BASIC program in
memory at one time, and switch back and forth between them.  Examples
of this application can be found in COMPUTE!'s First Book of PET/CBM,
pages 66 and 163.

This technique has a number of offshoots that are perhaps of more
practical use.

a) You can store two programs in memory simultaneously for the purpose
of appending one to the other.  This technique requires that the line
numbers of the two programs do not overlap.  (See Programming the
PET/CBM by Raeto Collin West, pages 41-42, for a discussion of this
technique).

b) You can have two programs in memory at once and use the concept in
(2) above to allow an easier way to create a safe area in low memory.
The first program is just one line that sets the start of BASIC
pointer to the address of the second program which is located higher
in memory, and then runs that second program.

4. Since this address is used as the address of the first byte to
SAVE, you can save any section of memory by changing this pointer to
indicate the starting address, and the pointer 45-46 ($002D-$002D) to
indicate the address of the byte after the last byte that you wish to
save.

### Reference (Joe Forster / STA)
Default: $0801, 2049.

### 64'er Magazin (64'er)
Dieser Zeiger, in der Low-/High-Byte-Darstellung, gibt dem Basic-Übersetzer an,
ab welcher Speicherzelle das Basic-Programm beginnt. Normalerweise ist diese
Adresse fest vorgegeben. Beim C 64 zum Beispiel zeigt der Zeiger auf 2049
($0801). Beim VC 20 ist die Lage schon schwieriger, denn der Speicherbeginn
hängt davon ab, welche Speichererweiterung eingesetzt ist. Die folgende Tabelle
3 gibt darüber Auskunft.

Tabelle 3: Beginn des Programmspeichers

| C 64          | 2049 ($0801) |
|---------------|--------------|
| VC 20 (GV)    | 4097 ($1001) |
| VC 20 (+3 K)  | 1025 ($0401) |
| VC 20 (+ 8 K) | 4609 ($1201) |

Mit dem Befehl

    PRINT PEEK (43) + PEEK (44)*256

läßt sich der jeweilige Beginn des Programmspeichers leicht feststellen. Mit
einem POKE-Befehl kann der Programmierer diese Anfangsadresse verändern. Wozu
das gut ist, fragen Sie?

##### Anwendung #1:

Nun, wenn Sie zum Beispiel ein Maschinenprogramm mit einem Basic-Programm
gemeinsam betreiben wollen, brauchen Sie einen Speicherbereich für das
Maschinenprogramm, der vom Basic-Programm nicht belegt wird. Wir sprechen vom
»Schützen des Maschinenprogramms vor dem Überschreiben durch das Basic«. Der
Speicherbereich eines Maschinenprogramms ist immer bekannt. Nach seinem letzten
Speicherplatz kann das Basic-Programm beginnen.

Die Verschiebung der Anfangsadresse erfolgt in vier Schritten:

1. Schritt: In den Speicherplatz vor dem neuen Basic-Bereich muß eine Null
   gePOKEt werden. Die Null dient zum Abgrenzen.
2. Schritt: Die Adresse der ersten Speicherzelle wird in die Low-/High-Byte-
   Darstellung umgerechnet. Ich verweise dazu auf die Erklärung dieses Vorgangs
   im Texteinschub Nr. 1.
3. Schritt: Das Low-Byte wird in die Speicherzelle 43, das High-Byte in die
   Zelle 44 gePOKEt.
4. Schritt: Die Operation muß unbedingt mit dem Befehl NEW abgeschlossen
   werden, um sicherzustellen, daß auch alle anderen Zeiger auf ihren
   Anfangszustand gesetzt werden.

Im folgenden kleinen Programm wird angenommen, daß der Speicher bis zur Adresse
6000 ($1388) durch ein Maschinenprogramm belegt ist. Das Basic-Programm kann
daher ab 5002 ($138A) anfangen, denn in 5001 muß ja eine Null stehen. Die
Adresse 5002 teilt sich auf in ein High-Byte von INT (5002/256) = 19 und ein
Low-Byte von 5002-(19*256) = 138.

    10 POKE 5001,0
    20 POKE 43,138
    30 POKE 44,19
    40 NEW

Der Effekt einer solchen »Verbiegung« des Zeigers in 43 und 44 wird im
Texteinschub Nr. 7 »Der sichtbare Basic-Speicher« demonstriert.

Neben der oben erwähnten Anwendung der Zeigerverbiegung gibt es noch andere
Möglichkeiten:

##### Anwendung #2:

Christoph Sauer hat in seinem Kurs »Der gläserne VC 20« in Ausgabe 10/84 auf
Seite 158 gezeigt, wie man mehrere Programme gleichzeitig im Speicher
unterbringen und zwischen ihnen umschalten kann.

##### Anwendung #3:

Man kann zwei oder mehrere unabhängige Programme genau hintereinander in den
Speicher bringen, um sie aneinander zu hängen, was dem im Commodore-Basic
fehlenden Befehl MERGE entspricht. Dabei dürfen die Zeilennummern sich
allerdings nicht überschneiden.

##### Anwendung #4:

Durch Hinaufschieben des Basic-Bereichs kann Platz geschaffen werden für
selbstdefinierte Zeichen oder hochauflösende Grafik.

Die Speicherzellen-Paare von 45, 46 bis 55, 56 ($0037 bis $0038) zeigen auf weitere
für Basic-Programme wichtige Speicherbereiche, die deswegen gemeinsam
betrachtet werden sollten. Bild 5 stellt den Zusammenhang grafisch dar. In
diesem Bereich werden alle Variablen eines Programms gespeichert. Zur
Erinnerung:

Wir unterscheiden zwischen »normalen« Variablen (numerische und String-
Variable) und Feld-Variablen (Arrays). Dabei ist wichtig zu wissen, daß ein
Basic-Programm während des Eintippens oder Einladens von Disk beziehungsweise
Kassette in den 1. Block kommt. Während des Programmlaufs werden alle normalen
Variablen in den 2. Block geschrieben, alle Felder (Arrays) in den 3. Block und
schließlich der Text der Zeichenketten (Strings) sozusagen rückwärts vom Ende
des Arbeitsspeichers in den 4 . Block. Je nach Größe des Programms und nach
Anzahl der Variablen wandern die Blockgrenzen nach oben beziehungsweise die von
Block 4 nach unten. Wenn sie sich treffen beziehungsweise überschneiden, gibt
es »OUT OF MEMORY«.

Diese Blockbewegung ist in Bild 5 durch die Pfeile dargestellt.

### 64map (—)
Pointer: Start of BASIC Text Area ($0801)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*