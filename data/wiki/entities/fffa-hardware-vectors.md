---
id: fffa-hardware-vectors
type: entity
title: hardware vectors
aliases:
- hardware vectors
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fffa-hardware-vectors.md
  sha256: e11a39df0abea9f2f99b16839311c210253bda7fdd369696cd223ce4a196bada
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fffa-hardware-vectors
---

# hardware vectors



# $FFFA — hardware vectors

## Disassemblatura
```assembly
.FFFA  43 FE   ; NMI Vector
.FFFC  E2 FC   ; RESET Vector
.FFFE  48 FF   ; IRQ Vector
```


## Commenti

### Original Disassembly (—)
- **$FFFA**: NMI Vector
- **$FFFC**: RESET Vector
- **$FFFE**: IRQ Vector

### Commodore-64-intern-Buch (Commodore)
- **$FFFA**: NMI Vektor
- **$FFFC**: RESET Vektor
- **$FFFE**: IRQ Vektor

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fffa-hardware-vectors]]
