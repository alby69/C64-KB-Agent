---
id: src-supercpu-adc
type: source
title: 'Source Summary: ADC'
aliases:
- ADC
- supercpu_adc.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/supercpu_adc.md
  sha256: 503dbec099913db553bb224aa28ccf9df3657bb816f486f2907ef194518584de
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ADC

**Raw Source File**: `data/docs/codebase_c64_org/base/supercpu_adc.md`
**SHA256**: `503dbec099913db553bb224aa28ccf9df3657bb816f486f2907ef194518584de`

## Summary



# ADC

base:supercpu_adc

                # ADC

```
    //---------------------------------------------------------------------------------------------
    // PseudoCommand-OPC: ADC16 (ADd with Carry)
    //
    // Addressing Modes:
    //   Immediate                               ($69 - 2 bytes*, 2 cycles¹°)
    //   Absolute                                ($6d - 3 bytes, 4 cycles¹°)
    //   Absolute Long                           ($6f - 4 bytes, 5 cycles¹°)
    //   Direct Page (also DP)  ...
