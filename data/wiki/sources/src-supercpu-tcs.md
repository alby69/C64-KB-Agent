---
id: src-supercpu-tcs
type: source
title: 'Source Summary: TCS'
aliases:
- TCS
- supercpu_tcs.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_tcs.md
  sha256: 0d5911ef25b270216b937d52b8844e7b3e075a81394cd4684db769eeb5b2f4ba
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TCS

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_tcs.md`
**SHA256**: `0d5911ef25b270216b937d52b8844e7b3e075a81394cd4684db769eeb5b2f4ba`

## Summary



# TCS

base:supercpu_tcs

                # TCS

```
    /*-------------------------------------------------------------------------
    OP CODE: TCS (Transfer aCcumulator to Stack pointer)
    ====================================================
    
    Addressing Modes:
        Implied                            ($1b - 1 byte, 2 cycles)
    Flags Affected:
        N/A
    Description:
        Transfer the value in the accumulator to the stack pointer S. The
        accumulator’s value is un...
