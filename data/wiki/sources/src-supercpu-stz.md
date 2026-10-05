---
id: src-supercpu-stz
type: source
title: 'Source Summary: STZ'
aliases:
- STZ
- supercpu_stz.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_stz.md
  sha256: e45ce1ca14640d289005c9f346a08f9b6fe53412e7a404cab6514400eec747a3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STZ

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_stz.md`
**SHA256**: `e45ce1ca14640d289005c9f346a08f9b6fe53412e7a404cab6514400eec747a3`

## Summary



# STZ

base:supercpu_stz

                # STZ

```
    /*-------------------------------------------------------------------------
    OP CODE: STZ (STore Zero to memory)
    ===================================
    
    Addressing Modes:
        Absolute                        ($9c - 3 bytes, 4 cycles¹)
        Direct Page                     ($64 - 2 bytes, 3 cycles¹²)
        Absolute Indexed,x              ($9e - 3 bytes, 5 cycles¹)
        Direct Page Indexed,x           ($74 - 2 bytes, ...
