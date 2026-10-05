---
id: a82f-perform-stop
type: entity
title: perform STOP
aliases:
- perform STOP
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a82f-perform-stop.md
  sha256: 432c1599f88978eea9ed01f6fad9d668e3d9c46b360d60978654f74ef31bf2a3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a82f-perform-stop
---

# perform STOP



# $A82F — perform STOP

## Disassemblatura
```assembly
.A82F  B0 01    BCS $A832   ; if carry set do BREAK instead of just END
```


## Commenti

### Original Disassembly (—)
- **$A82F**: if carry set do BREAK instead of just END

### Commodore-64-intern-Buch (Commodore)
- **$A82F**: C=1: Flag für STOP

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A82F**: CARRY=1 TO FORCE PRINTING "BREAK AT.."

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a82f-perform-stop]]
