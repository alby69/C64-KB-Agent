---
id: src-supercpu-stp
type: source
title: 'Source Summary: STP'
aliases:
- STP
- supercpu_stp.md
tags:
- sprite programming
- basic
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_stp.md
  sha256: f16ed04707074e48e0f14273797132a0da94676bced6a4a06f07ffd2213e1824
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STP

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_stp.md`
**SHA256**: `f16ed04707074e48e0f14273797132a0da94676bced6a4a06f07ffd2213e1824`

## Summary



# STP

base:supercpu_stp

                # STP

```
    /*-------------------------------------------------------------------------
    OP CODE: STP (SToP the processor)
    =================================
    
    Addressing Modes:
        Implied                            ($db - 1 byte, 3 cycles¹)
        ¹ - Uses 3 cycles to shut the processor down; additional cycles are
        required by reset to restart it
    Flags Affected:
        N/A
    Description:
        During the processor...
