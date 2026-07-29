---
title: CIA 2 (NMI) Interrupt Control
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
  address: $02A1
  symbol: ENABL
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RS-232 enables (replaces ier)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle erhält den Wert
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: RS-232 Enables
  - name: Memory Map
    author: Jim Butterfield
    description: CIA 2 (NMI) Interrupt Control
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 'This location holds the active NMI interrupt flag byte from CIA
      #2'
  - name: Reference
    author: Joe Forster / STA
    description: Temporary area for saving original value of CIA#2 interrupt control
      register,...
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle enthält den Wert des Interrupt-Steuerregisters
      56589, das
  - name: 64map
    author: —
    description: RS232 Enables
---

# ENABL — CIA 2 (NMI) Interrupt Control ($02A1)

## Panoramica
Il registro o area di memoria ENABL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$02A1` (`673` decimale)
- **Range**: `$02A1`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 enables (replaces ier)

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle erhält den Wert
des Interruptsteuerregisters, das die
RS-232 Schnittstelle steuert.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Enables

### Memory Map (Jim Butterfield)
CIA 2 (NMI) Interrupt Control

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the active NMI interrupt flag byte from CIA #2
Interrupt Control Register (56589, $DD0D).  The bit values for this
flag are as follows:

|Bit|Value| |
|---|-----|-|
| 4 | 16  | 1 = System is Waiting for Receiver Edge |
| 1 | 2   | 1 = System is Receiving Data            |
| 0 | 1   | 1 = System is Transmitting Data         |

### Reference (Joe Forster / STA)
Temporary area for saving original value of CIA#2 interrupt control register, at memory address $DD0D, during RS232 input/output

### 64'er Magazin (64'er)
Diese Speicherzelle enthält den Wert des Interrupt-Steuerregisters 56589, das
die RS232-Schnittstelle steuert. Die Bedeutung der einzelnen Bits, wenn sie auf
1 gesetzt sind, zeigt Tabelle 15. Diese Flagge kann zu Steuerzwecken abgefragt
werden. Um beispielsweise ein Programm warten zu lassen, bis der
Ausgabepufferspeicher geleert ist, gibt man die Anweisung

    100 IF (PEEK(673) AND 1) THEN 100

die das Programm so lange aufhält, bis die Übertragung abgeschlossen und Bit O
der Flagge gelöscht ist.

Die folgenden 4 Speicherzellen, nämlich 674 bis 678, werden nur vom C 64
benutzt. Beim VC 20 sind sie nicht belegt und können frei verwendet werden.

### 64map (—)
RS232 Enables

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*