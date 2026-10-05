---
id: src-scpu-setchermode
type: source
title: 'Source Summary: SetCharMode'
aliases:
- SetCharMode
- scpu_setchermode.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_setchermode.md
  sha256: 32503931a856947ff294ab81578c739ea7f2050c042ab290955e90beb0a918a1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SetCharMode

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_setchermode.md`
**SHA256**: `32503931a856947ff294ab81578c739ea7f2050c042ab290955e90beb0a918a1`

## Summary




# SetCharMode

base:scpu_setchermode

                # SetCharMode

Set Character Set Mode (reset bit #5 of $d011).

| SYNTAX: | :SetCharMode | 
| EXAMPLE: | :SetCharMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand SetChar {
        lda #%0010000000000000
        trb $d010
    }
```
base/scpu_setchermode.txt · Last modified:  by tww

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand SetChar {
        lda #%0010000000000000
        trb $d010...
