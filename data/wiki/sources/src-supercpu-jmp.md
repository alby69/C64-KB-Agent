---
id: src-supercpu-jmp
type: source
title: 'Source Summary: JMP'
aliases:
- JMP
- supercpu_jmp.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/supercpu_jmp.md
  sha256: 7ef59b15d7fd3f71ecf3d7bfe092aea5f8f7988d3f442ad78bbb185c3c964097
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: JMP

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_jmp.md`
**SHA256**: `7ef59b15d7fd3f71ecf3d7bfe092aea5f8f7988d3f442ad78bbb185c3c964097`

## Summary



# JMP

base:supercpu_jmp

                # JMP

```
    /*-------------------------------------------------------------------------
    OP CODE: JMP (JuMP)
    ===================
    
    Addressing Modes:
        Absolute                         ($4c - 3 bytes, 3 cycles)
        Absolute Indirect                ($6c - 3 bytes, 5 cycles¹²)
        Absolute Indexed Indirect        ($7c - 3 bytes, 6 cycles)
        Absolute Long                    ($5c - 4 bytes, 4 cycles)
        Absolute Ind...
