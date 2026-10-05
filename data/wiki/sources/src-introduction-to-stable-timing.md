---
id: src-introduction-to-stable-timing
type: source
title: 'Source Summary: Introduction to stable timing'
aliases:
- Introduction to stable timing
- introduction_to_stable_timing.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/introduction_to_stable_timing.md
  sha256: 27f6c32d242347c128d768c8e5a42d8d58e2f54d2d41dcb7dfdcd76ad03cc6a5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Introduction to stable timing

**Raw Source File**: `data/docs/codebase_c64_org/base/introduction_to_stable_timing.md`
**SHA256**: `27f6c32d242347c128d768c8e5a42d8d58e2f54d2d41dcb7dfdcd76ad03cc6a5`

## Summary




# Introduction to stable timing

### Table of Contents

# Introduction to stable timing

The definition of stable timing is to synchronize the CPU to an external signal so that after synchronization the CPU and the synchronization point is always at a constant cycles apart.

Most commonly is to synchronize the CPU to the raster beam to achieve all those glorious VIC-tricks that require cycle precise timing. Not uncommon either is to synchronize the CPU with the drive code so that you can burs...
