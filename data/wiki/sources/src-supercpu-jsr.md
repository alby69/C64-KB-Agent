---
id: src-supercpu-jsr
type: source
title: 'Source Summary: JSR'
aliases:
- JSR
- supercpu_jsr.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_jsr.md
  sha256: d907a9913ccbd9fc74b3a27b9ce7eaae8d4c14419b33948ad05e7a70e600447c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: JSR

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_jsr.md`
**SHA256**: `d907a9913ccbd9fc74b3a27b9ce7eaae8d4c14419b33948ad05e7a70e600447c`

## Summary



# JSR

base:supercpu_jsr

                # JSR

```
    /*-------------------------------------------------------------------------
    OP CODE: JSR (Jump to SubRoutine)
    =================================
    
    Addressing Modes:
        Absolute                         ($20 - 3 bytes, 6 cycles)
        Absolute Indexed Indirect        ($fc - 3 bytes, 8 cycles)
        Absolute Long                    ($22 - 4 bytes, 8 cycles)
    Flags Affected:
        N/A
    Description:
        Tran...
