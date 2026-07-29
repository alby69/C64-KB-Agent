---
title: Top of Basic Memory
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
  address: $0283
  address_end: $0284
  symbol: MEMSIZ
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Top of memory
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieser Zeiger wird nach einem Reset
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Top of Memory for O.S'
  - name: Memory Map
    author: Jim Butterfield
    description: Top of Basic Memory
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: When the power is first turned on, or a cold start RESET is performed,
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $A000, 40960.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger ist der Zwilling zu dem anderen Zeiger in 641 und 642.
      Er wird
  - name: 64map
    author: —
    description: 'Pointer: Top of Memory for Operating System ($A000)'
---

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