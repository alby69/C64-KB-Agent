---
id: src-loops-vs-unrolled
type: source
title: 'Source Summary: Loops vs unrolled loops'
aliases:
- Loops vs unrolled loops
- loops_vs_unrolled.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/loops_vs_unrolled.md
  sha256: 5e0bc387f64c19bb948d4c4054968c800b5d2c074ef995e7757f18185d858dac
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Loops vs unrolled loops

**Raw Source File**: `data/docs/codebase_c64_org/base/loops_vs_unrolled.md`
**SHA256**: `5e0bc387f64c19bb948d4c4054968c800b5d2c074ef995e7757f18185d858dac`

## Summary



# Loops vs unrolled loops

# Loops vs unrolled loops

Often we got tought to unroll loops to save on the overhead a loop gives us by having to decrease a counter and involving another branch. But there are situation where a loop can perform way faster, as we can set up values directly via code modification. A good example is a line algorithm.

Here we need to subtract for e.g. dx from A and in case of underrun add dy to A and advance the x-position. On every change in y-direction we also want ...
