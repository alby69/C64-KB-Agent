---
id: src-scpu-bitmode16
type: source
title: 'Source Summary: BitMode16'
aliases:
- BitMode16
- scpu_bitmode16.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/scpu_bitmode16.md
  sha256: 90cbcc99bbf5c7ad8078feea40f82c59e0ac75244e7218d2a3369ff41c464e47
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BitMode16

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_bitmode16.md`
**SHA256**: `90cbcc99bbf5c7ad8078feea40f82c59e0ac75244e7218d2a3369ff41c464e47`

## Summary



# BitMode16

base:scpu_bitmode16

                # BitMode16

Pseudocommand to set the Accumulator and X/Y Index registers to 16 bit mode on the 658C16.

| SYNTAX: | BitMode16 | 
| EXAMPLE: | BitMode16 | 
| PARAMETERS: | N/A | 

```
    .pseudocommand BitMode16 {
        rep #%00110000
    }
```
base/scpu_bitmode16.txt · Last modified:  by tww

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand BitMode16 {
        rep #%00110000
    }
```



---
*F...
