---
id: src-silversurfer-hardware-defines
type: source
title: 'Source Summary: base:silversurfer_hardware-defines [Codebase64 wiki]'
aliases:
- base:silversurfer_hardware-defines [Codebase64 wiki]
- silversurfer_hardware-defines.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/silversurfer_hardware-defines.md
  sha256: cfca5c1c1b77ba595934946711b46eed651374f4424da2ecc5c30b39d8920f2e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:silversurfer_hardware-defines [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/silversurfer_hardware-defines.md`
**SHA256**: `cfca5c1c1b77ba595934946711b46eed651374f4424da2ecc5c30b39d8920f2e`

## Summary



# base:silversurfer_hardware-defines [Codebase64 wiki]

base:silversurfer_hardware-defines

                ## SilverSurfer hardware defines

rs16550base             = $de08
fifo_rxd     = rs16550base+$00 ;8  (r)
fifo_txd     = rs16550base+$00 ;8 (w)
fifo_dll     = rs16550base+$00 ;8 (r/w)
fifo_dlm     = rs16550base+$01 ;9 (r/w)
fifo_ier     = rs16550base+$01 ;9
fifo_fcr     = rs16550base+$02 ;a (w)
fifo_iir     = rs16550base+$02 ;a (r)
fifo_lcr     = rs16550base+$03 ;b
fifo_mcr     = rs16550b...
