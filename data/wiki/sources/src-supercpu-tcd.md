---
id: src-supercpu-tcd
type: source
title: 'Source Summary: TCD'
aliases:
- TCD
- supercpu_tcd.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_tcd.md
  sha256: 0365a643c916858d48eb8ab12c8ea6ef52e1cbd41b6d29803879096ec924611a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TCD

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_tcd.md`
**SHA256**: `0365a643c916858d48eb8ab12c8ea6ef52e1cbd41b6d29803879096ec924611a`

## Summary



# TCD

base:supercpu_tcd

                # TCD

```
    /*-------------------------------------------------------------------------
    OP CODE: TCD (Transfer 16-Bit aCcumulator to Direct page register)
    ==================================================================
    
    Addressing Modes:
        Implied                            ($5b - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - S...
