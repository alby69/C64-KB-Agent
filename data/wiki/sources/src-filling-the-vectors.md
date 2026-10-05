---
id: src-filling-the-vectors
type: source
title: 'Source Summary: Filling the vectors'
aliases:
- Filling the vectors
- filling_the_vectors.md
tags:
- sprite programming
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/filling_the_vectors.md
  sha256: cc42eacafd1e6e844a9c870ee23bfe760f661dd7100f66e5ccc78bfcd0b9d078
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Filling the vectors

**Raw Source File**: `data/docs/codebase_c64_org/base/filling_the_vectors.md`
**SHA256**: `cc42eacafd1e6e844a9c870ee23bfe760f661dd7100f66e5ccc78bfcd0b9d078`

## Summary



# Filling the vectors

### Table of Contents

# Filling the vectors

By Bitbreaker/Performers

The attached vector.tar.gz is rather outdated. I rewrote most of the parts of the filler and ended up with 25% faster results. A new tar.gz will come soon, until then i have already updated the source for the fill.asm presented within this article. Have fun reading through the source and detecting new ways to solve the same problem.

## Precautions

For filling polygons you will use some sort of scan...
