---
id: src-8bit-divide-8bit-product
type: source
title: 'Source Summary: 8bit Divide - 8bit Result'
aliases:
- 8bit Divide - 8bit Result
- 8bit_divide_8bit_product.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_divide_8bit_product.md
  sha256: 59e57d1040793d4190d0a134e869a5ac548e27eb8a5f49b43e8bc03f86eeeb3e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 8bit Divide - 8bit Result

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_divide_8bit_product.md`
**SHA256**: `59e57d1040793d4190d0a134e869a5ac548e27eb8a5f49b43e8bc03f86eeeb3e`

## Summary



# 8bit Divide - 8bit Result

### Table of Contents

# 8bit Divide - 8bit Result

## Normal binary division

…with shifting in loop. (If I remember right - submitted by Graham at CSDb forum)

```
;normal binary division
        ASL $FD
        LDA #$00
        ROL
        LDX #$08
.loop1
        CMP $FC
        BCC *+4
        SBC $FC
        ROL $FD
        ROL
        DEX
        BNE .loop1
        LDX #$08
.loop2
        CMP $FC
        BCC *+4
        SBC $FC
        ROL $FE
        ASL
   ...
