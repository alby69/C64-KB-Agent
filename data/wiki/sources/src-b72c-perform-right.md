---
id: src-b72c-perform-right
type: source
title: 'Source Summary: perform RIGHT$()'
aliases:
- perform RIGHT$()
- b72c-perform-right.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b72c-perform-right.md
  sha256: c574d54b45daa85b479f3d377a2293a27f80cf128574fc2d8c159a777e8c0f0f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform RIGHT$()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b72c-perform-right.md`
**SHA256**: `c574d54b45daa85b479f3d377a2293a27f80cf128574fc2d8c159a777e8c0f0f`

## Summary



# $B72C — perform RIGHT$()

## Disassemblatura
```assembly
.B72C  20 61 B7 JSR $B761   ; pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
.B72F  18       CLC   ; clear carry for add-1
.B730  F1 50    SBC ($50),Y   ; subtract string length
.B732  49 FF    EOR #$FF   ; invert it (A=LEN(expression$)-l)
.B734  4C 06 B7 JMP $B706   ; go do rest of LEFT$()
```


## Commenti

### Original Disassembly (—)
- **$B72C**: pull string data and byte paramet...
