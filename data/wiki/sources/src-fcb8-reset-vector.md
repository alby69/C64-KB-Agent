---
id: src-fcb8-reset-vector
type: source
title: 'Source Summary: reset vector'
aliases:
- reset vector
- fcb8-reset-vector.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fcb8-reset-vector.md
  sha256: ea5982d12de7fba831f461a415aaa1bf34ff2c10c56647ba3b4e775f69059210
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: reset vector

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fcb8-reset-vector.md`
**SHA256**: `ea5982d12de7fba831f461a415aaa1bf34ff2c10c56647ba3b4e775f69059210`

## Summary



# $FCB8 — reset vector

## Disassemblatura
```assembly
.FCB8  20 93 FC JSR $FC93   ; restore everything for STOP
.FCBB  F0 97    BEQ $FC54   ; restore registers and exit interrupt, branch always
```


## Commenti

### Original Disassembly (—)
- **$FCB8**: restore everything for STOP
- **$FCBB**: restore registers and exit interrupt, branch always

### Commodore-64-intern-Buch (Commodore)
- **$FCB8**: IRQ auf Standard
- **$FCBB**: Abschluß IRQ
- **$FCBD**: IRQ-Vektor
- **$FCC0**: aus Tabelle se...
