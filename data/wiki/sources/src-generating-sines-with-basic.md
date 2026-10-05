---
id: src-generating-sines-with-basic
type: source
title: 'Source Summary: Generating Sines through BASIC'
aliases:
- Generating Sines through BASIC
- generating_sines_with_basic.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/generating_sines_with_basic.md
  sha256: a0146aaa76c097440a3e8bf53623804d36858f0092107145f3743c64c0f5e2d0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Generating Sines through BASIC

**Raw Source File**: `data/docs/codebase_c64_org/base/generating_sines_with_basic.md`
**SHA256**: `a0146aaa76c097440a3e8bf53623804d36858f0092107145f3743c64c0f5e2d0`

## Summary



# Generating Sines through BASIC

base:generating_sines_with_basic

                # Generating Sines through BASIC

By Doynax

Generating sines in BASIC is slow, but might be suitable for programs that need to be small. Improve if you can!

The routine is currently 28 bytes long and takes 5.9 seconds to execute:

table	= $0400		;; The output is a set of negated (phase-shifted by 180°)
			;; sines between -128 and +127.
			;; Preferably a low page. Must be paged aligned!
loop	lda #<index	;; L...
