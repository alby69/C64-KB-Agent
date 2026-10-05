---
id: src-stable-irq-with-dma
type: source
title: 'Source Summary: Stable IRQ with DMA'
aliases:
- Stable IRQ with DMA
- stable_irq_with_dma.md
tags:
- raster interrupts
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/stable_irq_with_dma.md
  sha256: 006970056197153b9600a1edc23f81940170f8d350e024664d3a9985669a2a37
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Stable IRQ with DMA

**Raw Source File**: `data/docs/codebase_c64_org/base/stable_irq_with_dma.md`
**SHA256**: `006970056197153b9600a1edc23f81940170f8d350e024664d3a9985669a2a37`

## Summary




# Stable IRQ with DMA

base:stable_irq_with_dma

                # Stable IRQ with DMA

ChristopherJam's stable IRQ routine using DMA, posted on [http://noname.c64.org/csdb/forums/?roomid=11&topicid=88971](http://noname.c64.org/csdb/forums/?roomid=11&topicid=88971) (cleaned up and converted to ca65 syntax).

	.segment "STARTUP"
 
	.word basicstub		; load address
 
basicstub:
	.word @nextline
	.word 1970 + (.time / 31557600)
	.byte $9e
	.byte <(((init / 1000) .mod 10) + $30)
	.byte <(((init / ...
