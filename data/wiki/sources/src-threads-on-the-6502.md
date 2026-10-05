---
id: src-threads-on-the-6502
type: source
title: 'Source Summary: Threads on the 6502'
aliases:
- Threads on the 6502
- threads_on_the_6502.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/threads_on_the_6502.md
  sha256: 10550331a87ea2b25c337219f0501d3af4007dc3285ba205a33794408b4e9a85
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Threads on the 6502

**Raw Source File**: `data/docs/codebase_c64_org/base/threads_on_the_6502.md`
**SHA256**: `10550331a87ea2b25c337219f0501d3af4007dc3285ba205a33794408b4e9a85`

## Summary




# Threads on the 6502

# Threads on the 6502

By Gregg.

Threads on the 6502, at first this might sound to be a little useless on the 6502 or inefficient to implement. But in fact, utilizing the stack, it is really easy, and has quite a few uses. Sometimes it can make code more elegant too.

In this example two threads will be initiated which will use different stack areas. Using a round-robin scheduler running in an irq (context_switch) these threads are ran one after the other. The thread d...
