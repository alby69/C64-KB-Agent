---
id: src-supercpu-plb
type: source
title: 'Source Summary: PLB'
aliases:
- PLB
- supercpu_plb.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_plb.md
  sha256: dbf4e0e573f77af156d6de7535bd2f9ac6b4365a0a7bdd458eee8d252a683297
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PLB

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_plb.md`
**SHA256**: `dbf4e0e573f77af156d6de7535bd2f9ac6b4365a0a7bdd458eee8d252a683297`

## Summary



# PLB

base:supercpu_plb

                # PLB

```
    /*-------------------------------------------------------------------------
    OP CODE: PLB (PulL data Bank register)
    ======================================
    
    Addressing Modes:
        Stack                            ($ab - 1 byte, 4 cycles)
    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z - Set if value pulled is zero; else cleared.
    Description:
        Pull the...
