---
id: 0330-iload
type: entity
title: LOAD link ($F4A5)
aliases:
- LOAD link ($F4A5)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0330-iload.md
  sha256: 7221254eaba469d220ce0f11b6859a3bbf153df30cab78f8daaebb6884eca054
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0330-iload
---

# LOAD link ($F4A5)



# ILOAD — LOAD link ($F4A5) ($0330)

## Panoramica
Il registro o area di memoria ILOAD è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0330` (`816` decimale)
- **Range**: `$0330`-`$0331`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F4A5 LOAD-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL LOAD Routine

### Memory Map (Jim Butterfield)
LOAD link ($F4A5)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal LOAD Routine (Currently at 62622 ($F49E))

### Reference (Joe Forster / STA)
Default: $F4A5.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 62622 ($F49E) - beim VC 20 auf 62793
($F549). Die dort beginnende Routine transferiert Daten von einem Eingabegerät
direkt in den RAM-Speicher. Sie kann auch zum VERIFYen durch Vergleich der
geladen mit den gespeicherten Daten verwendet werden.

### 64map (—)
Vector: Indirect entry to Kernal LOAD Routine ($F4A5)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0330-iload]]
