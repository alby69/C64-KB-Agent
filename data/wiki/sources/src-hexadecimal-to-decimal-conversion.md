---
id: src-hexadecimal-to-decimal-conversion
type: source
title: 'Source Summary: Hexadecimal to Decimal Conversion'
aliases:
- Hexadecimal to Decimal Conversion
- hexadecimal_to_decimal_conversion.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/hexadecimal_to_decimal_conversion.md
  sha256: 08e701f0a1830ff1659e762485bb32439cee11945b9cb8c9893dbce662516415
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Hexadecimal to Decimal Conversion

**Raw Source File**: `data/docs/codebase_c64_org/base/hexadecimal_to_decimal_conversion.md`
**SHA256**: `08e701f0a1830ff1659e762485bb32439cee11945b9cb8c9893dbce662516415`

## Summary



# Hexadecimal to Decimal Conversion

# Hexadecimal to Decimal Conversion

Without division or multiplication, this first routine takes an 8-bit hex number and returns a 10-bit decimal (BCD) number. It is done by the “add three” algorithm from Motorola AN-757, “Analog-to-Digital Conversion Techniques With the 6800 Microprocessor System” by Don Aldridge. Motorola apparently does not have the app. note on their website. I converted it in the 80's for a 65c02 product. Start with the input number i...
