---
id: src-ed09-command-serial-bus-device-to-talk
type: source
title: 'Source Summary: command serial bus device to TALK'
aliases:
- command serial bus device to TALK
- ed09-command-serial-bus-device-to-talk.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed09-command-serial-bus-device-to-talk.md
  sha256: 636bde41fa3b3e373314a93a86ca60737c93de1521dc093376d4695dedfbc794
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: command serial bus device to TALK

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ed09-command-serial-bus-device-to-talk.md`
**SHA256**: `636bde41fa3b3e373314a93a86ca60737c93de1521dc093376d4695dedfbc794`

## Summary



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

### Magnus Nyman (Ma...
