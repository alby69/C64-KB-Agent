---
id: src-8-bit-to-hexadecimal-conversion
type: source
title: 'Source Summary: base:8_bit_to_hexadecimal_conversion [Codebase64 wiki]'
aliases:
- base:8_bit_to_hexadecimal_conversion [Codebase64 wiki]
- 8_bit_to_hexadecimal_conversion.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8_bit_to_hexadecimal_conversion.md
  sha256: 615ed464f2db0b48a509f819794b0e24038073833cc86088358b68d9512ab8dc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:8_bit_to_hexadecimal_conversion [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/8_bit_to_hexadecimal_conversion.md`
**SHA256**: `615ed464f2db0b48a509f819794b0e24038073833cc86088358b68d9512ab8dc`

## Summary




# base:8_bit_to_hexadecimal_conversion [Codebase64 wiki]

base:8_bit_to_hexadecimal_conversion

                ## 8 bit to hexadecimal conversion

by ABujok

This is another way to print a 8 bit integer value as a HEX value on a C64 Screen. The given integer must be loaded into the accu before calling the routine.

```
; Example:
	lda #$3F        ; load accu immediate with $3f or 63      
        jsr OUTHEX      ; print $3F
        rts             ; bye
```
; Syntax for DASM
BSOUT  = $ffd2	;...
