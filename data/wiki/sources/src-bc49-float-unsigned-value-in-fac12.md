---
id: src-bc49-float-unsigned-value-in-fac12
type: source
title: 'Source Summary: FLOAT UNSIGNED VALUE IN FAC+1,2'
aliases:
- FLOAT UNSIGNED VALUE IN FAC+1,2
- bc49-float-unsigned-value-in-fac12.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc49-float-unsigned-value-in-fac12.md
  sha256: 89957e21355c1509755511bbc8c478478fa995183ea76d50bad574d1eabd1501
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: FLOAT UNSIGNED VALUE IN FAC+1,2

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc49-float-unsigned-value-in-fac12.md`
**SHA256**: `89957e21355c1509755511bbc8c478478fa995183ea76d50bad574d1eabd1501`

## Summary



# $BC49 — FLOAT UNSIGNED VALUE IN FAC+1,2

## Disassemblatura
```assembly
.BC49  A9 00    LDA #$00   ; CLEAR LOWER 16-BITS OF MANTISSA
.BC4B  85 65    STA $65
.BC4D  85 64    STA $64
.BC4F  86 61    STX $61   ; STORE EXPONENT
.BC51  85 70    STA $70   ; CLEAR EXTENSION
.BC53  85 66    STA $66   ; MAKE SIGN POSITIVE
.BC55  4C D2 B8 JMP $B8D2   ; IF C=0, WILL NEGATE FAC
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC49**: CLEAR LOWER 16-BITS OF MANTISSA
- **$BC4F**: STOR...
