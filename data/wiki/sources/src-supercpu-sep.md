---
id: src-supercpu-sep
type: source
title: 'Source Summary: SEP'
aliases:
- SEP
- supercpu_sep.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_sep.md
  sha256: 84ff528febb9cd82beb659947365ad49e84f4c26d03b02a48f245cd83fdfc842
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SEP

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_sep.md`
**SHA256**: `84ff528febb9cd82beb659947365ad49e84f4c26d03b02a48f245cd83fdfc842`

## Summary



# SEP

base:supercpu_sep

                # SEP

```
    /*-------------------------------------------------------------------------
    OP CODE: SEP (SEt status bits (P))
    ==================================
    
    Addressing Modes:
        Immediate                        ($e2 - 2 bytes, 3 cycles)
    Flags Affected:
        n - All flags for which an operand bit is set are set to one. All other
            flags are unaffected by the instruction. 65802/65816 emulation e=1
            & ...
