---
id: src-scpu-emulatedmode
type: source
title: 'Source Summary: EmulatedMode'
aliases:
- EmulatedMode
- scpu_emulatedmode.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/scpu_emulatedmode.md
  sha256: c860755a1be68da519e64974da4574c944e6bd8dd6fab760e10a20e64dc8176a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: EmulatedMode

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_emulatedmode.md`
**SHA256**: `c860755a1be68da519e64974da4574c944e6bd8dd6fab760e10a20e64dc8176a`

## Summary



# EmulatedMode

base:scpu_emulatedmode

                # EmulatedMode

Sets the processor into 6502/6510 Emulated mode.

| SYNTAX: | EmulatedMode | 
| EXAMPLE: | EmulatedMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand EmulatedMode {
        sec
        xce
    }
```
base/scpu_emulatedmode.txt · Last modified:  by tww

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand EmulatedMode {
        sec
        xce
    }
```



---
*Fonte originale: ...
