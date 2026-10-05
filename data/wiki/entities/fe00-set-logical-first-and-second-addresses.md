---
id: fe00-set-logical-first-and-second-addresses
type: entity
title: set logical, first and second addresses
aliases:
- set logical, first and second addresses
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe00-set-logical-first-and-second-addresses.md
  sha256: 485df2f4d77f964b791cd7801940baa45417fe743ac5ac0706d0a49d62cd5ca6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe00-set-logical-first-and-second-addresses
---

# set logical, first and second addresses



# $FE00 — set logical, first and second addresses

## Disassemblatura
```assembly
.FE00  85 B8    STA $B8   ; save the logical file
.FE02  86 BA    STX $BA   ; save the device number
.FE04  84 B9    STY $B9   ; save the secondary address
.FE06  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE00**: save the logical file
- **$FE02**: save the device number
- **$FE04**: save the secondary address

### Commodore-64-intern-Buch (Commodore)
- **$FE00**: logische Filenummer
- **$FE02**: Geräteadresse
- **$FE04**: Sekundäradresse
- **$FE06**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE00**: store logical filenumber in LA
- **$FE02**: store devicenumber in FA
- **$FE04**: store secondary address in SA

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe00-set-logical-first-and-second-addresses]]
