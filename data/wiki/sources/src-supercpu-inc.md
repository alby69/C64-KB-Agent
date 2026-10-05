---
id: src-supercpu-inc
type: source
title: 'Source Summary: INC'
aliases:
- INC
- supercpu_inc.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_inc.md
  sha256: a1baa918ceb870c66840b3084442761ca979b327851025046c997436319585d7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: INC

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_inc.md`
**SHA256**: `a1baa918ceb870c66840b3084442761ca979b327851025046c997436319585d7`

## Summary



# INC

base:supercpu_inc

                # INC

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: INC16 (INCrement)
    //
    // Addressing Modes:
    //   Accumulator                             ($1a - 1 bytes, 2 cycles)
    //   Absolute                                ($ee - 3 bytes, 6 cycles¹)
    //   Direct Page (Also DP)                   ($e6 - 2 bytes, 5 cycles¹²)
    //   Absolute Indexed,X              ...
