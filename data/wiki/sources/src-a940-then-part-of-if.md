---
id: src-a940-then-part-of-if
type: source
title: 'Source Summary: THEN part of IF'
aliases:
- THEN part of IF
- a940-then-part-of-if.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a940-then-part-of-if.md
  sha256: 80df9f04dd6b7d87baeddf6cdc181eb54f5f83a858bad1e923faca247372bdf9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: THEN part of IF

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a940-then-part-of-if.md`
**SHA256**: `80df9f04dd6b7d87baeddf6cdc181eb54f5f83a858bad1e923faca247372bdf9`

## Summary



# $A940 — THEN part of IF

## Disassemblatura
```assembly
.A940  20 79 00 JSR $0079
.A943  B0 03    BCS $A948
.A945  4C A0 A8 JMP $A8A0   ; do GOTO
.A948  4C ED A7 JMP $A7ED
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$A945**: do GOTO

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
