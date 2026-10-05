---
id: src-different-cpu-types
type: source
title: 'Source Summary: Different CPU types'
aliases:
- Different CPU types
- different_cpu_types.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/different_cpu_types.md
  sha256: 07546b12b5d7b38d564817c5ef1d77c0f312cfd27bf86d043e2dff86d50aa73a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Different CPU types

**Raw Source File**: `data/docs/codebase_c64_org/base/different_cpu_types.md`
**SHA256**: `07546b12b5d7b38d564817c5ef1d77c0f312cfd27bf86d043e2dff86d50aa73a`

## Summary



# Different CPU types

base:different_cpu_types

                # Different CPU types

The Rockwell data booklet 29651N52 (technical information about R65C00 microprocessors, dated October 1984), lists the following differences between NMOS R6502 microprocessor and CMOS R65C00 family:

```
 1. Indexed addressing across page boundary.
        NMOS: Extra read of invalid address.
        CMOS: Extra read of last instruction byte.
 2. Execution of invalid op codes.
        NMOS: Some terminate o...
