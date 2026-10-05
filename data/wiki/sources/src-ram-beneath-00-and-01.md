---
id: src-ram-beneath-00-and-01
type: source
title: 'Source Summary: RAM beneath 00 and 01'
aliases:
- RAM beneath 00 and 01
- ram_beneath_00_and_01.md
tags:
- sprite programming
- graphics
- memory management
sources:
- path: data/docs/codebase_c64_org/base/ram_beneath_00_and_01.md
  sha256: 8cb826293bdab086b037da64cbbe883e562753bae43d68378b94459839f9de3b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RAM beneath 00 and 01

**Raw Source File**: `data/docs/codebase_c64_org/base/ram_beneath_00_and_01.md`
**SHA256**: `8cb826293bdab086b037da64cbbe883e562753bae43d68378b94459839f9de3b`

## Summary



# RAM beneath 00 and 01

# RAM beneath 00 and 01

On an unexpanded Commodore 64, how does one read the RAM locations $00 and $01?

Well, you cannot do so with the CPU directly, since it resolves these locations into internal addresses. However, the VIC II can see these addresses as external memory. So, just make one sprite with the first bit in the sprite set, and move it over the first two bytes, pretending they are part of a bitmap. By checking the sprite-to-background collision register, yo...
