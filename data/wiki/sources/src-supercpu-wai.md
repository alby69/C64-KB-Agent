---
id: src-supercpu-wai
type: source
title: 'Source Summary: WAI'
aliases:
- WAI
- supercpu_wai.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_wai.md
  sha256: a2b92070259700cd517f8cc672072bfff8fa0036b23fc0609222f650f6ff3566
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: WAI

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_wai.md`
**SHA256**: `a2b92070259700cd517f8cc672072bfff8fa0036b23fc0609222f650f6ff3566`

## Summary



# WAI

base:supercpu_wai

                # WAI

```
    /*-------------------------------------------------------------------------
    OP CODE: WAI (WAit for Interrupt)
    =================================
    
    Addressing Modes:
        Implied                            ($cb - 1 byte, 3 cycles¹)
        ¹ Uses 3 cycles to shut the processor down;
        additional cycles are required by interrupt to restart it
    Flags Affected:
        N/A
    Description:
        It has been the go...
