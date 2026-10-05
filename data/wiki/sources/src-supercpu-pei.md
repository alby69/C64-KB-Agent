---
id: src-supercpu-pei
type: source
title: 'Source Summary: PEI'
aliases:
- PEI
- supercpu_pei.md
tags:
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_pei.md
  sha256: 2575988a1c3bc4bc0f01df9994f419164883d8bf82a5ce7601ec591c504badea
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PEI

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_pei.md`
**SHA256**: `2575988a1c3bc4bc0f01df9994f419164883d8bf82a5ce7601ec591c504badea`

## Summary



# PEI

base:supercpu_pei

                # PEI

```
    /*-------------------------------------------------------------------------
    OP CODE: PEI (Push Effective Indirect address)
    ==============================================
    
    Addressing Modes:
        Stack (Direct Page Indirect)    ($d4 - 2 bytes, 6 cycles¹)
        ¹ - Add 1 cycle if low byte of Direct Page register is other than zero
            (DL< >0)
    Flags Affected:
        N/A
    Description:
        Push the six...
