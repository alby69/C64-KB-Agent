---
id: src-ed0c-command-devices-on-the-serial-bus-to-listen
type: source
title: 'Source Summary: command devices on the serial bus to LISTEN'
aliases:
- command devices on the serial bus to LISTEN
- ed0c-command-devices-on-the-serial-bus-to-listen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed0c-command-devices-on-the-serial-bus-to-listen.md
  sha256: 503193cfa87b97e6cf4b26f747344812810723022d1f95df92e1637e22bea89a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: command devices on the serial bus to LISTEN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ed0c-command-devices-on-the-serial-bus-to-listen.md`
**SHA256**: `503193cfa87b97e6cf4b26f747344812810723022d1f95df92e1637e22bea89a`

## Summary



# $ED0C — command devices on the serial bus to LISTEN

## Disassemblatura
```assembly
.ED0C  09 20    ORA #$20   ; OR with the LISTEN command
.ED0E  20 A4 F0 JSR $F0A4   ; check RS232 bus idle
```


## Commenti

### Original Disassembly (—)
- **$ED0C**: OR with the LISTEN command
- **$ED0E**: check RS232 bus idle

### Commodore-64-intern-Buch (Commodore)
- **$ED0C**: Bit für Listen setzen
- **$ED0E**: Ende der RS 232 Übertragung abwarten
- **$ED11**: Akku merken
- **$ED12**: Noch Zeichen im Pu...
