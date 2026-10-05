---
id: src-b5c7-check-string-area
type: source
title: 'Source Summary: check string area'
aliases:
- check string area
- b5c7-check-string-area.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b5c7-check-string-area.md
  sha256: 5199c2975f1e6896e73a5b6806eb78b9c2525edf704c1319be130e942be9d7fb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check string area

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b5c7-check-string-area.md`
**SHA256**: `5199c2975f1e6896e73a5b6806eb78b9c2525edf704c1319be130e942be9d7fb`

## Summary



# $B5C7 — check string area

## Disassemblatura
```assembly
.B5C7  B1 22    LDA ($22),Y
.B5C9  F0 2B    BEQ $B5F6
.B5CB  C8       INY
.B5CC  B1 22    LDA ($22),Y
.B5CE  AA       TAX
.B5CF  C8       INY
.B5D0  B1 22    LDA ($22),Y
.B5D2  C5 34    CMP $34
.B5D4  90 06    BCC $B5DC
.B5D6  D0 1E    BNE $B5F6
.B5D8  E4 33    CPX $33
.B5DA  B0 1A    BCS $B5F6
.B5DC  C5 60    CMP $60
.B5DE  90 16    BCC $B5F6
.B5E0  D0 04    BNE $B5E6
.B5E2  E4 5F    CPX $5F
.B5E4  90 10    BCC $B5F6
.B5E6  86 5F    ...
