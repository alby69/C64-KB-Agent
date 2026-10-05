---
id: ee85-set-the-serial-clock-out-high
type: entity
title: set the serial clock out high
aliases:
- set the serial clock out high
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ee85-set-the-serial-clock-out-high.md
  sha256: 1e84979838b0b0a3e605ad8f28cc5270297a28b691cedf3d08b7fde952b93c50
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ee85-set-the-serial-clock-out-high
---

# set the serial clock out high



# $EE85 — set the serial clock out high

## Disassemblatura
```assembly
.EE85  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE88  29 EF    AND #$EF   ; mask xxx0 xxxx, set serial clock out high
.EE8A  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE8D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE85**: read VIA 2 DRA, serial port and video address
- **$EE88**: mask xxx0 xxxx, set serial clock out high
- **$EE8A**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EE85**: Port A laden
- **$EE88**: Bit 4 löschen
- **$EE8A**: und wieder speichern
- **$EE8D**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EE85**: serial port I/O register
- **$EE88**: clear bit4, ie. CLK out =1
- **$EE8A**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ee85-set-the-serial-clock-out-high]]
