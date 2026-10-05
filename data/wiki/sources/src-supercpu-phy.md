---
id: src-supercpu-phy
type: source
title: 'Source Summary: PHY'
aliases:
- PHY
- supercpu_phy.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_phy.md
  sha256: 2a53ad759444c88c25c183d2990ecd2fbb85c1f9e26ce38de952c8f4455a8609
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PHY

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_phy.md`
**SHA256**: `2a53ad759444c88c25c183d2990ecd2fbb85c1f9e26ce38de952c8f4455a8609`

## Summary



# PHY

base:supercpu_phy

                # PHY

```
    /*-------------------------------------------------------------------------
    OP CODE: PHY (PusH index register Y to stack)
    =============================================
    
    Addressing Modes:
        Stack                            ($5a - 1 byte, 3 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    Flags Affected:
        N/A
    Description:
        Push the contents of the Y index register onto the stack...
