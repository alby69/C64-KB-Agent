---
id: d413-atdcy3
type: entity
title: Voice 3 Attack/Decay Register
aliases:
- Voice 3 Attack/Decay Register
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d413-atdcy3.md
  sha256: f85b2511e1134ad13dde15ee52735ab1c288629a0db83b6467204d27d8933a83
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d413-atdcy3
---

# Voice 3 Attack/Decay Register



# ATDCY3 — Voice 3 Attack/Decay Register ($D413)

## Panoramica
Il registro o area di memoria ATDCY3 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D413` (`54291` decimale)
- **Range**: `$D413`
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
- Source: [[src-d413-atdcy3]]
