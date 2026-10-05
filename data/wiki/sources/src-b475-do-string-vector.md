---
id: src-b475-do-string-vector
type: source
title: 'Source Summary: do string vector'
aliases:
- do string vector
- b475-do-string-vector.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b475-do-string-vector.md
  sha256: 2f86a9eaa20a8d35fe5fbed9708d538cc401ae0f06b7057d6df6dfba05df8113
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do string vector

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b475-do-string-vector.md`
**SHA256**: `2f86a9eaa20a8d35fe5fbed9708d538cc401ae0f06b7057d6df6dfba05df8113`

## Summary



# $B475 — do string vector

## Disassemblatura
```assembly
.B475  A6 64    LDX $64   ; get descriptor pointer low byte
.B477  A4 65    LDY $65   ; get descriptor pointer high byte
.B479  86 50    STX $50   ; save descriptor pointer low byte
.B47B  84 51    STY $51   ; save descriptor pointer high byte
```


## Commenti

### Original Disassembly (—)
- **$B475**: get descriptor pointer low byte
- **$B477**: get descriptor pointer high byte
- **$B479**: save descriptor pointer low byte
- **$B47B*...
