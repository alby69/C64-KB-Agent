---
id: src-reu-read-and-write
type: source
title: 'Source Summary: Theory'
aliases:
- Theory
- reu_read_and_write.md
tags:
- assembly
- basic
- memory management
sources:
- path: data/docs/codebase_c64_org/base/reu_read_and_write.md
  sha256: fa43d0308d2f7df25597a4d098a0085ae1f2859e902c467f8b334b43f29efc32
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Theory

**Raw Source File**: `data/docs/codebase_c64_org/base/reu_read_and_write.md`
**SHA256**: `fa43d0308d2f7df25597a4d098a0085ae1f2859e902c467f8b334b43f29efc32`

## Summary



# Theory

### Table of Contents

# Theory

The three RAM Expansion Modules 1700, 1764 and 1750 that provide 128, 256 and 512 kilobytes of expanded memory, respectively, are utilized by means of DMA transfers performed by the REC or RAM Expansion Controller. The REC has 11 registers mapped to $DF00-$DF0A in the external IO2 area.

These registers specify each DMA operation as described in the provided source code. Only the status register at $DF00 can be read. The most important register is at ...
