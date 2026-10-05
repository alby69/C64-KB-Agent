---
id: src-streaming-1-2-4-8-bit-numbers-without-spanning-bytes
type: source
title: 'Source Summary: Packing bitfields evenly into bytes'
aliases:
- Packing bitfields evenly into bytes
- streaming_1_2_4_8-bit_numbers_without_spanning_bytes.md
tags:
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/streaming_1_2_4_8-bit_numbers_without_spanning_bytes.md
  sha256: 2267ef22328f9828c1f76e9f973ab55de7980c7873b0470c75838160c2f9c2d7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Packing bitfields evenly into bytes

**Raw Source File**: `data/docs/codebase_c64_org/base/streaming_1_2_4_8-bit_numbers_without_spanning_bytes.md`
**SHA256**: `2267ef22328f9828c1f76e9f973ab55de7980c7873b0470c75838160c2f9c2d7`

## Summary



# Packing bitfields evenly into bytes

# Packing bitfields evenly into bytes

(I first used this in my FMV system, around 2005 or so? - White Flame)

As long as you're outputting 1, 2, 4, and 8 bit tokens (not 3 or 5-7 bit), you can keep all the bitfields aligned so they do not span byte boundaries, making the reading simpler. No length tokens need to be added to the stream.

The reader will hold a byte-sized buffer each for reading 1, 2, or 4-bit values. If that buffer is empty upon reading i...
