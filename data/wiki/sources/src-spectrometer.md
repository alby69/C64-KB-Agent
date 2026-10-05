---
id: src-spectrometer
type: source
title: 'Source Summary: base:spectrometer [Codebase64 wiki]'
aliases:
- base:spectrometer [Codebase64 wiki]
- spectrometer.md
tags:
- raster interrupts
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/spectrometer.md
  sha256: 85387cf709e654ed0082633ed1558573361039fca630dc97652d939f738e9526
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:spectrometer [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/spectrometer.md`
**SHA256**: `85387cf709e654ed0082633ed1558573361039fca630dc97652d939f738e9526`

## Summary



# base:spectrometer [Codebase64 wiki]

base:spectrometer

                This is the code from T.P.C.T.S. demo that calculates the index values for the spectrometer. There are a few tricks in there, but I am sure many people could have written a more optimized version.

I hope it will help you understand how I did it.

Code can be compiled using KickAss.

/Trap

```
.const SID_Ghostbytes = $40                                     // Location of SID Ghostbytes (16 bytes)
///////////////////////...
