---
id: src-a1a0-basic-fehlermeldungen
type: source
title: 'Source Summary: BASIC-Fehlermeldungen'
aliases:
- BASIC-Fehlermeldungen
- a1a0-basic-fehlermeldungen.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a1a0-basic-fehlermeldungen.md
  sha256: 5f8d485553538a4747f3415383036c82fd430bc0f9decfb3cec97b1cfce940d0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BASIC-Fehlermeldungen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a1a0-basic-fehlermeldungen.md`
**SHA256**: `5f8d485553538a4747f3415383036c82fd430bc0f9decfb3cec97b1cfce940d0`

## Summary



# $A1A0 — BASIC-Fehlermeldungen

## Disassemblatura
```assembly
.A1A0  54 4F   ; 1 too many files
.A1A0  4F 20 4D 41 4E 59 20 46
.A1A8  49 4C 45 D3 46 49 4C 45   ; 2 file open
.A1B0  20 4F 50 45 CE 46 49 4C   ; 3 file not open
.A1B8  45 20 4E 4F 54 20 4F 50
.A1C0  45 CE 46 49 4C 45 20 4E   ; 4 file not found
.A1C8  4F 54 20 46 4F 55 4E C4   ; 5 device not present
.A1D0  44 45 56 49 43 45 20 4E
.A1D8  4F 54 20 50 52 45 53 45
.A1E0  4E D4 4E 4F 54 20 49 4E   ; 6 not input file
.A1E8  50 55 54 20...
