---
id: src-6510-instructions-by-addressing-modes
type: source
title: 'Source Summary: base:6510_instructions_by_addressing_modes [Codebase64 wiki]'
aliases:
- base:6510_instructions_by_addressing_modes [Codebase64 wiki]
- 6510_instructions_by_addressing_modes.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/6510_instructions_by_addressing_modes.md
  sha256: a6a41ce4e13d9e0797aef9fd7adae878ecafe681053b95f0e7045f7f0476c721
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:6510_instructions_by_addressing_modes [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/6510_instructions_by_addressing_modes.md`
**SHA256**: `a6a41ce4e13d9e0797aef9fd7adae878ecafe681053b95f0e7045f7f0476c721`

## Summary



# base:6510_instructions_by_addressing_modes [Codebase64 wiki]

base:6510_instructions_by_addressing_modes

                ## 6510 Instructions by Addressing Modes

```
off- ++++++++++ Positive ++++++++++  ---------- Negative ----------
set  00      20      40      60      80      a0      c0      e0      mode
+00  BRK     JSR     RTI     RTS     NOP*    LDY     CPY     CPX     Impl/immed
+01  ORA     AND     EOR     ADC     STA     LDA     CMP     SBC     (indir,x)
+02   t       t       t    ...
