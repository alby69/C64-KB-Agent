---
id: src-f2ee-serial-bus-device-close
type: source
title: 'Source Summary: serial bus device close'
aliases:
- serial bus device close
- f2ee-serial-bus-device-close.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f2ee-serial-bus-device-close.md
  sha256: 944bb064351810b0e7f304e0ba4017722809499e7e1db1af6ae0426e80be932b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: serial bus device close

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f2ee-serial-bus-device-close.md`
**SHA256**: `944bb064351810b0e7f304e0ba4017722809499e7e1db1af6ae0426e80be932b`

## Summary



# $F2EE — serial bus device close

## Disassemblatura
```assembly
.F2EE  20 42 F6 JSR $F642   ; close serial bus device
.F2F1  68       PLA   ; restore file index
```


## Commenti

### Original Disassembly (—)
- **$F2EE**: close serial bus device
- **$F2F1**: restore file index

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F2EE**: UNTALK/UNLISTEN serial device
- **$F2F3**: decrement LDTND, number of open files
- **$F2F5**: compare LDTND to...
