---
title: SYS X-reg save
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
  address: $030D
  symbol: SXREG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: .X reg
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: X-REG für SYS-Befehl
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Storage for 5502 .X Register
  - name: Memory Map
    author: Jim Butterfield
    description: SYS X-reg save
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Storage Area for .X Index Register
  - name: Reference
    author: Joe Forster / STA
    description: Default value of register X for SYS. Value of register X after SYS
  - name: 64'er Magazin
    author: 64'er
    description: Speicher für das X-Register
  - name: 64map
    author: —
    description: Storage for 6510 X-Register during SYS
---

# SXREG — SYS X-reg save ($030D)

## Panoramica
Il registro o area di memoria SXREG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$030D` (`781` decimale)
- **Range**: `$030D`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
.X reg

### Commodore-64-intern-Buch (Commodore)
X-REG für SYS-Befehl

### C64 Programmer's Reference Guide (Commodore)
Storage for 5502 .X Register

### Memory Map (Jim Butterfield)
SYS X-reg save

### Mapping the Commodore 64 (Sheldon Leemon)
Storage Area for .X Index Register

### Reference (Joe Forster / STA)
Default value of register X for SYS. Value of register X after SYS

### 64'er Magazin (64'er)
Speicher für das X-Register

### 64map (—)
Storage for 6510 X-Register during SYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*