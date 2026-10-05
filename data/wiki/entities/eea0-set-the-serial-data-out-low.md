---
id: eea0-set-the-serial-data-out-low
type: entity
title: set the serial data out low
aliases:
- set the serial data out low
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eea0-set-the-serial-data-out-low.md
  sha256: 42c06ea0aa2a2964133493bd53098e3d130672289896a7f66413a25aa7525324
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-eea0-set-the-serial-data-out-low
---

# set the serial data out low



# $EEA0 — set the serial data out low

## Disassemblatura
```assembly
.EEA0  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EEA3  09 20    ORA #$20   ; mask xx1x xxxx, set serial data out low
.EEA5  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EEA8  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEA0**: read VIA 2 DRA, serial port and video address
- **$EEA3**: mask xx1x xxxx, set serial data out low
- **$EEA5**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EEA0**: Port A laden
- **$EEA3**: Bit 5 setzen
- **$EEA5**: und wieder speichern
- **$EEA8**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EEA0**: serial bus I/O resister
- **$EEA3**: set bit 5
- **$EEA5**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-eea0-set-the-serial-data-out-low]]
