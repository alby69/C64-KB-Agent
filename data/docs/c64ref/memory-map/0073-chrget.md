---
title: CHRGET subroutine; get Basic char
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
related:
- 0073-chrget
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
  address: $0073
  address_end: $008A
  symbol: CHRGET
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: This code gets changed throughout execution.
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Routine holt ein Zeichen aus dem
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Subroutine: Get Next Byte of BASIC Text'
  - name: Memory Map
    author: Jim Butterfield
    description: CHRGET subroutine; get Basic char
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This is actually a machine language subroutine, which at the time
      of a
  - name: Reference
    author: Joe Forster / STA
    description: CHRGET. Machine code routine to read next byte from BASIC program
      or direct c...
  - name: 64'er Magazin
    author: 64'er
    description: Die Problematik der Übersetzung von Basic-Befehlen und Anweisungen
      besteht
  - name: 64map
    author: —
    description: ',0073  INC $7A'
---

# CHRGET — CHRGET subroutine; get Basic char ($0073)

## Panoramica
Il registro o area di memoria CHRGET è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0073` (`115` decimale)
- **Range**: `$0073`-`$008A`
- **Dimensione**: `24 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
This code gets changed throughout execution.
It is made to be fast this way.
Also, [X] and [Y] are not disturbed.

"CHRGET" using [TXTPTR] as the current text pntr,
fetches a new character into ACCA after incrementing [TXTPTR]
and sets condition codes according to what's in ACCA.

* not C = numeric ("0" thru "9")
* Z = ":" or end-of-line (a null)

[ACCA] = new char.

[TXTPTR]=[TXTPTR]+1

The following exists in ROM if ROM exists and is loaded
down here by init. Otherwise it is just loaded into this
RAM like all the rest of RAM is loaded.

### Commodore-64-intern-Buch (Commodore)
Diese Routine holt ein Zeichen aus dem
BASIC-Text.

### C64 Programmer's Reference Guide (Commodore)
Subroutine: Get Next Byte of BASIC Text

### Memory Map (Jim Butterfield)
CHRGET subroutine; get Basic char

### Mapping the Commodore 64 (Sheldon Leemon)
This is actually a machine language subroutine, which at the time of a
BASIC cold start (such as when the power is turned on) is copied from
MOVCHG (58274, $E3A2) in the ROM to this zero page location.

CHRGET is a crucial routine which BASIC uses to read text characters,
such as the text of the BASIC program which is being interpreted.  It
is placed on zero page to make the routine run faster.  Since it keeps
track of the address of the character being read within the routine
itself, the routine must be in RAM in order to update that pointer.
The pointer to the address of the byte currently being read is really
the operand of a LDA instruction.  When entered from CHRGET, the
routine increments the pointer by modifying the operand at TXTPTR
(122, $007A), thus allowing the next character to be read.

Entry at CHRGOT (121, $0079) allows the current character to be read
again.  The CHRGET routine skips spaces, sets the various flags or the
status register (.P) to indicate whether the character read was a
digit, statement terminator, or other type of character, and returns
with the retrieved character in the Accumulator (.A).

Since CHRGET is used to read every BASIC statement before it is
executed, and since it is in RAM, and therefore changeable, it makes a
handy place to intercept BASIC to add new features and commands (and
in the older PET line, it was the only way to add such features).
Diversion of the CHRGET routine for this purpose is generally referred
to as a wedge.

Since a wedge can greatly slow down execution speed, most of the time
it is set up so that it performs its preprocessing functions only when
in direct or immediate mode.  The most well-known example of such a
wedge is the "Universal DOS Support" program that allows easier
communication with the disk drive command channel.

As this is such a central routine, a disassembly listing is given
below to provide a better understanding of how it works.

    115 $73   CHRGET  INC TXTPTR   ; increment low byte of TXTPTR
    117 $75           BNE CHRGOT   ; if low byte isn't 0, skip next
    119 $77           INC TXTPTR+1 ; increment high byte of TXTPTR
    121 $79   CHRGOT  LDA          ; load byte from where TXTPTR points
                                   ; entry here does not update TXTPTR,
                                   ; allowing you to read the old byte again
    122 $7A   TXTPTR  $0207        ; pointer is really the LDA operand
                                   ; TXTPTR+1 points to 512-580 ($0200-$0250)
                                   ; when reading from the input buffer
                                   ; in direct mode
    124 $7C   POINTB  CMP #$3A     ; carry flag set if > ASCII numeral 9
    126 $7E           BCS EXIT     ; character is not a numeral--exit
    128 $80           CMP #$20     ; if it is an ASCI space...
    130 $82           BEQ CHRGET   ; ignore it and get next character
    132 $84           SEC          ; prepare to subtract
    133 $85           SBC #$30     ; ASCII 0-9 are between 48-57 ($30-$39)
    135 $87           SEC          ; prepare to subtract again
    136 $88           SBC #$D0     ; if < ASCII 0 (57, $39) then carry is set
    138 $8A   EXIT    RTS          ; carry is clear only for numeral on return

The Accumulator (.A register) holds the character that was read on
exit from the routine.  Status register (.P) bits which can be tested
for on exit are:

* Carry Clear if the character was an ASCII digit 0-9.
* Carry Set, otherwise.
* Zero Set only if the character was a statement terminator 0 or an
  ASCII colon, 58 ($3A).
* Zero Clear, otherwise.


