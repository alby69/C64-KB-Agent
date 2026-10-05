---
id: src-fe1c-or-into-the-serial-status-byte
type: source
title: 'Source Summary: OR into the serial status byte'
aliases:
- OR into the serial status byte
- fe1c-or-into-the-serial-status-byte.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe1c-or-into-the-serial-status-byte.md
  sha256: 52700a1d406147483fd0bb50179e7f8f42f9c3440824c5a6495d4d37978e9ba5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: OR into the serial status byte

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe1c-or-into-the-serial-status-byte.md`
**SHA256**: `52700a1d406147483fd0bb50179e7f8f42f9c3440824c5a6495d4d37978e9ba5`

## Summary



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

### Marko Mäkelä (Marko...
