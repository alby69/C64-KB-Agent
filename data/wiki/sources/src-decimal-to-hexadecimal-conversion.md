---
id: src-decimal-to-hexadecimal-conversion
type: source
title: 'Source Summary: Decimal to hexadecimal conversion'
aliases:
- Decimal to hexadecimal conversion
- decimal_to_hexadecimal_conversion.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/decimal_to_hexadecimal_conversion.md
  sha256: 55879d2df5afe594a37bd575e8672690476765122aef30268cf3ac7dc87d693f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Decimal to hexadecimal conversion

**Raw Source File**: `data/docs/codebase_c64_org/base/decimal_to_hexadecimal_conversion.md`
**SHA256**: `55879d2df5afe594a37bd575e8672690476765122aef30268cf3ac7dc87d693f`

## Summary



# Decimal to hexadecimal conversion

base:decimal_to_hexadecimal_conversion

                # Decimal to hexadecimal conversion

By Mace

This routine converts two bytes decimal to two bytes hexadecimal. 'hiInput' contains hundreds, 'loInput' contains tens and ones, so $0365 equals #365 decimal. It will be converted to 'hiResult' and 'loResult' (in this case $016d, the hexadecimal of 365).

	.pc = $0810
		lda #$00	; Init result bytes
		sta loResult
		sta hiResult
		lda loInput	; Fetch ones an...
