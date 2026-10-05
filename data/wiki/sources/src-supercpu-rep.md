---
id: src-supercpu-rep
type: source
title: 'Source Summary: REP'
aliases:
- REP
- supercpu_rep.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_rep.md
  sha256: ff99fed9d8bc5ac2eadb26b8b059f043dc7cd5b36426fdd1ee180e5527f711ff
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: REP

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_rep.md`
**SHA256**: `ff99fed9d8bc5ac2eadb26b8b059f043dc7cd5b36426fdd1ee180e5527f711ff`

## Summary



# REP

base:supercpu_rep

                # REP

```
    /*-------------------------------------------------------------------------
    OP CODE: REP (REset Status (P) Bits)
    ====================================
    
    Addressing Modes:
        Immediate                        ($c2 - 2 bytes, 3 cycles)
    Flags Affected:
        65802/65816 emulation mode e=1:
            n - Set/Reset
            v - Set/Reset
            d - Set/Reset
            i - Set/Reset
            z - Set/Reset...
