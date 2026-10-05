---
id: src-stable-raster-routine
type: source
title: 'Source Summary: STABLE RASTER ROUTINE'
aliases:
- STABLE RASTER ROUTINE
- stable_raster_routine.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/stable_raster_routine.md
  sha256: 744717748d23dd7799b9e8808fadbf27cc918b2851c37670575325e18faf6ea3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STABLE RASTER ROUTINE

**Raw Source File**: `data/docs/codebase_c64_org/base/stable_raster_routine.md`
**SHA256**: `744717748d23dd7799b9e8808fadbf27cc918b2851c37670575325e18faf6ea3`

## Summary




# STABLE RASTER ROUTINE

base:stable_raster_routine

                # STABLE RASTER ROUTINE

A Raster Stabbing routine using the double IRQ principle. Insert this code after you have pushed your registers onto the stack inside your IRQ code. The routine doesen't care what the actual $d012 value is so it is flexible.

Other Interrupts, $d012 = #$ff, Sprites, Badline and Badline-1 = fuckup.

If you have the KERNAL banked in, you need to modify the IRQ-Vectors.

Kickassembler format

```
//«»«»...
