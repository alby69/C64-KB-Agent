---
id: src-supercpu-phd
type: source
title: 'Source Summary: PHD'
aliases:
- PHD
- supercpu_phd.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_phd.md
  sha256: a4d7c734489e5c6113d48156c3d2ff08f7aa23cbdd8230fbc57cfb0330504ce9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PHD

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_phd.md`
**SHA256**: `a4d7c734489e5c6113d48156c3d2ff08f7aa23cbdd8230fbc57cfb0330504ce9`

## Summary



# PHD

base:supercpu_phd

                # PHD

```
    /*-------------------------------------------------------------------------
    OP CODE: PHD (PusH Direct page register)
    ========================================
    
    Addressing Modes:
        Stack (Push)                    ($0b - 1 byte, 4 cycles)
    Flags Affected:
        N/A
    Description:
        Push the contents of the direct page register D onto the stack.
        Since the direct page register is always a sixteen-bit...
