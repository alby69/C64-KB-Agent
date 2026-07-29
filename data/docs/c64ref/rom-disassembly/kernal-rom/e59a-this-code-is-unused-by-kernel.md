---
title: this code is unused by kernel
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - magnus_nyman.txt
  address: $E59A
  address_end: $E59D
  symbol: this-code-is-unused-by-kernel
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E59A**: set I/O defaults'
---

# $E59A — this code is unused by kernel

## Disassemblatura
```assembly
.E59A  20 A0 E5 JSR $E5A0
.E59D  4C 66 E5 JMP $E566
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E59A**: set I/O defaults
- **$E59D**: home cursor and exit routine
- **$E5A2**: DFLTO, default output device - screen
- **$E5A6**: DFLTN, default input device - keyboard
- **$E5AA**: VIC chip setup table
- **$E5AD**: VIC chip I/O registers
- **$E5B0**: next
- **$E5B1**: till ready

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*