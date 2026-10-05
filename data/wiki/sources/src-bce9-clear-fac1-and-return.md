---
id: src-bce9-clear-fac1-and-return
type: source
title: 'Source Summary: clear FAC1 and return'
aliases:
- clear FAC1 and return
- bce9-clear-fac1-and-return.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bce9-clear-fac1-and-return.md
  sha256: 93ed340421763818a9435468928ec18b483dd1340ce6d00961f3ccc82742b478
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: clear FAC1 and return

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bce9-clear-fac1-and-return.md`
**SHA256**: `93ed340421763818a9435468928ec18b483dd1340ce6d00961f3ccc82742b478`

## Summary



# $BCE9 — clear FAC1 and return

## Disassemblatura
```assembly
.BCE9  85 62    STA $62   ; clear FAC1 mantissa 1
.BCEB  85 63    STA $63   ; clear FAC1 mantissa 2
.BCED  85 64    STA $64   ; clear FAC1 mantissa 3
.BCEF  85 65    STA $65   ; clear FAC1 mantissa 4
.BCF1  A8       TAY   ; clear Y
.BCF2  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BCE9**: clear FAC1 mantissa 1
- **$BCEB**: clear FAC1 mantissa 2
- **$BCED**: clear FAC1 mantissa 3
- **$BCEF**: clear FAC1 manti...
