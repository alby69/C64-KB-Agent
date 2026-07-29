---
title: Print tokens link
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
  address: $0306
  address_end: $0307
  symbol: IQPLOP
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: indirect LIST (char list)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $A71A Vektor für Umwandlung in Klartext (LIST)
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: BASIC Text LIST'
  - name: Memory Map
    author: Jim Butterfield
    description: Print tokens link
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the QPLOP routine at 42778
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $A71A.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Adresse 42778 ($A71A), beim VC 20 auf
      50970
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to BASIC LIST Routine ($A71A)'
---

# IQPLOP — Print tokens link ($0306)

## Panoramica
Il registro o area di memoria IQPLOP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0306` (`774` decimale)
- **Range**: `$0306`-`$0307`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
indirect LIST (char list)

### Commodore-64-intern-Buch (Commodore)
$A71A Vektor für Umwandlung in Klartext (LIST)

### C64 Programmer's Reference Guide (Commodore)
Vector: BASIC Text LIST

### Memory Map (Jim Butterfield)
Print tokens link

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the QPLOP routine at 42778
($A71A).

### Reference (Joe Forster / STA)
Default: $A71A.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 42778 ($A71A), beim VC 20 auf 50970
($C71A). Dort beginnt eine Routine, die Token wieder in LISTbaren Text
umwandelt. Sie steht nicht allein, sondern wird als Unterprogramm von der LIST-
Routine verwendet.

Falls ein Programmierer spezielle zusätzliche Basic-Befehle erfunden hat, kann
er durch Verbiegen dieses Vektors seine eigenen Token lesbar ausLISTen.

Man kann auch durch eine entsprechende Verbiegung erreichen, daß die LIST-
Routine nicht angesprungen werden kann, was gleichbedeutend ist mit einer LIST-
Sperre. Das ist aber wohl nur sinnvoll bei einem Autostart-Programm.

Besser finde ich da ein kleines Programm, das J. Pellechi in der Zeitschrift
RUN, Ausgabe 6/85 (Seite 10), angegeben hat:

    10 FOR J=679 TO 688
    20 READ K
    30 POKE J,K
    40 NEXT J
    50 POKE 774,167:POKE 775,2
    60 NEW
    70 DATA 72,173,141
    80 DATA 2,208,251,104
    90 DATA 76,26,167

Beim VC 20 ist nur die Zeile 90 verschieden:

    90 DATA 76,26,199

In den freien Speicherbereich ab Speicherzelle 679 wird ein kleines
Maschinenprogramm gePOKEt, das in den DATA-Zeilen 70 bis 90 steht. In Zeile 50
steht der für unser Beispiel entscheidende Befehl: Der Vektor in 774 und 775
wird nach der Adresse 679 verbogen. Dadurch springt die LIST-Routine immer
zuerst auf die Adresse 679, in der sie das kleine Maschinenprogramm findet.

Disassembliert schaut das so aus:

    02A7 48	PHA
    02A8 AD 8D 02  LDA 028D
    02AB D0 FB     BNE 02A8
    02AD 68	PLA
    02AE 4C 1A A7  JMP A71A

Zuerst wird der Akkumulator mit dem Inhalt der Speicherzelle 653 ($028D)
geladen. Dort steht bekanntlich eine Zahl von 1 bis 7, je nachdem, ob die
SHIFT-, CTRL- oder Commodore-Taste gedrückt ist. Ist dies der Fall, springt das
Programm auf die Adresse 680 zurück und bildet so eine Dauerschleife, bis die
Taste wieder losgelassen wird. Erst dann geht es weiter mit der ursprünglichen
Zieladresse des Vektors in 774 und 775, nämlich $A71A (42778) beziehungsweise
$C71A (50970) beim VC 20.

Auf diese Weise können Sie das LISTen eines Programms mit einer der drei
genannten Tasten anhalten.

### 64map (—)
Vector: Indirect entry to BASIC LIST Routine ($A71A)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*