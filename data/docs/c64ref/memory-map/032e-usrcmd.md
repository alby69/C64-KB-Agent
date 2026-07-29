---
title: Warm start vector ($FE66)
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
- fe66-warm-start-basic
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
  address: $032E
  address_end: $032F
  symbol: USRCMD
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $FE66 Warmstart-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: User-Defined Vector
  - name: Memory Map
    author: Jim Butterfield
    description: Warm start vector ($FE66)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This appears to be a holdover from PET days, when the built-in machine
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $FE66.'
  - name: 64'er Magazin
    author: 64'er
    description: Nach dem Einschalten zeigt dieser Vektor auf die BREAK-Routine, genauso
      wie der
  - name: 64map
    author: —
    description: User Defined Vector ($FE66)
---

# USRCMD — Warm start vector ($FE66) ($032E)

## Panoramica
Il registro o area di memoria USRCMD è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$032E` (`814` decimale)
- **Range**: `$032E`-`$032F`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$FE66 Warmstart-Vektor

### C64 Programmer's Reference Guide (Commodore)
User-Defined Vector

### Memory Map (Jim Butterfield)
Warm start vector ($FE66)

### Mapping the Commodore 64 (Sheldon Leemon)
This appears to be a holdover from PET days, when the built-in machine
language monitor would JuMP through the USRCMD vector when it
encountered a command that it did not understand, allowing the user to
add new commands to the monitor.

Although this vector is initialized to point to the routine called by
STOP/ RESTORE and the BRK interrupt, and is updated by the Kernal
VECTOR routine (64794, $FD1A), it does not seem to have the function
of aiding in the addition of new commands.

### Reference (Joe Forster / STA)
Default: $FE66.

### 64'er Magazin (64'er)
Nach dem Einschalten zeigt dieser Vektor auf die BREAK-Routine, genauso wie der
Vektor in Speicherzelle 790 und 791. Er ist ein Überbleibsel aus dem PET-
Betriebssystem, das aber beim VC 20 und C 64 keine Rolle spielt. Hier können
also eigene Vektoren definiert und eingesetzt werden.

### 64map (—)
User Defined Vector ($FE66)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*