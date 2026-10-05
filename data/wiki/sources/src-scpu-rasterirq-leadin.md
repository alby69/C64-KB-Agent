---
id: src-scpu-rasterirq-leadin
type: source
title: 'Source Summary: RasterIRQLeadIn'
aliases:
- RasterIRQLeadIn
- scpu_rasterirq_leadin.md
tags:
- raster interrupts
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_rasterirq_leadin.md
  sha256: a84856edeb0138bdd8e84de682f362d0fb2cbf45a0c9ab63630a5aa6e6b685de
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RasterIRQLeadIn

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_rasterirq_leadin.md`
**SHA256**: `a84856edeb0138bdd8e84de682f362d0fb2cbf45a0c9ab63630a5aa6e6b685de`

## Summary



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
base/scpu_rasterirq_leadin.txt · Last modified:  by tww

## Codice Estratto

### Snippet...
