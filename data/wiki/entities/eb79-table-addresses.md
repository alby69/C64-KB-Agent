---
id: eb79-table-addresses
type: entity
title: table addresses
aliases:
- table addresses
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eb79-table-addresses.md
  sha256: 20cb7ca43f3ccfc6bb8b6e1c95714f4cb5e14ce22df9999a59c1cb3dc55feaf3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-eb79-table-addresses
---

# table addresses



# $EB79 — table addresses

## Disassemblatura
```assembly
.EB79  81 EB   ; standard
.EB7B  C2 EB   ; shift
.EB7D  03 EC   ; commodore
.EB7F  78 EC   ; control
```


## Commenti

### Original Disassembly (—)
- **$EB79**: standard
- **$EB7B**: shift
- **$EB7D**: commodore
- **$EB7F**: control

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
- **$EB79**: standard
- **$EB7B**: shift
- **$EB7D**: commodore key
- **$EB7F**: control

### Magnus Nyman (Magnus Nyman)
- **$EB79**: vector to unshifted keyboard, $eb81
- **$EB7B**: vector to shifted keyboard, $ebc2
- **$EB7D**: vector to cbm keyboard, $ec03
- **$EB7F**: vector to ctrl keyboard, $ec78

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-eb79-table-addresses]]
