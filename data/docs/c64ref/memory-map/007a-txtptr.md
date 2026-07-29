---
title: Basic pointer (within subrtn)
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/64map.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - 64map.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - commodore-64-intern-buch.txt
  address: $007A
  address_end: $007B
  symbol: TXTPTR
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Speicherzellen wird in LOW-
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Current Byte of BASIC Text'
  - name: Memory Map
    author: Jim Butterfield
    description: Basic pointer (within subrtn)
  - name: 64map
    author: —
    description: 'Pointer: Current Byte of BASIC Text'
---

# TXTPTR — Basic pointer (within subrtn) ($007A)

## Panoramica
Il registro o area di memoria TXTPTR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$007A` (`122` decimale)
- **Range**: `$007A`-`$007B`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Commodore-64-intern-Buch (Commodore)
In diesen Speicherzellen wird in LOW-
und HIGH-Byte die Anfangsadresse des
als nächstes auszuführenden Befehls
im BASIC-RAM angegeben.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Current Byte of BASIC Text

### Memory Map (Jim Butterfield)
Basic pointer (within subrtn)

### 64map (—)
Pointer: Current Byte of BASIC Text

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*