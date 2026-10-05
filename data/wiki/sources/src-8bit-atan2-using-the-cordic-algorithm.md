---
id: src-8bit-atan2-using-the-cordic-algorithm
type: source
title: 'Source Summary: 8bit_atan2_using_the_cordic_algorithm'
aliases:
- 8bit_atan2_using_the_cordic_algorithm
- 8bit_atan2_using_the_cordic_algorithm.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/8bit_atan2_using_the_cordic_algorithm.md
  sha256: 07c399da34d19daedd1d662c50adf0fcf9d97997b7d1b8c2a17db85465baf7a8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 8bit_atan2_using_the_cordic_algorithm

**Raw Source File**: `data/docs/codebase_c64_org/base/8bit_atan2_using_the_cordic_algorithm.md`
**SHA256**: `07c399da34d19daedd1d662c50adf0fcf9d97997b7d1b8c2a17db85465baf7a8`

## Summary




# 8bit_atan2_using_the_cordic_algorithm

base:8bit_atan2_using_the_cordic_algorithm

                # 8bit_atan2_using_the_cordic_algorithm

By Oswald

64tass source below, it will calculate the angles for the default char screen and display them on it. it is possible to get more than 8 precise bit by increasing the angleslo/hi tables and running the loop as many times as many entries in the tables. 16 is too much, at that stage all bits are 0 in the angleslo/hi tables.

explanation of the a...
