---
id: 0310-usrpok
type: entity
title: USR function jump ($B248)
aliases:
- USR function jump ($B248)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0310-usrpok.md
  sha256: 3f4c773dd9f9ce2966d0cd307d7a91dac969f82ef1bf56767c4d4c9ce61d6dff
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0310-usrpok
---

# USR function jump ($B248)



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

## References
- Source: [[src-0310-usrpok]]
