---
id: 030d-sxreg
type: entity
title: SYS X-reg save
aliases:
- SYS X-reg save
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/030d-sxreg.md
  sha256: f8c75012dc6f6ef2784cc4a01412eb079f47e8fede9f283943af58d092b30513
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-030d-sxreg
---

# SYS X-reg save



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

## References
- Source: [[src-030d-sxreg]]
