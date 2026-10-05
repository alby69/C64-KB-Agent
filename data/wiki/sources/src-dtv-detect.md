---
id: src-dtv-detect
type: source
title: 'Source Summary: DTV detect'
aliases:
- DTV detect
- dtv_detect.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/dtv_detect.md
  sha256: 5034cf0f9aae79deebdf94c1b5587452e6c5e4738304f3e371472530f801de73
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: DTV detect

**Raw Source File**: `data/docs/codebase_c64_org/base/dtv_detect.md`
**SHA256**: `5034cf0f9aae79deebdf94c1b5587452e6c5e4738304f3e371472530f801de73`

## Summary




# DTV detect

base:dtv_detect

                # DTV detect

Also detects C64 vs C128, and PAL vs NTSC.

```
;----------------------------------------------------------
; DTV detect v1.0 by TLR (disassembly by groepaz)
;
; returns:
;
; a=$7f c64
;   $ff c128
;   $7d dtv1 (ntsc dtv)
;   $75 dtv2 (early pal dtv)
;   $74 dtv3 (recent pal dtv, hummer game)
;
; x=0 ntsc
;   1 pal
;----------------------------------------------------------
dtvdetect:
        PHP
        SEI
        LDA #$00
       ...
