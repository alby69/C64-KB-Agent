---
id: src-shortest-stable-raster
type: source
title: 'Source Summary: Shortest Stable Raster code (PAL/NTSC)'
aliases:
- Shortest Stable Raster code (PAL/NTSC)
- shortest_stable_raster.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/shortest_stable_raster.md
  sha256: 0a9d25194ea2e75aaea39e2444a87ee56155068b3ea9fc9d83275dd3c53c207f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Shortest Stable Raster code (PAL/NTSC)

**Raw Source File**: `data/docs/codebase_c64_org/base/shortest_stable_raster.md`
**SHA256**: `0a9d25194ea2e75aaea39e2444a87ee56155068b3ea9fc9d83275dd3c53c207f`

## Summary




# Shortest Stable Raster code (PAL/NTSC)

base:shortest_stable_raster

                # Shortest Stable Raster code (PAL/NTSC)

The polling method, half variance technique, in its shortest form. PAL/NTSC.

```
;64tass format
stirq	.byte $a5	;subroutine
        .byte $ea
        .byte $a9 	;for NTSC, change this to $ea
        .byte $ea
	ldy #$07    
-       dey
        bne -
        inx
        rts
        ldx #$28	;main start is here!
-       cpx $d012
        bne -
        
        jsr sti...
