---
id: src-datasette
type: source
title: 'Source Summary: Datasette'
aliases:
- Datasette
- datasette.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/datasette.md
  sha256: b2797488876899d2eda30126af600167bc5d5f9d3f3f1c4218e32718837bb6d0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Datasette

**Raw Source File**: `data/docs/codebase_c64_org/base/datasette.md`
**SHA256**: `b2797488876899d2eda30126af600167bc5d5f9d3f3f1c4218e32718837bb6d0`

## Summary



# Datasette

base:datasette

                # Datasette

The datasette is accessed via $01 (right, it's directly connected to CPU)

You have 3 lines = 3 bits in $01:


bit 5  is Cassette Motor Control (NOTE! It's low-active: 0 = on; 1 = off)

bit 4  is Cassette Switch Sense: 1 = Switch Closed

bit 3  is Cassette Data Output Line


Make sure you don't mess up $00!

Since bit 4 is input and bit 3 obviously output.

Default for $00 on C64 is %00101111 ($2f)


And in case you wondered: you READ f...
