---
id: src-scpu-rasterirq-init
type: source
title: 'Source Summary: RasterIRQ'
aliases:
- RasterIRQ
- scpu_rasterirq_init.md
tags:
- raster interrupts
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_rasterirq_init.md
  sha256: da213a64a8572331c469e7fee20b30d927bcd4cf63483923523ecc574327a06d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RasterIRQ

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_rasterirq_init.md`
**SHA256**: `da213a64a8572331c469e7fee20b30d927bcd4cf63483923523ecc574327a06d`

## Summary



# RasterIRQ

base:scpu_rasterirq_init

                # RasterIRQ

Raster Interrupt initialisation code. Grounds NMI and disable IRQ's from CIA Timers.

After all initialisation is completed, the routine clears the interrupt flag and allows an interrupt to occurr once a raster IRQ is triggered by the raster compare value passed to the routine.

Standard Memoryconfiguration set to RAM+IO

| SYNTAX: | :RasterIRQ RasterCompareValue : VectorIRQ |  |  | 
| EXAMPLE: | :RasterIRQ 52 : #IRQ |  |  | 
...
