---
id: src-supercpu-pld
type: source
title: 'Source Summary: PLD'
aliases:
- PLD
- supercpu_pld.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_pld.md
  sha256: 5c10a56d3515a4be5132bd2bfc02478d4a24cf3b9eedfdd19bcef7b68f09ebdf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PLD

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_pld.md`
**SHA256**: `5c10a56d3515a4be5132bd2bfc02478d4a24cf3b9eedfdd19bcef7b68f09ebdf`

## Summary



# PLD

base:supercpu_pld

                # PLD

```
    /*-------------------------------------------------------------------------
    OP CODE: PLD (PulL Direct page register)
    ========================================
    
    Addressing Modes:
        Stack                            ($ab - 1 byte, 5 cycles)
    Flags Affected:
        n - Set if most significant bit of pulled value is set; else cleared.
        z - Set if value pulled is zero; else cleared.
    Description:
        Pull...
