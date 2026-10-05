---
id: src-32bit-galois-lfsr
type: source
title: 'Source Summary: 32 bit Galois LFSR random generator'
aliases:
- 32 bit Galois LFSR random generator
- 32bit_galois_lfsr.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/32bit_galois_lfsr.md
  sha256: 8f53fb0515378a3c00029c405ac203747f8e0edae5f83c43e1341063ba881888
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 32 bit Galois LFSR random generator

**Raw Source File**: `data/docs/codebase_c64_org/base/32bit_galois_lfsr.md`
**SHA256**: `8f53fb0515378a3c00029c405ac203747f8e0edae5f83c43e1341063ba881888`

## Summary



# 32 bit Galois LFSR random generator

base:32bit_galois_lfsr

                # 32 bit Galois LFSR random generator

A fast random generator based on the CRC32 algorythm.

It uses the CRC32 IEEE 802.3 polynom $04C11DB7 which produces a random number period of 2^32-1 (4.3 billion) numbers.

```
rnd:
        ASL random
        ROL random+1
        ROL random+2
        ROL random+3
        BCC .nofeedback
        LDA random
        EOR #$B7
        STA random
        LDA random+1
        EOR #$1...
