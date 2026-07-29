---
title: serial bus device close
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- common
- f2ee-close-close-file-part-2
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $F2EE
  address_end: $F2F1
  symbol: serial-bus-device-close
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F2EE**: close serial bus device'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F2EE**: UNTALK/UNLISTEN serial device'
---

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