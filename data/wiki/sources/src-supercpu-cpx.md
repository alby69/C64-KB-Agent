---
id: src-supercpu-cpx
type: source
title: 'Source Summary: CPX'
aliases:
- CPX
- supercpu_cpx.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_cpx.md
  sha256: 9f8415ce6b59cbe5532d9edd450425b6a7fc494fc818125f6e814a23f8d318c1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CPX

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_cpx.md`
**SHA256**: `9f8415ce6b59cbe5532d9edd450425b6a7fc494fc818125f6e814a23f8d318c1`

## Summary



# CPX

base:supercpu_cpx

                # CPX

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: CPX16 (ComPare index Register X with memory)
    //
    // Addressing Modes:
    //   Immediate                               ($e0 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($ec - 3 bytes, 4 cycles¹)
    //   Direct Page (also DP)                   ($e4 - 2 bytes, 3 cycles¹²)
    //   * -...
