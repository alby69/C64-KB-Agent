---
id: 0054-jmper
type: entity
title: Jump vector for functions
aliases:
- Jump vector for functions
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0054-jmper.md
  sha256: 0e9e1e553ba1be5d76fab86f19a444244f8e5a5b9f42cc639847a3b791cbcbd3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0054-jmper
---

# Jump vector for functions



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

## References
- Source: [[src-0054-jmper]]
