---
id: src-supercpu-ora
type: source
title: 'Source Summary: ORA'
aliases:
- ORA
- supercpu_ora.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_ora.md
  sha256: 8d359b92fa3adf3c67f5a0c2d5a4fed714045f576c936e9c424567dbd2c75ca3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ORA

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_ora.md`
**SHA256**: `8d359b92fa3adf3c67f5a0c2d5a4fed714045f576c936e9c424567dbd2c75ca3`

## Summary



# ORA

base:supercpu_ora

                # ORA

```
    /*-------------------------------------------------------------------------
    OP CODE: ORA (OR Accumulator with memory)
    =========================================
    
    Addressing Modes:
        Immediate                        ($09 - 2 bytes*, 2 cycles¹)
        Absolute                         ($0d - 3 bytes, 4 cycles¹)
        Absolute Long                    ($0f - 4 bytes, 5 cycles¹)
        Direct Page (also DP)            ...
