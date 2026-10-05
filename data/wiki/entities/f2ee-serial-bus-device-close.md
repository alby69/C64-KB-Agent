---
id: f2ee-serial-bus-device-close
type: entity
title: serial bus device close
aliases:
- serial bus device close
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f2ee-serial-bus-device-close.md
  sha256: 944bb064351810b0e7f304e0ba4017722809499e7e1db1af6ae0426e80be932b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f2ee-serial-bus-device-close
---

# serial bus device close



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
- **$F2F5**: compare LDTND to (X)
- **$F2F7**: equal, closed file = last file in table
- **$F2F9**: else, move last entry to position of closed entry
- **$F2FB**: LAT, active file numbers
- **$F301**: FAT, active device numbers
- **$F307**: SAT, active secondary addresses
- **$F30E**: return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f2ee-serial-bus-device-close]]
