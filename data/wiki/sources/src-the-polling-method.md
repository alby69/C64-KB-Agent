---
id: src-the-polling-method
type: source
title: 'Source Summary: Stable raster position by polling $D012'
aliases:
- Stable raster position by polling $D012
- the_polling_method.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/the_polling_method.md
  sha256: c06928d8aa4db425110088b7f0957b74d3d9bdb482f142710cc078181bf1b02f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Stable raster position by polling $D012

**Raw Source File**: `data/docs/codebase_c64_org/base/the_polling_method.md`
**SHA256**: `c06928d8aa4db425110088b7f0957b74d3d9bdb482f142710cc078181bf1b02f`

## Summary




# Stable raster position by polling $D012

# Stable raster position by polling $D012

One method to acheive stable timing and complete synchronization with another signal is simply to poll the signal and take counter measures. The signal in this case could be the raster beam (stable rasters) or f.e. the drive CPU.

Let's examplify this with polling the raster beam. We know $D012 contains lower 8 bits (out of nine) of the current raster line counter, and will increase by one every 63rd cycle.
...
