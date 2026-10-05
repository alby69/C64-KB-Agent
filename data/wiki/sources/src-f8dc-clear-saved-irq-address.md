---
id: src-f8dc-clear-saved-irq-address
type: source
title: 'Source Summary: clear saved IRQ address'
aliases:
- clear saved IRQ address
- f8dc-clear-saved-irq-address.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f8dc-clear-saved-irq-address.md
  sha256: 476eec6ffea0a882599678fb131af89bd3f10f592e249e1dcd6f0f9fa3191190
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: clear saved IRQ address

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f8dc-clear-saved-irq-address.md`
**SHA256**: `476eec6ffea0a882599678fb131af89bd3f10f592e249e1dcd6f0f9fa3191190`

## Summary



# $F8DC — clear saved IRQ address

## Disassemblatura
```assembly
.F8DC  A9 00    LDA #$00   ; clear A
.F8DE  8D A0 02 STA $02A0   ; clear saved IRQ address high byte
.F8E1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F8DC**: clear A
- **$F8DE**: clear saved IRQ address high byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
