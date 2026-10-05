---
id: src-scpu-rastercompare
type: source
title: 'Source Summary: RasterCompare'
aliases:
- RasterCompare
- scpu_rastercompare.md
tags:
- raster interrupts
- assembly
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/scpu_rastercompare.md
  sha256: 36d7dee0d2319eba9d0c747283ff405ee0a68ab5932487eab314c41f5018adb2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RasterCompare

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_rastercompare.md`
**SHA256**: `36d7dee0d2319eba9d0c747283ff405ee0a68ab5932487eab314c41f5018adb2`

## Summary




# RasterCompare

base:scpu_rastercompare

                # RasterCompare

Sets $d011:$d012 to 9 bit value passed to the pseudocommand. Assumes 16 bit Acc.

| SYNTAX: | RasterCompare RasterCompareValue |  |  | 
| EXAMPLE: | RasterCompare 52 |  |  | 
| PARAMETERS: | Type | Minimum | Maximum | 
| RasterCompareValue | U9 | 0 | 312 | 

```
    .pseudocommand RasterCompare val {
        // Sets Both $d012 & $d011 (for Y adresses > 256)
        lda $d011
        and #%0000000001111111
        ora #...
