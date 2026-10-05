---
id: d40c-atdcy2
type: entity
title: Voice 2 Attack/Decay Register
aliases:
- Voice 2 Attack/Decay Register
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d40c-atdcy2.md
  sha256: e3d4525509def08f4406158fef83bed162abef3e772be74c43020724dfe57c48
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d40c-atdcy2
---

# Voice 2 Attack/Decay Register



# ATDCY2 — Voice 2 Attack/Decay Register ($D40C)

## Panoramica
Il registro o area di memoria ATDCY2 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D40C` (`54284` decimale)
- **Range**: `$D40C`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7-4  Select Attack Cycle Duration: 0-15
3-0  Select Decay Cycle Duration: 0-15

### Mapping the Commodore 64 (Sheldon Leemon)
0-3  Select decay cycle duration (0-15)
4-7  Select attack cycle duration (0-15)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d40c-atdcy2]]
