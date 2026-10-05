---
id: fe21-set-timeout-on-serial-bus
type: entity
title: set timeout on serial bus
aliases:
- set timeout on serial bus
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe21-set-timeout-on-serial-bus.md
  sha256: 23dda846c42db0e6e05b7060337da3571e3d54f071cef7f8f08249373182f4f1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe21-set-timeout-on-serial-bus
---

# set timeout on serial bus



# $FE21 — set timeout on serial bus

## Disassemblatura
```assembly
.FE21  8D 85 02 STA $0285   ; save serial bus timeout flag
.FE24  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE21**: save serial bus timeout flag

### Commodore-64-intern-Buch (Commodore)
- **$FE21**: Timeout-disable
- **$FE24**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE21**: store in TIMOUT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe21-set-timeout-on-serial-bus]]
