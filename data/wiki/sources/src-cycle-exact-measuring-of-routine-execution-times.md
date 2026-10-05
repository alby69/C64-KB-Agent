---
id: src-cycle-exact-measuring-of-routine-execution-times
type: source
title: 'Source Summary: Cycle Exact Measuring of Execution Times'
aliases:
- Cycle Exact Measuring of Execution Times
- cycle_exact_measuring_of_routine_execution_times.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/cycle_exact_measuring_of_routine_execution_times.md
  sha256: e896929500ca0447eff76f7b585c94655710a2edd0956876bc22c0d9e27d6a74
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Cycle Exact Measuring of Execution Times

**Raw Source File**: `data/docs/codebase_c64_org/base/cycle_exact_measuring_of_routine_execution_times.md`
**SHA256**: `e896929500ca0447eff76f7b585c94655710a2edd0956876bc22c0d9e27d6a74`

## Summary




# Cycle Exact Measuring of Execution Times

# Cycle Exact Measuring of Execution Times

In most cases one will measure how long certain subroutines take to execute by changing the border colors. This is usually sufficient to see how many rasters are wasted, but sometimes you want to know the exact number of cycles spent, or the routine in question takes more than a frame to execute, causing the color changes overlap in a way that makes it difficult to see where the execution starts and ends. ...
