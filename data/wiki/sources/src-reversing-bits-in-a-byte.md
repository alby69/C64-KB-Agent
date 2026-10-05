---
id: src-reversing-bits-in-a-byte
type: source
title: 'Source Summary: Reversing bits in a byte'
aliases:
- Reversing bits in a byte
- reversing_bits_in_a_byte.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/reversing_bits_in_a_byte.md
  sha256: b918dc7ff45f3ed7f91a20a039c3409a5020aefb2d8c10dd66f0120fbb03146e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Reversing bits in a byte

**Raw Source File**: `data/docs/codebase_c64_org/base/reversing_bits_in_a_byte.md`
**SHA256**: `b918dc7ff45f3ed7f91a20a039c3409a5020aefb2d8c10dd66f0120fbb03146e`

## Summary



# Reversing bits in a byte

base:reversing_bits_in_a_byte

                # Reversing bits in a byte

If you quickly need to flip the bits in a byte in reverse (turning bits from 01234567 to 76543210) you can use this unrolled loop.

```
        ldx #0
.for(var i=0;i<8;i++)
{
        lsr // shift A down, bit 0 to C
        tay // copy to Y doesn't change C
        txa // pull x to a, doesn't change C
        rol // shift left, C to bit 0
        tax // stash a in x
        tya // get start a ...
