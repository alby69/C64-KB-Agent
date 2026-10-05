---
id: src-b3a2-float-y-into-fac-giving-value-0-255
type: source
title: 'Source Summary: FLOAT (Y) INTO FAC, GIVING VALUE 0-255'
aliases:
- FLOAT (Y) INTO FAC, GIVING VALUE 0-255
- b3a2-float-y-into-fac-giving-value-0-255.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3a2-float-y-into-fac-giving-value-0-255.md
  sha256: c4bfdb6689cb8a3492b16d93505373994a76f0b6a5e4c84c921bf9547bf53f31
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: FLOAT (Y) INTO FAC, GIVING VALUE 0-255

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b3a2-float-y-into-fac-giving-value-0-255.md`
**SHA256**: `c4bfdb6689cb8a3492b16d93505373994a76f0b6a5e4c84c921bf9547bf53f31`

## Summary



# $B3A2 — FLOAT (Y) INTO FAC, GIVING VALUE 0-255

## Disassemblatura
```assembly
.B3A2  A9 00    LDA #$00   ; MSB = 0
.B3A4  F0 EB    BEQ $B391   ; ...ALWAYS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B3A2**: MSB = 0
- **$B3A4**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
