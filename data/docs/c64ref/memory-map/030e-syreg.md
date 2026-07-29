---
title: SYS Y-reg save
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
  address: $030E
  symbol: SYREG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: .Y reg
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Y-REG für SYS-Befehl
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Storage for 6502 .Y Register
  - name: Memory Map
    author: Jim Butterfield
    description: SYS Y-reg save
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Storage Area for .Y Index Register
  - name: Reference
    author: Joe Forster / STA
    description: Default value of register Y for SYS. Value of register Y after SYS
  - name: 64'er Magazin
    author: 64'er
    description: Speicher für das Y-Register
  - name: 64map
    author: —
    description: Storage for 6510 Y-Register during SYS
---

# SYREG — SYS Y-reg save ($030E)

## Panoramica
Il registro o area di memoria SYREG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$030E` (`782` decimale)
- **Range**: `$030E`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
.Y reg

### Commodore-64-intern-Buch (Commodore)
Y-REG für SYS-Befehl

### C64 Programmer's Reference Guide (Commodore)
Storage for 6502 .Y Register

### Memory Map (Jim Butterfield)
SYS Y-reg save

### Mapping the Commodore 64 (Sheldon Leemon)
Storage Area for .Y Index Register

### Reference (Joe Forster / STA)
Default value of register Y for SYS. Value of register Y after SYS

### 64'er Magazin (64'er)
Speicher für das Y-Register

### 64map (—)
Storage for 6510 Y-Register during SYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*