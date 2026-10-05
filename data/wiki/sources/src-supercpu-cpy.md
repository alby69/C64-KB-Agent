---
id: src-supercpu-cpy
type: source
title: 'Source Summary: CPY'
aliases:
- CPY
- supercpu_cpy.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_cpy.md
  sha256: 769b1f09c4b5395da77f8bc6840813d48941958e8d89f0ef6dde0934c6499c77
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CPY

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_cpy.md`
**SHA256**: `769b1f09c4b5395da77f8bc6840813d48941958e8d89f0ef6dde0934c6499c77`

## Summary



# CPY

base:supercpu_cpy

                # CPY

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: CPY (ComPare index Register Y with memory)
    //
    // Addressing Modes:
    //   Immediate                               ($c0 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($cc - 3 bytes, 4 cycles¹)
    //   Direct Page (also DP)                   ($c4 - 2 bytes, 3 cycles¹²)
    //   * - A...
