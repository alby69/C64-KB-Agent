---
title: RasterIRQLeadIn
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_leadin
category: reference
topics:
- raster interrupts
- basic
- assembly
difficulty: advanced
language: assembly
hardware:
- VIC-II
- CPU
related:
- sprite-programming
- raster-interrupts
- vic-ii-registers
scraped_at: '2026-07-14'
---

# RasterIRQLeadIn

base:scpu_rasterirq_leadin

                # RasterIRQLeadIn

Pushes A, X & Y registers to stack in preparation to handle the IRQ. Does not need stabilization as this is handled by the WAI OPC in asynchrenous code.

| SYNTAX: | RasterIRQLeadIn | 
| EXAMPLE: | RasterIRQLeadIn | 
| PARAMETERS: | N/A | 

```
    .pseudocommand RasterIRQLeadIn {
        pha
        phx
        phy
    }
```
base/scpu_rasterirq_leadin.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand RasterIRQLeadIn {
        pha
        phx
        phy
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_leadin](https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_leadin)*
