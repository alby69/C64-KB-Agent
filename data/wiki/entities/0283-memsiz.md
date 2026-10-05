---
id: 0283-memsiz
type: entity
title: Top of Basic Memory
aliases:
- Top of Basic Memory
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0283-memsiz.md
  sha256: 8e44e184e7fab1a4bd9da68feb8e56f75d49a4b57cc444558f05cf99819ad70d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0283-memsiz
---

# Top of Basic Memory



# MEMSIZ — Top of Basic Memory ($0283)

## Panoramica
Il registro o area di memoria MEMSIZ è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0283` (`643` decimale)
- **Range**: `$0283`-`$0284`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Top of memory

### Commodore-64-intern-Buch (Commodore)
Dieser Zeiger wird nach einem Reset
oder einem Kaltstart auf den letzten
verfügbaren freien RAM-Speicherplatz
gesetzt.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Top of Memory for O.S

### Memory Map (Jim Butterfield)
Top of Basic Memory

### Mapping the Commodore 64 (Sheldon Leemon)
When the power is first turned on, or a cold start RESET is performed,
the Kernal routine RAMTAS (64848, $FD50) performs a nondestructive
test of RAM from 1024 ($0400) up, stopping when the test fails,
indicating the presence of ROM.  This will normally occur at 40960
($A000), the location of the BASIC ROM.  The top of user RAM pointer
is then set to point to that first ROM location.

After BASIC has been started, the system will alter this location only
when an RS-232 channel (device number 2) is OPENed or CLOSEd.  As 512
bytes of memory are required for the RS-232 transmission and reception
buffers, this pointer, as well as the end of BASIC pointer at 55
($0037), is lowered to create room for those buffers when the device is
opened.  CLOSing the device resets these pointers.

The Kernal routine MEMTOP (65061, $FE25) may be used to read or set
this pointer.

### Reference (Joe Forster / STA)
Default: $A000, 40960.

### 64'er Magazin (64'er)
Dieser Zeiger ist der Zwilling zu dem anderen Zeiger in 641 und 642. Er wird
vom Betriebssystem auf die Adresse gesetzt, welche beim Kaltstart
beziehungsweise der dabei durchgeführten Prüfung des Speichers den letzten
verfügbaren RAM-Speicherplatz angibt. Beim C 64 ist diese Adresse normalerweise
40960 ($A000), beim VC 20 ohne Erweiterung 7680.

Dieser Zeiger wird vom Basic-Übersetzer in die Speicherzelle 55 übernommen.

### 64map (—)
Pointer: Top of Memory for Operating System ($A000)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0283-memsiz]]
