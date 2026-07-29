---
title: Jump vector for functions
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
  address: $0054
  address_end: $0056
  symbol: JMPER
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier ist die Konstante für JMP ($4C)
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Jump Vector used in Function Evaluation- JMP followed by Address
      ($4C,$LB,$MB)
  - name: Memory Map
    author: Jim Butterfield
    description: Jump vector for functions
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The first byte is the 6502 JMP instruction ($4C), followed by the
  - name: Reference
    author: Joe Forster / STA
    description: JMP ABS machine instruction, jump to current BASIC function
  - name: 64'er Magazin
    author: 64'er
    description: Jede Basic-Funktion, wie zum Beispiel SGN, INT, ABS, USR und so weiter,
      wird
  - name: 64map
    author: —
    description: Jump Vector used in Function Evaluation - JMP followed by Address
      ($4C,$LB,$MB)
---

# JMPER — Jump vector for functions ($0054)

## Panoramica
Il registro o area di memoria JMPER è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0054` (`84` decimale)
- **Range**: `$0054`-`$0056`
- **Dimensione**: `3 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
Hier ist die Konstante für JMP ($4C)
festgelegt.

### C64 Programmer's Reference Guide (Commodore)
Jump Vector used in Function Evaluation- JMP followed by Address ($4C,$LB,$MB)

### Memory Map (Jim Butterfield)
Jump vector for functions

### Mapping the Commodore 64 (Sheldon Leemon)
The first byte is the 6502 JMP instruction ($4C), followed by the
address of the required function taken from the table at 41042
($A052).

### Reference (Joe Forster / STA)
JMP ABS machine instruction, jump to current BASIC function

### 64'er Magazin (64'er)
Jede Basic-Funktion, wie zum Beispiel SGN, INT, ABS, USR und so weiter, wird
durch ein spezielles Teilprogramm (Routine) des Basic-Übersetzers ausgeführt.
Die Anfangsadresse jeder dieser Routinen sind in einer Tabelle im ROM fest
eingespeichert. Im VC 20 steht diese Tabelle von 49234 bis 49279 ($C052 bis
$C07F), im C 64 von 41042 bis 41087 ($A052 bis $A07F).

In der Speicherzelle 84 steht der Sprungbefehl JMP in Maschinencode,
dargestellt durch die Zahl 75 ($4C). In den beiden anderen Zellen 85 und 86
steht dann in Low-/High-Byte-Darstellung die jeweilige Adresse in der Tabelle,
welche der vom Programm gerade gebrauchten Basic-Funktion entspricht. Dieser
gesamte Befehl JMP plus Adresse entspricht in Basic der GOSUB-Zeilennummer.

Ein Beispiel soll das verdeutlichen. Geben Sie direkt ein:

    PRINT PEEK(84) ;PEEK(85); PEEK(86)

Wir erhalten

* beim C 64: 76 13 184
* beim VC 20: 76 13 216

Die erste Zahl ist genauso wie oben beschrieben. Die beiden anderen Zahlen
ergeben zusammen die Adresse 47117 ($B80D) beziehungsweise 55309 ($D80D). Wenn
Sie ein Buch mit ROM-Listing haben, werden Sie unter dieser Adresse die Routine
für die Funktion »PEEK« finden. Das ist natürlich nicht erstaunlich, haben wir
doch gerade vorher als letzten Befehl genau diese Funktion eingegeben.

Leider ist das auch die einzige Funktion, die ich Ihnen vorführen kann, denn
zum Vorführen muß ich eben immer PEEKen, so daß beim besten Willen immer nur
die oben angegebenen Zahlen erscheinen können.

### 64map (—)
Jump Vector used in Function Evaluation - JMP followed by Address ($4C,$LB,$MB)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*