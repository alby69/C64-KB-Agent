---
id: src-supercpu-phx
type: source
title: 'Source Summary: PHX'
aliases:
- PHX
- supercpu_phx.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_phx.md
  sha256: 58228720093ed76d0a1dd825008302633bf86e11de2c982bf7f39a9973a7aa2c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PHX

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_phx.md`
**SHA256**: `58228720093ed76d0a1dd825008302633bf86e11de2c982bf7f39a9973a7aa2c`

## Summary



# PHX

base:supercpu_phx

                # PHX

```
    /*-------------------------------------------------------------------------
    OP CODE: PHX (PusH index register X to stack)
    =============================================
    Addressing Modes:
        Stack                            ($da - 1 byte, 3 cycles¹)
        ¹ - Add 1 cycle if x = 0 (16-bit index registers)
    Flags Affected:
        N/A
    Description:
        Push the contents of the X index register onto the stack. The...
