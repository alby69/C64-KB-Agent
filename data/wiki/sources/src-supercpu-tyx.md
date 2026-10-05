---
id: src-supercpu-tyx
type: source
title: 'Source Summary: TYX'
aliases:
- TYX
- supercpu_tyx.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_tyx.md
  sha256: fdd3c59086195ca6db33eab84f736fbc649f23c5873b261bf50d4bab41a821a8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TYX

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_tyx.md`
**SHA256**: `fdd3c59086195ca6db33eab84f736fbc649f23c5873b261bf50d4bab41a821a8`

## Summary



# TYX

base:supercpu_tyx

                # TYX

```
    /*-------------------------------------------------------------------------
    OP CODE: TYX (Transfer index register Y to X)
    =============================================
    
    Addressing Modes:
        Implied                            ($bb - 1 byte, 2 cycles)
    Flags Affected:
        n - Set if most significant bit of transferred value is set; else
            cleared.
        z - Set if value transferred is zero; else clea...
