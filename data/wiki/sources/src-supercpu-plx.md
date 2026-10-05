---
id: src-supercpu-plx
type: source
title: 'Source Summary: PLX'
aliases:
- PLX
- supercpu_plx.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_plx.md
  sha256: 42802c434205b9efd5a9b2d1691063a3d84241cc5cc807e65643aac7929b3280
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PLX

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_plx.md`
**SHA256**: `42802c434205b9efd5a9b2d1691063a3d84241cc5cc807e65643aac7929b3280`

## Summary



# PLX

base:supercpu_plx

                # PLX

```
    /*-------------------------------------------------------------------------
    OP CODE: PLX (PulL index register X from stack)
    ===============================================
    
    Addressing Modes:
        Stack                            ($fa - 1 byte, 4 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z -...
