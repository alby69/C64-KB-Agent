---
id: src-supercpu-dey
type: source
title: 'Source Summary: DEY'
aliases:
- DEY
- supercpu_dey.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/supercpu_dey.md
  sha256: 6e938dcefcd6db9444f8a70401e46617a18aa72f72254f1ea42c0945393b8ebc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DEY

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_dey.md`
**SHA256**: `6e938dcefcd6db9444f8a70401e46617a18aa72f72254f1ea42c0945393b8ebc`

## Summary



# DEY

base:supercpu_dey

                # DEY

Dey does not need a special pseudocommand, this is only for conveniance.

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: dey16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to Decrease Y with.
    //
    // SYNTAX:
    //   dey16 Value
    //
    // EXAMPLE:
    //   dey16                                   // Decrease Y...
