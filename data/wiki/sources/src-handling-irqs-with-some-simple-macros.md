---
id: src-handling-irqs-with-some-simple-macros
type: source
title: 'Source Summary: Handling IRQs macros'
aliases:
- Handling IRQs macros
- handling_irqs_with_some_simple_macros.md
tags:
- sprite programming
- basic
- graphics
- assembly
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/handling_irqs_with_some_simple_macros.md
  sha256: 508895d11e502d1ad5877931b9d498831add2ab8e1d073f575fec2229575c77f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Handling IRQs macros

**Raw Source File**: `data/docs/codebase_c64_org/base/handling_irqs_with_some_simple_macros.md`
**SHA256**: `508895d11e502d1ad5877931b9d498831add2ab8e1d073f575fec2229575c77f`

## Summary




# Handling IRQs macros

base:handling_irqs_with_some_simple_macros

                # Handling IRQs macros

Assemble with ACME.

Just notice how the macro ENTER and EXIT are used, to make nice clean demosource with as many IRQ as you need.

;some macros to use for easy raster handling, by rambones
 
!to "part1.prg"
 
 
!zone mainprogram
*=$1000
 
 
;-------------- MACROS ----------------
;;!macro INIT .inadd, .pladd{
; (code here)
;}
 
!macro ENTER{
 pha
 tya
 pha
 txa
 pha
}
 
!macro EXIT .i...
