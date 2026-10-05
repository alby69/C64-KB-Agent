---
id: src-two-very-fast-16bit-pseudo-random-generators-as-lfsr
type: source
title: 'Source Summary: base:two_very_fast_16bit_pseudo_random_generators_as_lfsr
  [Codebase64 wiki]'
aliases:
- base:two_very_fast_16bit_pseudo_random_generators_as_lfsr [Codebase64 wiki]
- two_very_fast_16bit_pseudo_random_generators_as_lfsr.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/two_very_fast_16bit_pseudo_random_generators_as_lfsr.md
  sha256: fb86582335308a4659a3e7e210ee380f9d1edb56d663cfe048ecb96cc1a8036a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:two_very_fast_16bit_pseudo_random_generators_as_lfsr [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/two_very_fast_16bit_pseudo_random_generators_as_lfsr.md`
**SHA256**: `fb86582335308a4659a3e7e210ee380f9d1edb56d663cfe048ecb96cc1a8036a`

## Summary



# base:two_very_fast_16bit_pseudo_random_generators_as_lfsr [Codebase64 wiki]

base:two_very_fast_16bit_pseudo_random_generators_as_lfsr

                ;LFSR random generators
;
;with cc65 compiler/assembler package
;compile: ca65 -t c64 random.s && ld65 -t c64 -o random random.o c64.lib
;
;© 2007 Hanno Behrens (pebbles@schattenlauf.de)
;LGPL Licence
;
;Call random and you get a lowbyte in A and an highbyte in Y
;you should only use the 8 bit lowbyte cause thats best random. 
;The full 16 A/...
