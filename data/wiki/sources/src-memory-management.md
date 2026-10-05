---
id: src-memory-management
type: source
title: 'Source Summary: Without Cartridges'
aliases:
- Without Cartridges
- memory_management.md
tags:
- assembly
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/memory_management.md
  sha256: 7e2df880cea44f30df8639611970d7d4fdd983ee2f55e8a15e18413a8a108162
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Without Cartridges

**Raw Source File**: `data/docs/codebase_c64_org/base/memory_management.md`
**SHA256**: `7e2df880cea44f30df8639611970d7d4fdd983ee2f55e8a15e18413a8a108162`

## Summary



# Without Cartridges

### Table of Contents

# Without Cartridges

The low 3 bits of $01 control the mapping of specific regions of memory. When a bit is set to 0, it activates its bank, but the interplay between them is kind of fiddly:

| Name | Bit | Region | 0 | 1 | Notes | 
|---|---|---|---|---|---|
| LORAM | 0 | $A000-BFFF | RAM | BASIC | If KERNAL isn't mapped in, then BASIC won't map in either and this region stays mapped to RAM. | 
| HIRAM | 1 | $E000-FFFF | RAM | KERNAL |  | 
| CHAREN...
