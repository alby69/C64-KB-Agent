---
id: eea9-get-the-serial-data-status-in-cb
type: entity
title: get the serial data status in Cb
aliases:
- get the serial data status in Cb
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eea9-get-the-serial-data-status-in-cb.md
  sha256: e80f5e9a7a516a3d440b44dd7b41f8c9668d6f2529b9ab0b83c095940f14856c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-eea9-get-the-serial-data-status-in-cb
---

# get the serial data status in Cb



# $EEA9 — get the serial data status in Cb

## Disassemblatura
```assembly
.EEA9  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EEAC  CD 00 DD CMP $DD00   ; compare it with itself
.EEAF  D0 F8    BNE $EEA9   ; if changing got try again
.EEB1  0A       ASL   ; shift the serial data into Cb
.EEB2  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEA9**: read VIA 2 DRA, serial port and video address
- **$EEAC**: compare it with itself
- **$EEAF**: if changing got try again
- **$EEB1**: shift the serial data into Cb

### Commodore-64-intern-Buch (Commodore)
- **$EEA9**: Port A laden
- **$EEAC**: Änderung ?
- **$EEAF**: verzweige wenn ja
- **$EEB1**: Datenbit ins Carry schieben
- **$EEB2**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$EEA9**: serial port I/O register
- **$EEAC**: compare
- **$EEAF**: wait for bus to settle
- **$EEB1**: shift data into carry, and CLK into bit 7

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-eea9-get-the-serial-data-status-in-cb]]
