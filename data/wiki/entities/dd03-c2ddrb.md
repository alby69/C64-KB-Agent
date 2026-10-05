---
id: dd03-c2ddrb
type: entity
title: Data Direction Register B
aliases:
- Data Direction Register B
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dd03-c2ddrb.md
  sha256: 4bf26418a8b330140b69ee509ed23eef02aee45a3d22c7e1844c045822f5c247
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dd03-c2ddrb
---

# Data Direction Register B



# C2DDRB — Data Direction Register B ($DD03)

## Panoramica
Il registro o area di memoria C2DDRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DD03` (`56579` decimale)
- **Range**: `$DD03`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Data Direction Register - Port B

### Mapping the Commodore 64 (Sheldon Leemon)
0    Select Bit 0 of data Port B for input or output (0=input, 1=output)
1    Select Bit 1 of data Port B for input or output (0=input, 1=output)
2    Select Bit 2 of data Port B for input or output (0=input, 1=output)
3    Select Bit 3 of data Port B for input or output (0=input, 1=output)
4    Select Bit 4 of data Port B for input or output (0=input, 1=output)
5    Select Bit 5 of data Port B for input or output (0=input, 1=output)
6    Select Bit 6 of data Port B for input or output (0=input, 1=output)
7    Select Bit 7 of data Port B for input or output (0=input, 1=output)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dd03-c2ddrb]]
