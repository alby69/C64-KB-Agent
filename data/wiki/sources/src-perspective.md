---
id: src-perspective
type: source
title: 'Source Summary: base:perspective [Codebase64 wiki]'
aliases:
- base:perspective [Codebase64 wiki]
- perspective.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/perspective.md
  sha256: 727d830898f716baacb4ab35fa54a92cbacc2715ab08fa39609c3c923fda9ee8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:perspective [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/perspective.md`
**SHA256**: `727d830898f716baacb4ab35fa54a92cbacc2715ab08fa39609c3c923fda9ee8`

## Summary



# base:perspective [Codebase64 wiki]

base:perspective

                ### Perspective

by Bitbreaker/Oxyron/Nuance

Best is to calculate the perspective during multiply with the rotation matrix. As soon as you get the value for Z, lookup a corresponding factor in a table and multply the results for X and Y with that factor:

```
        ... matrix multipplication for Z ...
        tay
        lda z_fact,y
        sta z1
        eor #$ff
        sta z2
        
        ... matrix multiplicati...
