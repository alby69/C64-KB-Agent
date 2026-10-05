---
id: src-e1be-perform-open
type: source
title: 'Source Summary: perform OPEN'
aliases:
- perform OPEN
- e1be-perform-open.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e1be-perform-open.md
  sha256: 3c4838be0dc57f792a47e96db6a9674fb8bd6305497d6f0857e3a4488ac04445
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform OPEN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e1be-perform-open.md`
**SHA256**: `3c4838be0dc57f792a47e96db6a9674fb8bd6305497d6f0857e3a4488ac04445`

## Summary



# $E1BE — perform OPEN

## Disassemblatura
```assembly
.E1BE  20 19 E2 JSR $E219   ; get parameters for OPEN/CLOSE
.E1C1  20 C0 FF JSR $FFC0   ; open a logical file
.E1C4  B0 0B    BCS $E1D1   ; branch if error
.E1C6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E1BE**: get parameters for OPEN/CLOSE
- **$E1C1**: open a logical file
- **$E1C4**: branch if error

### Commodore-64-intern-Buch (Commodore)
- **$E1BE**: Parameter holen
- **$E1C1**: OPEN-Routine
- **$E1C4**: Fehl...
