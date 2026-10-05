---
id: src-supercpu-phb
type: source
title: 'Source Summary: PHB'
aliases:
- PHB
- supercpu_phb.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_phb.md
  sha256: dd2dfdeca5b8a29db1fa7220d3deed61eab473b63ee77158d2a32edf83f2c390
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PHB

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_phb.md`
**SHA256**: `dd2dfdeca5b8a29db1fa7220d3deed61eab473b63ee77158d2a32edf83f2c390`

## Summary



# PHB

base:supercpu_phb

                # PHB

```
    /*-------------------------------------------------------------------------
    OP CODE: PHB (PusH data Bank register)
    ======================================
    Addressing Modes:
        Stack                            ($8b - 1 byte, 3 cycles)
    Flags Affected:
        N/A
    Description:
        Push the contents of the data bank register onto the stack.
        The single-byte contents of the data bank registers are pushed ont...
