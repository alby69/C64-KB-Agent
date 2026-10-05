---
id: 02a1-enabl
type: entity
title: CIA 2 (NMI) Interrupt Control
aliases:
- CIA 2 (NMI) Interrupt Control
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/02a1-enabl.md
  sha256: e96aed9fffc8229dee3e67d3f09a8df181cd999754283720ac6be5af50cb586e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-02a1-enabl
---

# CIA 2 (NMI) Interrupt Control



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

## References
- Source: [[src-02a1-enabl]]
