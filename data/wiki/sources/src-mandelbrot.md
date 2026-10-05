---
id: src-mandelbrot
type: source
title: 'Source Summary: base:mandelbrot [Codebase64 wiki]'
aliases:
- base:mandelbrot [Codebase64 wiki]
- mandelbrot.md
tags:
- raster interrupts
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/mandelbrot.md
  sha256: 3aae19988c7b9f9a2d22f34a43ac10d6f78ecdc161c138ea38d81059f785c365
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:mandelbrot [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/mandelbrot.md`
**SHA256**: `3aae19988c7b9f9a2d22f34a43ac10d6f78ecdc161c138ea38d81059f785c365`

## Summary



# base:mandelbrot [Codebase64 wiki]

base:mandelbrot

                ## Mandelbrot generator

Using the floating point routines in the BASIC ROM.

The “stdlib.a” which is required by this asm source can be found in the [Resurrection](https://codebase.c64.org/doku.php?id=projects:resurrection) project ZIP file.

```
;Mandelbrot test code
!source "../stdlib/stdlib.a"
!to "Mandelbrot.prg", cbm
!sal
!sl "Mandelbrot.map"
!svl "Mandelbrot.lbl"
!cpu 6510
!ct pet
!source "../stdlib/BASICEntry80d.a"
!...
