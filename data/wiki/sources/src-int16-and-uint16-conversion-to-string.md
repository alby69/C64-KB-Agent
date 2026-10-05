---
id: src-int16-and-uint16-conversion-to-string
type: source
title: 'Source Summary: base:int16_and_uint16_conversion_to_string [Codebase64 wiki]'
aliases:
- base:int16_and_uint16_conversion_to_string [Codebase64 wiki]
- int16_and_uint16_conversion_to_string.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/int16_and_uint16_conversion_to_string.md
  sha256: 4061f09a77a218f7d3ce6a085c6c423f000f8b962f48f9429438db213e5880c6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:int16_and_uint16_conversion_to_string [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/int16_and_uint16_conversion_to_string.md`
**SHA256**: `4061f09a77a218f7d3ce6a085c6c423f000f8b962f48f9429438db213e5880c6`

## Summary




# base:int16_and_uint16_conversion_to_string [Codebase64 wiki]

base:int16_and_uint16_conversion_to_string

                
Conversion of a number in int16 (lo/hi) into a string in CnvStr.

_ItoA converts a signed number

_UtoA converts an unsigned number

The conversion is obtained via a BCD intermediate value.

bcd     = $61    ; system Fac, 3 bytes
int16   = $64    ; system Fac, 2 bytes
sgn     byte 0
CnvStr  byte 0,0,0,0,0,0,0      ; 7 bytes: sgn + 5bytes + '\0'
CnvTrm  byte 0,0,0,0,0,0,...
