---
id: 030f-spreg
type: entity
title: SYS status reg save
aliases:
- SYS status reg save
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/030f-spreg.md
  sha256: 5fb644b97718a61ba9bb05926ccaaefd9974557e3ab7e946fe124631e824d9d8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-030f-spreg
---

# SYS status reg save



# SPREG — SYS status reg save ($030F)

## Panoramica
Il registro o area di memoria SPREG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$030F` (`783` decimale)
- **Range**: `$030F`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
.P reg

### Commodore-64-intern-Buch (Commodore)
tatus-Register für SYS-Befehl

### C64 Programmer's Reference Guide (Commodore)
Storage for 6502 .SP Register

### Memory Map (Jim Butterfield)
SYS status reg save

### Mapping the Commodore 64 (Sheldon Leemon)
The Status (.P) register has seven different flags.  Their bit
assignments are as follows:

|Bit|Value|                   |
|---|-----|-------------------|
| 7 | 128 | Negative          |
| 6 | 64  | Overflow          |
| 5 | 32  | Not Used          |
| 4 | 16  | BREAK             |
| 3 | 8   | Decimal           |
| 2 | 4   | Interrupt Disable |
| 1 | 2   | Zero              |
| 0 | 1   | Carry             |

If you wish to clear any flag before a SYS, it is safe to clear them
all with a POKE 783,0.  The reverse is not true, however, as you must
watch out for the Interrupt disable flag.

A 1 in this flag bit is equal to an SEI instruction, which turns off
all IRQ interrupts (like the one that reads the keyboard, for
example).  Turning off the keyboard could make the computer very
difficult to operate!  To set all flags except for Interrupt disable
to 1, POKE 783,247.

### Reference (Joe Forster / STA)
Default value of status register for SYS. Value of status register after SYS

### 64'er Magazin (64'er)
Speicher für das Statusregister

### 64map (—)
Storage for 6510 Status Register during SYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-030f-spreg]]
