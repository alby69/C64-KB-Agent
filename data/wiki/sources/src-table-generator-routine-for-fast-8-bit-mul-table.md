---
id: src-table-generator-routine-for-fast-8-bit-mul-table
type: source
title: 'Source Summary: Table generator for square table based multiplications'
aliases:
- Table generator for square table based multiplications
- table_generator_routine_for_fast_8_bit_mul_table.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/table_generator_routine_for_fast_8_bit_mul_table.md
  sha256: d0ece98381ca9d074be2a536f094c0dc70bc0ed2626039c739e35e13e9c3e5bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Table generator for square table based multiplications

**Raw Source File**: `data/docs/codebase_c64_org/base/table_generator_routine_for_fast_8_bit_mul_table.md`
**SHA256**: `d0ece98381ca9d074be2a536f094c0dc70bc0ed2626039c739e35e13e9c3e5bc`

## Summary



# Table generator for square table based multiplications

base:table_generator_routine_for_fast_8_bit_mul_table

                # Table generator for square table based multiplications

By Graham.

For the fast 8 bit multiplication routine you need a table containing 512 16-bit values of the function f(x)=int(x*x/4).

Since this table needs to be generated quite often, here is a minimum size routine to calculate that table (36 bytes long):

```
      ldx #$00
      txa
      .byte $c9   ; CMP...
