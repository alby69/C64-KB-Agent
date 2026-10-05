---
id: src-b37d-fre-function
type: source
title: 'Source Summary: FRE function'
aliases:
- FRE function
- b37d-fre-function.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b37d-fre-function.md
  sha256: a5847467455522ba6663279c66ae83307b487dcaeeb51ed9f0d7aa9d606b8b9a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: FRE function

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b37d-fre-function.md`
**SHA256**: `a5847467455522ba6663279c66ae83307b487dcaeeb51ed9f0d7aa9d606b8b9a`

## Summary



# $B37D — FRE function

## Disassemblatura
```assembly
.B37D  A5 0D    LDA $0D
.B37F  F0 03    BEQ $B384
.B381  20 A6 B6 JSR $B6A6
.B384  20 26 B5 JSR $B526
.B387  38       SEC
.B388  A5 33    LDA $33
.B38A  E5 31    SBC $31
.B38C  A8       TAY
.B38D  A5 34    LDA $34
.B38F  E5 32    SBC $32
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B37D**: Typflag
- **$B37F**: kein String
- **$B381**: FRESTR
- **$B384**: Garbage Collection
- **$B387**: Carry setzen (Subtr.)
- **$B388**:...
