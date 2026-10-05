---
id: src-scpu-setrambank
type: source
title: 'Source Summary: SetRAMBank'
aliases:
- SetRAMBank
- scpu_setrambank.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_setrambank.md
  sha256: ae2f9667a1328564ae12de28915150450e061474d5c5896546c2219ad9f58ea6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SetRAMBank

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_setrambank.md`
**SHA256**: `ae2f9667a1328564ae12de28915150450e061474d5c5896546c2219ad9f58ea6`

## Summary



# SetRAMBank

base:scpu_setrambank

                # SetRAMBank

Set's the active RAM Bank used by the 658C16 CPU.

Requires the function: “SwitchEndian16”

| SYNTAX: | :SetRAMBank val |  |  | 
| EXAMPLE: | :SetRAMBank $100000 |  |  | 
| PARAMETERS: | Type | Minimum | Maximum | 
| val | U8 | $00 | $ff | 

```
    .pseudocommand SetRAMBank val {
        lda #SwitchEndian16(val.getValue())
        pha
        plb
        plb
    }
```
base/scpu_setrambank.txt · Last modified:  by tww

## Codice...
