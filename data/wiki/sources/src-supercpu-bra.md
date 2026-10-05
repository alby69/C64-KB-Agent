---
id: src-supercpu-bra
type: source
title: 'Source Summary: BRA / BRL'
aliases:
- BRA / BRL
- supercpu_bra.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_bra.md
  sha256: ec075e24cd7e18be927e512089a6d475563a726e402bbe7751a46b560024f17d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BRA / BRL

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_bra.md`
**SHA256**: `ec075e24cd7e18be927e512089a6d475563a726e402bbe7751a46b560024f17d`

## Summary



# BRA / BRL

base:supercpu_bra

                # BRA / BRL

This pseudocommand merges both BRA and BRL opcommands and chooses automatically which one to use.

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: BRA (BRanch Always)
    //
    // Addressing Modes:
    //   Program Counter Relative                ($80 - 2 bytes, 3 cycles¹)
    //   Program Counter Relative Long           ($82 - 3 bytes, 4 cycles)
    /...
