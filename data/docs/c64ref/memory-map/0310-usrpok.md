---
title: USR function jump ($B248)
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
- b248-error-illegal-quantity
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0310
  address_end: $0312
  symbol: USRPOK
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: user function dispatch
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: USR Function Jump Instr (4C)
  - name: Memory Map
    author: Jim Butterfield
    description: USR function jump ($B248)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The value here (67, $4C) is first part of the 6510 machine language
  - name: Reference
    author: Joe Forster / STA
    description: JMP ABS machine instruction, jump to USR() function
  - name: 64'er Magazin
    author: 64'er
    description: Mit dem Basic-Befehl USR wird bekanntlich ein Maschinenprogramm gestartet.
  - name: 64map
    author: —
    description: USR Function JMP Instruction ($4C)
---

# USRPOK — USR function jump ($B248) ($0310)

## Panoramica
Il registro o area di memoria USRPOK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0310` (`784` decimale)
- **Range**: `$0310`-`$0312`
- **Dimensione**: `3 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
user function dispatch

### C64 Programmer's Reference Guide (Commodore)
USR Function Jump Instr (4C)

### Memory Map (Jim Butterfield)
USR function jump ($B248)

### Mapping the Commodore 64 (Sheldon Leemon)
The value here (67, $4C) is first part of the 6510 machine language
JuMP instruction for the USR command.

### Reference (Joe Forster / STA)
JMP ABS machine instruction, jump to USR() function

### 64'er Magazin (64'er)
Mit dem Basic-Befehl USR wird bekanntlich ein Maschinenprogramm gestartet.
Diese drei Speicherzellen werden bei der Abwicklung von USR verwendet. In ihnen
muß der Anwender des USR-Befehls die Zieladresse in Low-/High-Byte-Darstellung
angeben, ab der das Maschinenprogramm im Speicher steht.

Dieser Vorgang ist bereits behandelt worden bei den Speicherzellen 0 bis 2 des
VC 20, die ja genau den Speicherzellen 784 bis 786 des C 64 entsprechen.

Speziell für den C 64 ist der USR-Befehl noch einmal behandelt, und zwar im
Texteinschub Nr. 34 »Das Mauerblümchen USR«.

(Diese drei Speicherzellen 784 bis 786 sind beim VC 20 nicht belegt. Beim C 64
entsprechen sie den Adressen 0 bis 2 des VC 20.)

### 64map (—)
USR Function JMP Instruction ($4C)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*