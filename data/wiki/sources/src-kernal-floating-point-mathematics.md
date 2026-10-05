---
id: src-kernal-floating-point-mathematics
type: source
title: 'Source Summary: Floating Point Math'
aliases:
- Floating Point Math
- kernal_floating_point_mathematics.md
tags:
- sprite programming
- assembly
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/kernal_floating_point_mathematics.md
  sha256: c669969d00e0a336d0d31521320c768c71d6564c9d1f1918f8001ee3b416c07b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Floating Point Math

**Raw Source File**: `data/docs/codebase_c64_org/base/kernal_floating_point_mathematics.md`
**SHA256**: `c669969d00e0a336d0d31521320c768c71d6564c9d1f1918f8001ee3b416c07b`

## Summary



# Floating Point Math

# Floating Point Math

[Floating point](http://en.wikipedia.org/wiki/Floating_point) numbers are handled by the C64's BASIC and Kernal ROMs. Called directly from machine language programs, they execute faster than when burdened by the BASIC interpreter. The difficulty lies in the variety of ways you must prepare the registers and zero-page before calling certain routines. Macros are recommended when dealing with FP in assembly.


Floating point numbers are stored with 5 ...
