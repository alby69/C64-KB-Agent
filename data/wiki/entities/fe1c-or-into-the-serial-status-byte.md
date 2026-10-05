---
id: fe1c-or-into-the-serial-status-byte
type: entity
title: OR into the serial status byte
aliases:
- OR into the serial status byte
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe1c-or-into-the-serial-status-byte.md
  sha256: 52700a1d406147483fd0bb50179e7f8f42f9c3440824c5a6495d4d37978e9ba5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe1c-or-into-the-serial-status-byte
---

# OR into the serial status byte



# $FE1C — OR into the serial status byte

## Disassemblatura
```assembly
.FE1C  05 90    ORA $90   ; OR with the serial status byte
.FE1E  85 90    STA $90   ; save the serial status byte
.FE20  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE1C**: OR with the serial status byte
- **$FE1E**: save the serial status byte

### Commodore-64-intern-Buch (Commodore)
- **$FE1C**: Statusflag testen und
- **$FE1E**: wieder abspeichern
- **$FE20**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe1c-or-into-the-serial-status-byte]]
