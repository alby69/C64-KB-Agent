---
id: 030e-syreg
type: entity
title: SYS Y-reg save
aliases:
- SYS Y-reg save
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/030e-syreg.md
  sha256: a078b799488c7fe67132945a927d4280d66b3edb169588a6adc327be6e634a38
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-030e-syreg
---

# SYS Y-reg save



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

## References
- Source: [[src-030e-syreg]]
