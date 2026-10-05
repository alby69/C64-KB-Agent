---
id: ed09-command-serial-bus-device-to-talk
type: entity
title: command serial bus device to TALK
aliases:
- command serial bus device to TALK
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed09-command-serial-bus-device-to-talk.md
  sha256: 636bde41fa3b3e373314a93a86ca60737c93de1521dc093376d4695dedfbc794
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ed09-command-serial-bus-device-to-talk
---

# command serial bus device to TALK



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

## References
- Source: [[src-ed09-command-serial-bus-device-to-talk]]
