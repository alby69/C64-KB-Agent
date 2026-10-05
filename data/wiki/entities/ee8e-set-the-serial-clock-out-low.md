---
id: ee8e-set-the-serial-clock-out-low
type: entity
title: set the serial clock out low
aliases:
- set the serial clock out low
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ee8e-set-the-serial-clock-out-low.md
  sha256: 06bb563caf58c988798364b01458bb7f83b64c1961788f8b2b1911875573d34f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ee8e-set-the-serial-clock-out-low
---

# set the serial clock out low



# $EE8E — set the serial clock out low

## Disassemblatura
```assembly
.EE8E  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE91  09 10    ORA #$10   ; mask xxx1 xxxx, set serial clock out low
.EE93  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE96  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE8E**: read VIA 2 DRA, serial port and video address
- **$EE91**: mask xxx1 xxxx, set serial clock out low
- **$EE93**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EE8E**: Port A laden
- **$EE91**: Bit 4 setzen
- **$EE93**: und wieder speichern
- **$EE96**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EE8E**: serial port I/O register
- **$EE91**: set bit4, ie. CLK out =0
- **$EE93**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ee8e-set-the-serial-clock-out-low]]
