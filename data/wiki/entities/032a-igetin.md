---
id: 032a-igetin
type: entity
title: GET vector ($F13E)
aliases:
- GET vector ($F13E)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/032a-igetin.md
  sha256: 2692f0f3fd33cb8a9ae91540c17882c0e02b0d02368442770a2fc495ed161e8f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-032a-igetin
---

# GET vector ($F13E)



# IGETIN — GET vector ($F13E) ($032A)

## Panoramica
Il registro o area di memoria IGETIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$032A` (`810` decimale)
- **Range**: `$032A`-`$032B`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F13E GET-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL GETIN Routine

### Memory Map (Jim Butterfield)
GET vector ($F13E)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal GETIN Routine (Currently at 61758 ($F13E))

### Reference (Joe Forster / STA)
Default: $F13E.

### 64'er Magazin (64'er)
Diese Routine ist fast identisch mit der CHRiN-Routine (siehe Speicherzellen
804 bis 805). Sie holt genauso Zeichen von angewählten Geräten in die
Eingabepuffer. Der einzige und damit wichtigste Unterschied liegt in der
Behandlung der Tastatur-Eingabe. Im Gegensatz zu CHRIN holt sie ein Byte aus
dem Tastaturpuffer sofort in den Akkumulator. Der Vektor zeigt auf den Anfang
der Routine ab Speicherzelle 61785 ($F13E) - beim VC 20 ab 61941 ($F1F5).

### 64map (—)
Vector: Indirect entry to Kernal GETIN Routine ($F13E)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-032a-igetin]]
