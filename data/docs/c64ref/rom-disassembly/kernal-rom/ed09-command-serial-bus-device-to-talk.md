---
title: command serial bus device to TALK
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bit
- ed09-talk-senden
- talk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $ED09
  address_end: $ED0B
  symbol: command-serial-bus-device-to-talk
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ED09**: OR with the TALK command'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$ED09**: Bit für Talk setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$ED09**: set TALK flag'
---

# $ED09 — command serial bus device to TALK

## Disassemblatura
```assembly
.ED09  09 40    ORA #$40   ; OR with the TALK command
.ED0B  2C       .BYTE $2C   ; makes next line BIT $2009
```


## Commenti

### Original Disassembly (—)
- **$ED09**: OR with the TALK command
- **$ED0B**: makes next line BIT $2009

### Commodore-64-intern-Buch (Commodore)
- **$ED09**: Bit für Talk setzen
- **$ED0B**: Skip nach $ED0E

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$ED09**: set TALK flag
- **$ED0B**: bit $2009, mask ORA command
- **$ED0C**: set LISTEN flag
- **$ED0E**: check serial bus idle
- **$ED12**: C3PO, character in serial buffer
- **$ED14**: nope
- **$ED16**: prepare for ROR
- **$ED17**: temp data area
- **$ED19**: send data to serial bus
- **$ED1C**: 3CPO
- **$ED21**: BSOUR, buffered character for bus
- **$ED24**: set data 1, and clear serial bit count
- **$ED27**: UNTALK?
- **$ED29**: nope
- **$ED2B**: set CLK 1
- **$ED2E**: serial bus I/O port
- **$ED31**: clear ATN, prepare for command
- **$ED33**: store
- **$ED36**: disable interrupts
- **$ED37**: set CLK 1
- **$ED3A**: set data 1
- **$ED3D**: delay 1 ms

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*