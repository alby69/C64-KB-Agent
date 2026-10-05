---
id: src-supercpu-lda
type: source
title: 'Source Summary: LDA'
aliases:
- LDA
- supercpu_lda.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_lda.md
  sha256: 7a310d0bda250350eaf73d3a8f50e270bdb73fb2b305e1d10cf40c2703993785
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LDA

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_lda.md`
**SHA256**: `7a310d0bda250350eaf73d3a8f50e270bdb73fb2b305e1d10cf40c2703993785`

## Summary



# LDA

base:supercpu_lda

                # LDA

```
    /*-------------------------------------------------------------------------
    OP CODE: LDA (LoaD Accumulator from memory)
    ===========================================
    
    Addressing Modes:
        Immediate                        ($a9 - 2 bytes*, 2 cycles¹)
        Absolute                         ($ad - 3 bytes, 4 cycles¹)
        Absolute Long                    ($af - 4 bytes, 5 cycles¹)
        Direct Page (also DP)        ...
