---
id: src-16bit-division-16-bit-result
type: source
title: 'Source Summary: 16-bit Division'
aliases:
- 16-bit Division
- 16bit_division_16-bit_result.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/16bit_division_16-bit_result.md
  sha256: 4467135e7faf2d189652c1c938258f2c4ee8bb8b59f6571bb06864cc26b20dbb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 16-bit Division

**Raw Source File**: `data/docs/codebase_c64_org/base/16bit_division_16-bit_result.md`
**SHA256**: `4467135e7faf2d189652c1c938258f2c4ee8bb8b59f6571bb06864cc26b20dbb`

## Summary



# 16-bit Division

base:16bit_division_16-bit_result

                # 16-bit Division

To make the most common integer multiplication/division routines complete:

divisor = $58     ;$59 used for hi-byte
dividend = $fb	  ;$fc used for hi-byte
remainder = $fd	  ;$fe used for hi-byte
result = dividend ;save memory by reusing divident to store the result
divide	lda #0	        ;preset remainder to 0
	sta remainder
	sta remainder+1
	ldx #16	        ;repeat for each bit: ...
divloop	asl dividend	;d...
