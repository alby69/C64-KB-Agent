---
id: src-e284-fac-angle-as-a-fraction-of-a-full-circle
type: source
title: 'Source Summary: (FAC) = ANGLE AS A FRACTION OF A FULL CIRCLE'
aliases:
- (FAC) = ANGLE AS A FRACTION OF A FULL CIRCLE
- e284-fac-angle-as-a-fraction-of-a-full-circle.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e284-fac-angle-as-a-fraction-of-a-full-circle.md
  sha256: 0a04b4f208f3b225b9c516c2cc919e742dd49060e2ec4ba4552023e472038c1b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: (FAC) = ANGLE AS A FRACTION OF A FULL CIRCLE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e284-fac-angle-as-a-fraction-of-a-full-circle.md`
**SHA256**: `0a04b4f208f3b225b9c516c2cc919e742dd49060e2ec4ba4552023e472038c1b`

## Summary



# $E284 — (FAC) = ANGLE AS A FRACTION OF A FULL CIRCLE

## Disassemblatura
```assembly
.E284  A9 EA    LDA #$EA   ; 1/4 - FRACTION MAKES
.E286  A0 E2    LDY #$E2   ; -3/4 <= FRACTION < 1/4
.E288  20 50 B8 JSR $B850
.E28B  A5 66    LDA $66   ; TEST SIGN OF RESULT
.E28D  48       PHA   ; SAVE SIGN FOR LATER UNFOLDING
.E28E  10 0D    BPL $E29D   ; ALREADY 0...1/4
.E290  20 49 B8 JSR $B849   ; ADD 1/2 TO SHIFT TO -1/4...1/2
.E293  A5 66    LDA $66   ; TEST SIGN
.E295  30 09    BMI $E2A0   ; -1/4.....
