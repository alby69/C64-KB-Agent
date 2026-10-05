---
id: src-supercpu-xce
type: source
title: 'Source Summary: XCE'
aliases:
- XCE
- supercpu_xce.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_xce.md
  sha256: 15e9d21b20b2ee631e178b67bfd258787d5505a15f26c8ec49a53ad4c14853f9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: XCE

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_xce.md`
**SHA256**: `15e9d21b20b2ee631e178b67bfd258787d5505a15f26c8ec49a53ad4c14853f9`

## Summary



# XCE

base:supercpu_xce

                # XCE

```
    /*-------------------------------------------------------------------------
    OP CODE: XCE (Exchange Carry and Emulation bits)
    ================================================
    
    Addressing Modes:
        Implied                            ($fb - 1 byte, 2 cycles)
    Flags Affected:
        e - Takes carry’s previous value: set if carry was set; else cleared.
        c - Takes emulation’s previous value: set if previous mode...
