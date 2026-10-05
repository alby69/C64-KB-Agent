---
id: src-supercpu-xba
type: source
title: 'Source Summary: XBA'
aliases:
- XBA
- supercpu_xba.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_xba.md
  sha256: 23b2e63e1f9e2a9425a0a5e52d1160a579e1514f0b2f54cc89f13727ff05c49f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: XBA

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_xba.md`
**SHA256**: `23b2e63e1f9e2a9425a0a5e52d1160a579e1514f0b2f54cc89f13727ff05c49f`

## Summary



# XBA

base:supercpu_xba

                # XBA

```
    /*-------------------------------------------------------------------------
    OP CODE: XBA (eXchange the B and A accumulators)
    ================================================
    
    Addressing Modes:
        Implied                            ($eb - 1 byte, 3 cycles)
    Flags Affected:
        n - Set if most significant bit of new 8-bit value A accumulator is
            set; else cleared.
        z - Set if new 8-bit value in...
