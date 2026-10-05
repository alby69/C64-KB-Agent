---
id: dc03-ciddrb
type: entity
title: Data Direction Register B
aliases:
- Data Direction Register B
tags:
- cia-registers
- io-map
sources:
- path: data/docs/c64ref/io-map/cia/dc03-ciddrb.md
  sha256: 19afa9a602df611e96c54875a50de57752b9f0585b64076c294fdf03eb6f5040
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-dc03-ciddrb
---

# Data Direction Register B



# CIDDRB — Data Direction Register B ($DC03)

## Panoramica
Il registro o area di memoria CIDDRB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$DC03` (`56323` decimale)
- **Range**: `$DC03`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Data Direction Register - Port B (56321)

### Mapping the Commodore 64 (Sheldon Leemon)
0    Select Bit 0 of Data Port B for input or output (0=input, 1=output)
1    Select Bit 1 of Data Port B for input or output (0=input, 1=output)
2    Select Bit 2 of Data Port B for input or output (0=input, 1=output)
3    Select Bit 3 of Data Port B for input or output (0=input, 1=output)
4    Select Bit 4 of Data Port B for input or output (0=input, 1=output)
5    Select Bit 5 of Data Port B for input or output (0=input, 1=output)
6    Select Bit 6 of Data Port B for input or output (0=input, 1=output)
7    Select Bit 7 of Data Port B for input or output (0=input, 1=output)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-dc03-ciddrb]]
