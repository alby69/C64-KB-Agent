---
id: src-scpu-setgraphicsbank
type: source
title: 'Source Summary: SetGraphicsBank'
aliases:
- SetGraphicsBank
- scpu_setgraphicsbank.md
tags:
- assembly
- basic
- graphics
- memory management
sources:
- path: data/docs/codebase_c64_org/base/scpu_setgraphicsbank.md
  sha256: 0a2eb4eb227c3b9d29baa81f99facbc89dbefd24dca0172de4b14e426a1bf2bd
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SetGraphicsBank

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_setgraphicsbank.md`
**SHA256**: `0a2eb4eb227c3b9d29baa81f99facbc89dbefd24dca0172de4b14e426a1bf2bd`

## Summary




# SetGraphicsBank

base:scpu_setgraphicsbank

                # SetGraphicsBank

Sets the VIC Grahoics Bank, The Screen Memory and the Bitmap Memory (both for Bitmap Graphics and Charset Graphics).

| SYNTAX: | SetGraphicsBank SCRMem : BMPMem |  |  | 
| EXAMPLE: | SetGraphicsBank $0400 : $2000 |  |  | 
| PARAMETERS: | Type | Minimum | Maximum | 
| SCRMem | U16 | $0000 | $ffff | 
| BMPMem | U16 | $0000 | $ffff | 

Imporvements: Don't like the write to $d019….

```
    .pseudocommand SetGraphic...
