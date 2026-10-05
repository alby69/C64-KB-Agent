---
id: src-16bit-pseudo-random-generator
type: source
title: 'Source Summary: 16 bit Pseudo Random Generator'
aliases:
- 16 bit Pseudo Random Generator
- 16bit_pseudo_random_generator.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/16bit_pseudo_random_generator.md
  sha256: 1f40ca54f93608648635e696ed8f5eee58723649e3a76b4efd499e809c5037dc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 16 bit Pseudo Random Generator

**Raw Source File**: `data/docs/codebase_c64_org/base/16bit_pseudo_random_generator.md`
**SHA256**: `1f40ca54f93608648635e696ed8f5eee58723649e3a76b4efd499e809c5037dc`

## Summary



# 16 bit Pseudo Random Generator

base:16bit_pseudo_random_generator

                # 16 bit Pseudo Random Generator

The original creator of this routine is unknown.

```
;---------------------------------------------------------------------------
;pseudo-random routine, value in random+1 (akku also) and random
;---------------------------------------------------------------------------
getrandom:
         lda random+1
         sta temp1
         lda random
         asl a
         rol temp1...
