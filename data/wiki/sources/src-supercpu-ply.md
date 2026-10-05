---
id: src-supercpu-ply
type: source
title: 'Source Summary: PLY'
aliases:
- PLY
- supercpu_ply.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_ply.md
  sha256: 84536d05c762633be80952465c22848c65acc34b348c926f3a193fa77a8d215f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PLY

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_ply.md`
**SHA256**: `84536d05c762633be80952465c22848c65acc34b348c926f3a193fa77a8d215f`

## Summary



# PLY

base:supercpu_ply

                # PLY

```
    /*-------------------------------------------------------------------------
    OP CODE: PLY (PulL index register Y from stack)
    ===============================================
    
    Addressing Modes:
        Stack                            ($7a - 1 byte, 4 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z -...
