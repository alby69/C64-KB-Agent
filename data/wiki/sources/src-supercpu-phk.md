---
id: src-supercpu-phk
type: source
title: 'Source Summary: PHK'
aliases:
- PHK
- supercpu_phk.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_phk.md
  sha256: 885cea043a80b2e76a8a1c47f999c0373b94714108df874c9fa90b5b4a3ae97f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PHK

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_phk.md`
**SHA256**: `885cea043a80b2e76a8a1c47f999c0373b94714108df874c9fa90b5b4a3ae97f`

## Summary



# PHK

base:supercpu_phk

                # PHK

```
    /*-------------------------------------------------------------------------
    OP CODE: PHK (PusH program bank register)
    =========================================
    
    Addressing Modes:
        Stack (Push)                     ($4b - 1 byte, 3 cycles)
    Flags Affected:
        N/A
    Description:
        Push the program bank register onto the stack.
        The single-byte contents of the program bank register are pushed. Th...
