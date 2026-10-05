---
id: bdb3-limits-for-scientific-mode
type: entity
title: limits for scientific mode
aliases:
- limits for scientific mode
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bdb3-limits-for-scientific-mode.md
  sha256: 908ad2cffc3c9d37068173f13807e83a653b938c19206feffb8ffe2d195682f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bdb3-limits-for-scientific-mode
---

# limits for scientific mode



# $BDB3 — limits for scientific mode

## Disassemblatura
```assembly
.BDB3  9B 3E BC 1F FD   ; 99999999.90625, maximum value with at least one decimal
.BDB8  9E 6E 6B 27 FD   ; 999999999.25, maximum value before scientific notation
.BDBD  9E 6E 6B 28 00   ; 1000000000
```


## Commenti

### Original Disassembly (—)
- **$BDB3**: 99999999.90625, maximum value with at least one decimal
- **$BDB8**: 999999999.25, maximum value before scientific notation
- **$BDBD**: 1000000000

### Commodore-64-intern-Buch (Commodore)
- **$BDB3**: 99999999.9
- **$BDB8**: 999999999
- **$BDBD**: 1E9

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bdb3-limits-for-scientific-mode]]
