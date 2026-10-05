---
id: src-using-a-timer-as-an-inverted-raster-x-pos-register-method
type: source
title: 'Source Summary: Using a Timer as an Inverted Raster X-Pos Register'
aliases:
- Using a Timer as an Inverted Raster X-Pos Register
- using_a_timer_as_an_inverted_raster_x-pos_register_method.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/using_a_timer_as_an_inverted_raster_x-pos_register_method.md
  sha256: e0601259ea1bd06d9b4845ded4bca19c17258582855f1ecf76a0624da3700b34
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Using a Timer as an Inverted Raster X-Pos Register

**Raw Source File**: `data/docs/codebase_c64_org/base/using_a_timer_as_an_inverted_raster_x-pos_register_method.md`
**SHA256**: `e0601259ea1bd06d9b4845ded4bca19c17258582855f1ecf76a0624da3700b34`

## Summary




# Using a Timer as an Inverted Raster X-Pos Register

# Using a Timer as an Inverted Raster X-Pos Register

Hi, I'm Hermit Soft. On CSDB I've shared my strongly optimized (shortened) CIA-timer using stable raster method. Now it's here to fill the gap in Codebase64. I hope it will be useful in “everyday's demo coding” . :)

A short pre-description: The first cmp$d012, bne*-3 waits till the raster-row given in the Accu. The occurence of this testing jitters in 1…7 cycles to the real starting (c...
