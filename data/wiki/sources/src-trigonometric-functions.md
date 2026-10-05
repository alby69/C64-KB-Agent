---
id: src-trigonometric-functions
type: source
title: 'Source Summary: Trigonometric Functions'
aliases:
- Trigonometric Functions
- trigonometric_functions.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/trigonometric_functions.md
  sha256: c867ab7281103fd69c9ae555caef98d7fc3209d763327af7d790dc047e7a2243
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Trigonometric Functions

**Raw Source File**: `data/docs/codebase_c64_org/base/trigonometric_functions.md`
**SHA256**: `c867ab7281103fd69c9ae555caef98d7fc3209d763327af7d790dc047e7a2243`

## Summary



# Trigonometric Functions

# Trigonometric Functions

okay, well there's no magic here other than using tables. That is you simply precalculate a bunch of Cosines / Sines into a lookup table and use that. In 99.99% of the time it ends up in a 256 byte long table, as we're living in a 8 bit world, and wrapping around is a nice feat.

a little pseudo c64 basic code here:

c=2*pi/256
for x=0 to 2*pi step c
value=(sin(x)*128)
if value<0 then value=255-value+1
poke 8192+q,sine
q=q+1
next x

the c64...
