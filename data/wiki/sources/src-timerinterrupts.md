---
id: src-timerinterrupts
type: source
title: 'Source Summary: base:timerinterrupts [Codebase64 wiki]'
aliases:
- base:timerinterrupts [Codebase64 wiki]
- timerinterrupts.md
tags:
- sprite programming
- basic
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/timerinterrupts.md
  sha256: b51fa65814d1ef3ac5f6ef39ad16aec9197ef194ef95259149e8e5d20b4d6c60
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:timerinterrupts [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/timerinterrupts.md`
**SHA256**: `b51fa65814d1ef3ac5f6ef39ad16aec9197ef194ef95259149e8e5d20b4d6c60`

## Summary




# base:timerinterrupts [Codebase64 wiki]

base:timerinterrupts

                A sourcecode for doing a CIA IRQ Timer A interrupt Example: If you want to play a music file with init at $1000 and play at $1003 Add jsr $1000 at “Initcode” comment and jsr $1003 at “add code here”

```
;Cia Timer B interrupt example by Terric(Anders L) in 2011
;This example shows a stable one frame CIA Timer B interrupt.
;This piece of code fires of at same cycle on PAL, NTSC, NTSCOLD, DREAN
;Revision 4, Compile...
