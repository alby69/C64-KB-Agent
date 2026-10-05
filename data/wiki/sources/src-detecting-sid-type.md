---
id: src-detecting-sid-type
type: source
title: 'Source Summary: Method used in "Mathematica" by Reflex'
aliases:
- Method used in "Mathematica" by Reflex
- detecting_sid_type.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/detecting_sid_type.md
  sha256: bbfddb061325daae58cb9e8be0ef172c10e6a8b9948df63d72a8ba025f01403b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Method used in "Mathematica" by Reflex

**Raw Source File**: `data/docs/codebase_c64_org/base/detecting_sid_type.md`
**SHA256**: `bbfddb061325daae58cb9e8be0ef172c10e6a8b9948df63d72a8ba025f01403b`

## Summary



# Method used in "Mathematica" by Reflex

base:detecting_sid_type

                # Method used in "Mathematica" by Reflex

```
;;;;;
;;;;  detecting sid type (disassembled from Mathematica by Reflex)
;;;
;;    commented and labelled by Raf/Vulture Design
;
	; subroutine filling SID's registers with $00
        LDX #24
        LDA #0
loop    STA $D400,x
        DEX
        BPL loop
	; main routine
        LDA #$02
	STA $D40F
	LDA #$30
	STA $D412
	LDY #$00
	LDX #$00
sl3	LDA $D41B
	BMI sl2
	DEX...
