---
id: src-scpu-memcpy
type: source
title: 'Source Summary: MemCopy'
aliases:
- MemCopy
- scpu_memcpy.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_memcpy.md
  sha256: ae0dd46250dcd057b5f1882c6c16655708a3145539b01c3135ca04e05b785db2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MemCopy

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_memcpy.md`
**SHA256**: `ae0dd46250dcd057b5f1882c6c16655708a3145539b01c3135ca04e05b785db2`

## Summary



# MemCopy

# MemCopy

Uses the SuperCPU Memory transfer OPC. Automatically chooses the correct Copy Up or Copy Down OPC based on parameters.

| SYNTAX: | MemCopy src : dst : qty |  |  | 
| EXAMPLE1: | :MemCopy CopyFrom : CopyTo : Quantity-1 |  |  | 
| EXAMPLE2: | :MemCopy $200000 : $2000 : 8000-1 |  |  | 
| PARAMETERS: | Type | Minimum | Maximum | 
| src | U16 | $000000 | $ffffff | 
| dst | U16 | $000000 | $ffffff | 
| qty | U8 | $000000 | $ffffff | 

The MVN instruction uses X and Y to specif...
