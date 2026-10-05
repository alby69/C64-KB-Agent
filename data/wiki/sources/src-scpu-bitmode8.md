---
id: src-scpu-bitmode8
type: source
title: 'Source Summary: BitMode8'
aliases:
- BitMode8
- scpu_bitmode8.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/scpu_bitmode8.md
  sha256: e886acd303a1bd9148667909b0faea7dfc4f6ba513b11deeec025bbaca7216c5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BitMode8

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_bitmode8.md`
**SHA256**: `e886acd303a1bd9148667909b0faea7dfc4f6ba513b11deeec025bbaca7216c5`

## Summary



# BitMode8

base:scpu_bitmode8

                # BitMode8

Pseudocommand to set the Accumulator and X/Y Index registers to 8 bit mode on the 658C16.

| SYNTAX: | BitMode8 | 
| EXAMPLE: | BitMode8 | 
| PARAMETERS: | N/A | 

```
    .pseudocommand BitMode8 {
        sep #%00110000
    }
```
base/scpu_bitmode8.txt · Last modified:  by tww

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand BitMode8 {
        sep #%00110000
    }
```



---
*Fonte orig...
