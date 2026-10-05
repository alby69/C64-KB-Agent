---
id: src-bbd0-pack-fac1-into-variable-pointer
type: source
title: 'Source Summary: pack FAC1 into variable pointer'
aliases:
- pack FAC1 into variable pointer
- bbd0-pack-fac1-into-variable-pointer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbd0-pack-fac1-into-variable-pointer.md
  sha256: cda5e9f2952f0a3a43389813dff119982fc4bd3b7edf5eb8e471d9e6c66d6363
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: pack FAC1 into variable pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bbd0-pack-fac1-into-variable-pointer.md`
**SHA256**: `cda5e9f2952f0a3a43389813dff119982fc4bd3b7edf5eb8e471d9e6c66d6363`

## Summary



# $BBD0 — pack FAC1 into variable pointer

## Disassemblatura
```assembly
.BBD0  A6 49    LDX $49   ; get destination pointer low byte
.BBD2  A4 4A    LDY $4A   ; get destination pointer high byte
```


## Commenti

### Original Disassembly (—)
- **$BBD0**: get destination pointer low byte
- **$BBD2**: get destination pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$BBD0**: Variablenadresse
- **$BBD2**: holen
- **$BBD4**: FAC runden
- **$BBD7**: Zeiger auf
- **$BBD9**: Zieladre...
