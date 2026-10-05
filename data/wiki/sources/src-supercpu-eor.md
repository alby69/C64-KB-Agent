---
id: src-supercpu-eor
type: source
title: 'Source Summary: EOR'
aliases:
- EOR
- supercpu_eor.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_eor.md
  sha256: 2df8b6c2361c50d5a11e6bd672efb1c3b4d0a10cee7ac03cf21c7700185728ee
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: EOR

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_eor.md`
**SHA256**: `2df8b6c2361c50d5a11e6bd672efb1c3b4d0a10cee7ac03cf21c7700185728ee`

## Summary



# EOR

base:supercpu_eor

                # EOR

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: EOR16 (Exclusive-OR accumulator with memory)
    //
    // Addressing Modes:
    //   Immediate                               ($49 - 2 bytes*, 2 cycles¹)
    //   Absolute                                ($4d - 3 bytes, 4 cycles¹)
    //   Absolute Long                           ($4f - 4 bytes, 5 cycles¹)
    //   Dire...
