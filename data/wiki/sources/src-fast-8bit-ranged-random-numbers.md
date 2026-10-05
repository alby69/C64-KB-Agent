---
id: src-fast-8bit-ranged-random-numbers
type: source
title: 'Source Summary: Fast 8bit ranged random numbers'
aliases:
- Fast 8bit ranged random numbers
- fast_8bit_ranged_random_numbers.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/fast_8bit_ranged_random_numbers.md
  sha256: bcd3b56fe28010427c5f0f4ad509f2fc84141d17404dd75f396b4f6f864c7972
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Fast 8bit ranged random numbers

**Raw Source File**: `data/docs/codebase_c64_org/base/fast_8bit_ranged_random_numbers.md`
**SHA256**: `bcd3b56fe28010427c5f0f4ad509f2fc84141d17404dd75f396b4f6f864c7972`

## Summary



# Fast 8bit ranged random numbers

# Fast 8bit ranged random numbers

by kerm1t

Randomness may be effective, since a random element is chosen from a table that is randomly generated. On the other hand, memory consumption may be quite huge.

The random generator [1…256] I have found on White Flame's page:

```
           lda seed
           beq doEor
           clc
           asl
           beq noEor    ;if the input was $80, skip the EOR
           bcc noEor
doEor      eor #$1d
noEor      sta...
