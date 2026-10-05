---
id: src-b853-perform-subtraction-fac1-from-fac2
type: source
title: 'Source Summary: perform subtraction, FAC1 from FAC2'
aliases:
- perform subtraction, FAC1 from FAC2
- b853-perform-subtraction-fac1-from-fac2.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b853-perform-subtraction-fac1-from-fac2.md
  sha256: 3bfc616a2f5d8d8bfa97311b7f1ef5074a142c2213428840e7534f4ff53ce131
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform subtraction, FAC1 from FAC2

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b853-perform-subtraction-fac1-from-fac2.md`
**SHA256**: `3bfc616a2f5d8d8bfa97311b7f1ef5074a142c2213428840e7534f4ff53ce131`

## Summary



# $B853 — perform subtraction, FAC1 from FAC2

## Disassemblatura
```assembly
.B853  A5 66    LDA $66   ; get FAC1 sign (b7)
.B855  49 FF    EOR #$FF   ; complement it
.B857  85 66    STA $66   ; save FAC1 sign (b7)
.B859  45 6E    EOR $6E   ; EOR with FAC2 sign (b7)
.B85B  85 6F    STA $6F   ; save sign compare (FAC1 EOR FAC2)
.B85D  A5 61    LDA $61   ; get FAC1 exponent
.B85F  4C 6A B8 JMP $B86A   ; add FAC2 to FAC1 and return
.B862  20 99 B9 JSR $B999   ; shift FACX A times right (>8 shift...
