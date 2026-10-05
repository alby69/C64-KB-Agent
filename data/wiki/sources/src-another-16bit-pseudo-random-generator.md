---
id: src-another-16bit-pseudo-random-generator
type: source
title: 'Source Summary: base:another_16bit_pseudo_random_generator [Codebase64 wiki]'
aliases:
- base:another_16bit_pseudo_random_generator [Codebase64 wiki]
- another_16bit_pseudo_random_generator.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/another_16bit_pseudo_random_generator.md
  sha256: 62aaae3a1276e4f999f35bd037f470fa050e824336bc774b6f66a816650a59b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:another_16bit_pseudo_random_generator [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/another_16bit_pseudo_random_generator.md`
**SHA256**: `62aaae3a1276e4f999f35bd037f470fa050e824336bc774b6f66a816650a59b3`

## Summary



# base:another_16bit_pseudo_random_generator [Codebase64 wiki]

base:another_16bit_pseudo_random_generator

                
Better use this one, which is more evolved: [Two very fast 16bit pseudo random generators as LFSR](https://codebase.c64.org/doku.php?id=base:two_very_fast_16bit_pseudo_random_generators_as_lfsr)

sr=$FD
lda sr+1
asl
asl
eor sr+1
asl
eor sr+1
asl
asl
eor sr+1
asl
rol sr
rol sr+1
rts

base/another_16bit_pseudo_random_generator.txt · Last modified:  by 127.0.0.1

## Codice ...
