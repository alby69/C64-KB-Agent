---
id: afa0-real-variable-holen
type: entity
title: REAL-Variable holen
aliases:
- REAL-Variable holen
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/afa0-real-variable-holen.md
  sha256: 562b989e03227961eb34b8f71d126f7d2c05fd83fd45d3fd4dbc2c8c780fef02
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-afa0-real-variable-holen
---

# REAL-Variable holen



# $AFA0 — REAL-Variable holen

## Disassemblatura
```assembly
.AFA0  A5 64    LDA $64   ; LOW- und HIGH-Byte der
.AFA2  A4 65    LDY $65   ; Variablenadresse
.AFA4  4C A2 BB JMP $BBA2   ; Variable in FAC holen
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AFA0**: LOW- und HIGH-Byte der
- **$AFA2**: Variablenadresse
- **$AFA4**: Variable in FAC holen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-afa0-real-variable-holen]]
