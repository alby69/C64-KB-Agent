---
title: SYS status reg save
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $030F
  symbol: SPREG
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: .P reg
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: tatus-Register für SYS-Befehl
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Storage for 6502 .SP Register
  - name: Memory Map
    author: Jim Butterfield
    description: SYS status reg save
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The Status (.P) register has seven different flags.  Their bit
  - name: Reference
    author: Joe Forster / STA
    description: Default value of status register for SYS. Value of status register
      after SYS
  - name: 64'er Magazin
    author: 64'er
    description: Speicher für das Statusregister
  - name: 64map
    author: —
    description: Storage for 6510 Status Register during SYS
---

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