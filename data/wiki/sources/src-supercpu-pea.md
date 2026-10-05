---
id: src-supercpu-pea
type: source
title: 'Source Summary: PEA'
aliases:
- PEA
- supercpu_pea.md
tags:
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_pea.md
  sha256: d2e943811438c2b1fdfc9db5c4307f462ab3e16610ede1a914e4bb45fb44fe27
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PEA

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_pea.md`
**SHA256**: `d2e943811438c2b1fdfc9db5c4307f462ab3e16610ede1a914e4bb45fb44fe27`

## Summary



# PEA

base:supercpu_pea

                # PEA

```
    /*-------------------------------------------------------------------------
    OP CODE: PEA (Push Effective Absolute address)
    ==============================================
    
    Addressing Modes:
        Stac (Absolute)                  ($f4 - 3 bytes, 5 cycles)
    Flags Affected:
        N/A
    Description:
        Push the sixteen-bit operand (typically an absolute address) onto the
        stack. The stack pointer is decrem...
