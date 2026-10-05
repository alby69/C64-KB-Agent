---
id: src-a43a-do-error-x-then-warm-start-the-error-message-vector-is-initialised-to-point-here
type: source
title: 'Source Summary: do error #X then warm start, the error message vector is initialised
  to point here'
aliases:
- 'do error #X then warm start, the error message vector is initialised to point here'
- a43a-do-error-x-then-warm-start-the-error-message-vector-is-initialised-to-point-here.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a43a-do-error-x-then-warm-start-the-error-message-vector-is-initialised-to-point-here.md
  sha256: 4338d1f956e918f7cd4198da885a0494d30a8b3e0d8fc33932e000b9724fa426
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do error #X then warm start, the error message vector is initialised to point here

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a43a-do-error-x-then-warm-start-the-error-message-vector-is-initialised-to-point-here.md`
**SHA256**: `4338d1f956e918f7cd4198da885a0494d30a8b3e0d8fc33932e000b9724fa426`

## Summary



# $A43A — do error #X then warm start, the error message vector is initialised to point here

## Disassemblatura
```assembly
.A43A  8A       TXA   ; copy error number
.A43B  0A       ASL   ; *2
.A43C  AA       TAX   ; copy to index
.A43D  BD 26 A3 LDA $A326,X   ; get error message pointer low byte
.A440  85 22    STA $22   ; save it
.A442  BD 27 A3 LDA $A327,X   ; get error message pointer high byte
.A445  85 23    STA $23   ; save it
.A447  20 CC FF JSR $FFCC   ; close input and output channe...
