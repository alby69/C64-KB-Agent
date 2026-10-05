---
id: src-decimal-mode-in-nmos-6500-series
type: source
title: 'Source Summary: Decimal mode in NMOS 6500 series'
aliases:
- Decimal mode in NMOS 6500 series
- decimal_mode_in_nmos_6500_series.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/decimal_mode_in_nmos_6500_series.md
  sha256: 237e826dc72f77cff0a527a72d6efbe91ac52623dc88bc504e505e2d5c27d3e1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Decimal mode in NMOS 6500 series

**Raw Source File**: `data/docs/codebase_c64_org/base/decimal_mode_in_nmos_6500_series.md`
**SHA256**: `237e826dc72f77cff0a527a72d6efbe91ac52623dc88bc504e505e2d5c27d3e1`

## Summary



# Decimal mode in NMOS 6500 series

base:decimal_mode_in_nmos_6500_series

                # Decimal mode in NMOS 6500 series

Most sources claim that the NMOS 6500 series sets the N, V and Z flags unpredictably when performing addition or subtraction in decimal mode. Of course, this is not true. While testing how the flags are set, I also wanted to see what happens if you use illegal BCD values.

ADC works in Decimal mode in a quite complicated way. It is amazing how it can do that all in a s...
