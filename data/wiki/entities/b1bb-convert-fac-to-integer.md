---
id: b1bb-convert-fac-to-integer
type: entity
title: CONVERT FAC TO INTEGER
aliases:
- CONVERT FAC TO INTEGER
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b1bb-convert-fac-to-integer.md
  sha256: ceeb583238cd0b49c2482b4964732bf7772e624d585085cdb293f1ed1045cdf0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b1bb-convert-fac-to-integer
---

# CONVERT FAC TO INTEGER



# $B1BB — CONVERT FAC TO INTEGER

## Disassemblatura
```assembly
.B1BB  A5 66    LDA $66   ; ERROR IF -
.B1BD  30 0D    BMI $B1CC
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B1BB**: ERROR IF -

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b1bb-convert-fac-to-integer]]
