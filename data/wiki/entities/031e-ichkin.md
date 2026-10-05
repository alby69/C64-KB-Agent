---
id: 031e-ichkin
type: entity
title: Set - input vector ($F20E)
aliases:
- Set - input vector ($F20E)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/031e-ichkin.md
  sha256: e569eefacf692c124a612eba1d1b3c269917cce1859e1b7a0a77a2c3f7f541b4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-031e-ichkin
---

# Set - input vector ($F20E)



# ICHKIN — Set - input vector ($F20E) ($031E)

## Panoramica
Il registro o area di memoria ICHKIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$031E` (`798` decimale)
- **Range**: `$031E`-`$031F`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F20E CHKIN-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CHKIN Routine

### Memory Map (Jim Butterfield)
Set - input vector ($F20E)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CHKIN Routine (Currently at 61966 ($F20E))

### Reference (Joe Forster / STA)
Default: $F20E.

### 64'er Magazin (64'er)
Diese Routine beginnt ab Adresse 61966 ($F20E) - beim VC 20 ab 62161 ($F2C7).
Sie eröffnet einen Datenkanal zur Übernahme von Daten von dem Gerät, das durch
den OPEN-Befehl angegeben worden ist.

### 64map (—)
Vector: Indirect entry to Kernal CHKIN Routine ($F20E)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-031e-ichkin]]