One wedge insertion technique is to change CHRGET's INC $7A to a JMP
WEDGE, have your wedge update TXTPTR itself, and then JSR CHRGOT.
Another is to change the CMP #$3A at location 124 ($007C), which I have
labeled POINTB, to a JMP WEDGE, do your wedge processing, and then
exit through the ROM version of POINTB, which is located at 48283
($E3AB).  For more detailed information about wedges, see Programming
the PET/CBM, Raeto Collin West, pages 365-68.

While the wedge is a good, quick technique for adding new commands, a
much more elegant method exists for accomplishing this task on the
VIC-20 and 64 without slowing BASIC down to the extent that the wedge
does.  See the entries for the BASIC RAM vector area at 768-779
($0300-$030B) for more details.

### Reference (Joe Forster / STA)
CHRGET. Machine code routine to read next byte from BASIC program or direct command (24 bytes)

### 64'er Magazin (64'er)
Die Problematik der Übersetzung von Basic-Befehlen und Anweisungen besteht
darin, daß die Übersetzungsschritte durch entsprechende Programmteile des
Basic-Übersetzers im Computer fest vorprogrammiert sein müssen, was bedeutet,
daß diese Programme natürlich im - nicht veränderbaren - ROM stehen.

Auf der anderen Seite verlangt aber der Übersetzungsvorgang, daß gewisse Teile
dieser Programme sich laufend verändern. Als Beispiel soll der Zeiger
herhalten, der angibt, in welcher Speicherzelle das nächste zu bearbeitende
Zeichen steht. Dieser Zeiger und die zusammengehörigen Programmschritte dürfen
natürlich nicht im ROM stehen, denn da sind sie ja nicht änderbar.

Dieser Konflikt wird dadurch gelöst, daß dieses »variable« Teilprogramm des
Übersetzers zwar im ROM steht (im C 64 ab 58274 oder $E3A2, im VC 20 ab 58247
oder $E387), von wo es aber direkt nach dem Einschalten des Computers in das
RAM, und zwar in die Speicherzellen 115 bis 138, umgeladen wird.

Dieses Teilprogramm, welches die Zeichen zur Übersetzung herbeiholt und
deswegen »Character-Get« oder kurz CHARGET-Routine genannt wird, ist wegen
seiner Veränderbarkeit natürlich ein beliebtes Objekt aller möglichen
Manipulationen. Es ist deshalb im Assembler-Kurs, Teil 5, im 64’er, Ausgabe
1/85, im Detail beschrieben worden, allerdings mit Schwerpunkt auf Assembler-
Maschinensprache.

Für Basic-Programmierer möchte ich hier deshalb eine kurze Beschreibung der
CHARGET-Routine einfügen.

Die Routine beginnt mit einem Sprung auf den oben schon erwähnten Zeiger in
Adresse 122 und 123, welcher seinerseits auf die Adresse zeigt, in welcher das
nächste zu übersetzende Zeichen steht. Das Zeichen wird entsprechend dem
Hinweis des Zeigers geholt, in den Akkumulator des Mikroprozessors geladen und
dort verschiedenen Prüfungen unterzogen. Ist das Zeichen ein Gänsefuß, erkennt
das Programm, wie es das nächste Zeichen interpretieren und behandeln muß. Ein
Doppelpunkt leitet einen neuen Befehl ein, eine Leerstelle wird unterdrückt und
so weiter.

Mit dem Befehl

    PRINT PEEK(122)+256*PEEK(123)

können wir innerhalb eines Programms ausdrucken, wohin der Zeiger nach dem
letzten Basic-Zeichen deutet. Eine Überprüfung mit den Methoden, die ich bei
der Besprechung der Speicherzellen 43 bis 56 genannt habe, zeigt Ihnen den
Zusammenhang.

Normalerweise wird der Zeiger in 122 und 123 nach jedem Zeichen um 1 erhöht, da
ja die Zeichen einer Basic-Zeile hintereinander im Speicher stehen. Ein GOTO-
oder GOSUB-Befehl kann diese Folge natürlich unterbrechen, ebenso wie eine
willkürliche Änderung durch einen Eingriff von außen.

Ein derartiger Eingriff, auch »wedge« (Keil) genannt, öffnet natürlich Tür und
Tor für Programmiertricks, insbesondere für Einbau von neuen, selbsterfundenen
Befehlen. Man kann entweder den allerersten Sprungbefehl auf den Zeiger so
umlenken, daß er auf ein eigenes Maschinenprogramm springt, oder man kann den
Zeiger selbst »verbiegen«, so daß er auf eine andere Adresse und damit auf ein
anderes Zeichen zeigt. Es gibt dafür viele Möglichkeiten, die aber alle nur in
Maschinencode funktionieren. Theoretisch können wir natürlich den Inhalt des
Zeigers in 122 und 123 durch POKE verändern. Aber was dann? Jeder nachfolgende
Basic-Befehl löst natürlich wieder die normale Übersetzungsroutine aus und
unser schöner POKE ist für die Katz.

Wie ein Wedge in Maschinensprache gemacht wird, hat Christoph Sauer im VC 20-
Kurs - 64’er, Ausgabe 9/84 beschrieben. Allerdings ist das Beispiel für
Anfänger nicht verständlich, was mich zu der Überzeugung bringt, daß die
CHARGET-Routine und ihre Anwendung einen eigenen Aufsatz wert wäre.

### 64map (—)
,0073  INC $7A
    ,0075  BNE $0079
    ,0077  INC $7B
    ,0079  LDA $0801
    ,007C  CMP #$3A
    ,007E  BCS $008A
    ,0080  CMP #$20
    ,0082  BEQ $0073
    ,0084  SEC
    ,0085  SBC #$30
    ,0087  SEC
    ,0088  SBC #$D0
    ,008A  RTS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*