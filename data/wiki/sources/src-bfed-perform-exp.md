---
id: src-bfed-perform-exp
type: source
title: 'Source Summary: perform EXP()'
aliases:
- perform EXP()
- bfed-perform-exp.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bfed-perform-exp.md
  sha256: d444ba9017586136ee7f0d36671ba89dd66d75ee380f41a2f71035121fbe2ed9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform EXP()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bfed-perform-exp.md`
**SHA256**: `d444ba9017586136ee7f0d36671ba89dd66d75ee380f41a2f71035121fbe2ed9`

## Summary



# $BFED — perform EXP()

## Disassemblatura
```assembly
.BFED  A9 BF    LDA #$BF   ; set 1.443 pointer low byte
.BFEF  A0 BF    LDY #$BF   ; set 1.443 pointer high byte
.BFF1  20 28 BA JSR $BA28   ; do convert AY, FCA1*(AY)
.BFF4  A5 70    LDA $70   ; get FAC1 rounding byte
.BFF6  69 50    ADC #$50   ; +$50/$100
.BFF8  90 03    BCC $BFFD   ; skip rounding if no carry
.BFFA  20 23 BC JSR $BC23   ; round FAC1 (no check)
.BFFD  4C 00 E0 JMP $E000   ; continue EXP()
```


## Commenti

### Original...
