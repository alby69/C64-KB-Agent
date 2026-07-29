---
title: Data Direction Register B
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- cia-registers
difficulty: intermediate
language: assembly
hardware:
- CIA
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $DC03
  symbol: CIDDRB
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Data Direction Register - Port B (56321)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: 0    Select Bit 0 of Data Port B for input or output (0=input, 1=output)
---

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