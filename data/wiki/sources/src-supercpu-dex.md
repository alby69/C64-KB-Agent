---
id: src-supercpu-dex
type: source
title: 'Source Summary: DEX'
aliases:
- DEX
- supercpu_dex.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/supercpu_dex.md
  sha256: ea62be8f00f28ab64d839477795c2d7d0d8568d0ffd725ea7840b1c571820379
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DEX

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_dex.md`
**SHA256**: `ea62be8f00f28ab64d839477795c2d7d0d8568d0ffd725ea7840b1c571820379`

## Summary



# DEX

base:supercpu_dex

                # DEX

Dex does not need a special pseudocommand, this is only for conveniance.

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: dex16
    //
    // DESCRIPTION:
    //   Pseudocommand which allows to pass a value on how much to Decrease X with.
    //
    // SYNTAX:
    //   dex16 Value
    //
    // EXAMPLE:
    //   dex16                                   // Decrease X...
