---
id: src-16bit-and-24bit-sqrt
type: source
title: 'Source Summary: base:16bit_and_24bit_sqrt [Codebase64 wiki]'
aliases:
- base:16bit_and_24bit_sqrt [Codebase64 wiki]
- 16bit_and_24bit_sqrt.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/16bit_and_24bit_sqrt.md
  sha256: 5abcadc149acd6416772acac897d9bbe13775050f327c0c3ccae11a102e7ad32
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:16bit_and_24bit_sqrt [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/16bit_and_24bit_sqrt.md`
**SHA256**: `5abcadc149acd6416772acac897d9bbe13775050f327c0c3ccae11a102e7ad32`

## Summary



# base:16bit_and_24bit_sqrt [Codebase64 wiki]

base:16bit_and_24bit_sqrt

                
this one is from: [http://www.geocities.com/oneelkruns/asm1step.html](http://www.geocities.com/oneelkruns/asm1step.html) (defunct page)

Returns the 8-bit square root in $20 of the 16-bit number in $20 (low) and $21 (high). The remainder is in location $21.

sqrt16
	LDY #$01 ; lsby of first odd number = 1
	STY $22
	DEY
	STY $23 ; msby of first odd number (sqrt = 0)
again
	SEC
	LDA $20 ; save remainder in...
