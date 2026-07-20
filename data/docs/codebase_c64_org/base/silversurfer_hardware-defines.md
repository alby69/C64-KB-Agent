---
title: base:silversurfer_hardware-defines [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asilversurfer_hardware-defines
category: reference
topics: []
difficulty: intermediate
language: none
hardware: []
related: []
scraped_at: '2026-07-20'
---

# base:silversurfer_hardware-defines [Codebase64 wiki]

base:silversurfer_hardware-defines

                ## SilverSurfer hardware defines

rs16550base = $de08 fifo_rxd = rs16550base+$00 ;8 (r) fifo_txd = rs16550base+$00 ;8 (w) fifo_dll = rs16550base+$00 ;8 (r/w) fifo_dlm = rs16550base+$01 ;9 (r/w) fifo_ier = rs16550base+$01 ;9 fifo_fcr = rs16550base+$02 ;a (w) fifo_iir = rs16550base+$02 ;a (r) fifo_lcr = rs16550base+$03 ;b fifo_mcr = rs16550base+$04 ;c fifo_lsr = rs16550base+$05 ;d fifo_msr = rs16550base+$06 ;e (r) fifo_scratch = rs16550base+$07 ;f (r/w)

base/silversurfer_hardware-defines.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
rs16550base             = $de08

fifo_rxd     = rs16550base+$00 ;8  (r)
fifo_txd     = rs16550base+$00 ;8 (w)

fifo_dll     = rs16550base+$00 ;8 (r/w)
fifo_dlm     = rs16550base+$01 ;9 (r/w)

fifo_ier     = rs16550base+$01 ;9

fifo_fcr     = rs16550base+$02 ;a (w)
fifo_iir     = rs16550base+$02 ;a (r)
fifo_lcr     = rs16550base+$03 ;b
fifo_mcr     = rs16550base+$04 ;c
fifo_lsr     = rs16550base+$05 ;d
fifo_msr     = rs16550base+$06 ;e (r)
fifo_scratch = rs16550base+$07 ;f (r/w)
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asilversurfer_hardware-defines](https://codebase.c64.org/doku.php?id=base%3Asilversurfer_hardware-defines)*
