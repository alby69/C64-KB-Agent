---
id: src-supercpu-tsc
type: source
title: 'Source Summary: TSC'
aliases:
- TSC
- supercpu_tsc.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_tsc.md
  sha256: 60db9250180392b79a1933e3eb806c8d59494d9533a7bc1d2147fdfd53b68b34
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TSC

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_tsc.md`
**SHA256**: `60db9250180392b79a1933e3eb806c8d59494d9533a7bc1d2147fdfd53b68b34`

## Summary



# TSC

base:supercpu_tsc

                # TSC

```
    /*-------------------------------------------------------------------------
    OP CODE: TSC (Transfer Stack pointer to 16-bit aCcumulator)
    ===========================================================
    Addressing Modes:
        Implied                            ($3b - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transfe...
