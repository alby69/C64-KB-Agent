---
id: b185-variable-found
type: entity
title: variable found
aliases:
- variable found
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b185-variable-found.md
  sha256: 0181c2a8d1c6246e2e30d6c72334b9f88830ae46d770803276bc2025a98e1a38
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b185-variable-found
---

# variable found



# $B185 — variable found

## Disassemblatura
```assembly
.B185  A5 5F    LDA $5F
.B187  18       CLC
.B188  69 02    ADC #$02
.B18A  A4 60    LDY $60
.B18C  90 01    BCC $B18F
.B18E  C8       INY
.B18F  85 47    STA $47
.B191  84 48    STY $48
.B193  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B185**: LOWTR POINTS AT NAME OF VARIABLE,
- **$B187**: SO ADD 2 TO GET TO VALUE
- **$B18F**: ADDRESS IN VARPNT AND Y,A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b185-variable-found]]
