---
id: ee97-set-the-serial-data-out-high
type: entity
title: set the serial data out high
aliases:
- set the serial data out high
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ee97-set-the-serial-data-out-high.md
  sha256: f902f40494f9d04b33744eb4aa30866441a4f3021d1df6eb62abad8408a3c2cc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ee97-set-the-serial-data-out-high
---

# set the serial data out high



# $EE97 — set the serial data out high

## Disassemblatura
```assembly
.EE97  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE9A  29 DF    AND #$DF   ; mask xx0x xxxx, set serial data out high
.EE9C  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE9F  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE97**: read VIA 2 DRA, serial port and video address
- **$EE9A**: mask xx0x xxxx, set serial data out high
- **$EE9C**: save VIA 2 DRA, serial port and video address

### Commodore-64-intern-Buch (Commodore)
- **$EE97**: Port A laden
- **$EE9A**: Bit 5 löschen
- **$EE9C**: und wieder speichern
- **$EE9F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EE97**: serial bus I/O register
- **$EE9A**: clear bit5
- **$EE9C**: store

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ee97-set-the-serial-data-out-high]]
