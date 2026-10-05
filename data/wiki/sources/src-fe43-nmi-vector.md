---
id: src-fe43-nmi-vector
type: source
title: 'Source Summary: NMI vector'
aliases:
- NMI vector
- fe43-nmi-vector.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe43-nmi-vector.md
  sha256: b9245a51b463e3808d59bf859694e3ae06b8873d49c1b1e96b97c440f8ddb89c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NMI vector

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe43-nmi-vector.md`
**SHA256**: `b9245a51b463e3808d59bf859694e3ae06b8873d49c1b1e96b97c440f8ddb89c`

## Summary



# $FE43 — NMI vector

## Disassemblatura
```assembly
.FE43  78       SEI   ; disable the interrupts
.FE44  6C 18 03 JMP ($0318)   ; do NMI vector
```


## Commenti

### Original Disassembly (—)
- **$FE43**: disable the interrupts
- **$FE44**: do NMI vector

### Commodore-64-intern-Buch (Commodore)
- **$FE43**: Interrupt setzen
- **$FE44**: JMP $FE47, NMI-Vektor
- **$FE47**: Akku auf Stapel retten
- **$FE48**: X nach Akku
- **$FE49**: X retten
- **$FE4A**: Y nach Akku
- **$FE4B**: Y retten
- **...
