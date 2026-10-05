---
id: src-scpu-nativemode
type: source
title: 'Source Summary: NativeMode'
aliases:
- NativeMode
- scpu_nativemode.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/scpu_nativemode.md
  sha256: 6c1fd5abebac428435751e56acc8cd09a1efcdce396900c413f4ffffbb2b63c9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NativeMode

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_nativemode.md`
**SHA256**: `6c1fd5abebac428435751e56acc8cd09a1efcdce396900c413f4ffffbb2b63c9`

## Summary



# NativeMode

base:scpu_nativemode

                # NativeMode

Sets the processor into 65C816 native mode.

| SYNTAX: | NativeMode | 
| EXAMPLE: | NativeMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand NativeMode {
        clc
        xce
    }
```
base/scpu_nativemode.txt · Last modified:  by tww

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand NativeMode {
        clc
        xce
    }
```



---
*Fonte originale: [https://codebase.c64...
