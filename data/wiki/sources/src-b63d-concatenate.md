---
id: src-b63d-concatenate
type: source
title: 'Source Summary: concatenate'
aliases:
- concatenate
- b63d-concatenate.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b63d-concatenate.md
  sha256: db355c5eb572122242e9b6c41f45e2f14832b94ece409cef0cdf108be04ab4d2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: concatenate

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b63d-concatenate.md`
**SHA256**: `db355c5eb572122242e9b6c41f45e2f14832b94ece409cef0cdf108be04ab4d2`

## Summary



# $B63D — concatenate

## Disassemblatura
```assembly
.B63D  A5 65    LDA $65   ; get descriptor pointer high byte
.B63F  48       PHA   ; put on stack
.B640  A5 64    LDA $64   ; get descriptor pointer low byte
.B642  48       PHA   ; put on stack
.B643  20 83 AE JSR $AE83   ; get value from line
.B646  20 8F AD JSR $AD8F   ; check if source is string, else do type mismatch
.B649  68       PLA   ; get descriptor pointer low byte back
.B64A  85 6F    STA $6F   ; set pointer low byte
.B64C  68 ...
