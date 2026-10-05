---
id: src-scpu-setbitmapmode
type: source
title: 'Source Summary: SetBitmapMode'
aliases:
- SetBitmapMode
- scpu_setbitmapmode.md
tags:
- basic
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_setbitmapmode.md
  sha256: 6d72c33c9e7cb31c72790bbdc24c8c9105e96b5d1bd09510feb24e547c2bef87
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SetBitmapMode

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_setbitmapmode.md`
**SHA256**: `6d72c33c9e7cb31c72790bbdc24c8c9105e96b5d1bd09510feb24e547c2bef87`

## Summary




# SetBitmapMode

base:scpu_setbitmapmode

                # SetBitmapMode

Set Bitmap Mode (set bit #5 of $d011).

| SYNTAX: | :SetBitmapMode | 
| EXAMPLE: | :SetBitmapMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand SetBitmapMode {
        lda #%0010000000000000
        tsb $d010
    }
```
base/scpu_setbitmapmode.txt · Last modified:  by tww

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand SetBitmapMode {
        lda #%0010000000000000
  ...
