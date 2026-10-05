---
id: src-supercpu-and
type: source
title: 'Source Summary: AND'
aliases:
- AND
- supercpu_and.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_and.md
  sha256: 83d464672f669ccc936c6af71754722515953a23ade2fe53ef0d492713d638f8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: AND

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_and.md`
**SHA256**: `83d464672f669ccc936c6af71754722515953a23ade2fe53ef0d492713d638f8`

## Summary



# AND

base:supercpu_and

                # AND

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: AND16 (AND accumulator with memory)
    //
    // Addressing Modes:
    //   Immediate                               ($29 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($2d - 3 bytes, 4 cycles¹)
    //   Absolute Long                           ($2f - 4 bytes, 5 cycles¹)
    //   Direct Page (...
