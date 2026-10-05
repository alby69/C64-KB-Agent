---
id: src-32-bit-hexadecimal-to-decimal-conversion
type: source
title: 'Source Summary: 32 bit hexadecimal to decimal conversion'
aliases:
- 32 bit hexadecimal to decimal conversion
- 32_bit_hexadecimal_to_decimal_conversion.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/32_bit_hexadecimal_to_decimal_conversion.md
  sha256: 7cf676f5255993953d6a977799571397e8755d88432c75e80b3e0c7edee32340
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 32 bit hexadecimal to decimal conversion

**Raw Source File**: `data/docs/codebase_c64_org/base/32_bit_hexadecimal_to_decimal_conversion.md`
**SHA256**: `7cf676f5255993953d6a977799571397e8755d88432c75e80b3e0c7edee32340`

## Summary




# 32 bit hexadecimal to decimal conversion

base:32_bit_hexadecimal_to_decimal_conversion

                # 32 bit hexadecimal to decimal conversion

By Graham.

In cases you need to print decimal values, you can use this routine to convert any unsigned 32 bit value to decimal. It doesn't use the BCD mode. The conversion is done by repeatedly dividing the 32 bit value by 10 and storing the remainder of each division as decimal digits.

```
        ; prints a 32 bit value to the screen
printd...
