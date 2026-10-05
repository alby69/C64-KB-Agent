---
id: src-a-new-kind-of-hard-restart
type: source
title: 'Source Summary: A new kind of hard-restart'
aliases:
- A new kind of hard-restart
- a_new_kind_of_hard-restart.md
tags:
- raster interrupts
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/a_new_kind_of_hard-restart.md
  sha256: 4f3ef82d1a82e20cac6b5758f78252af917010a596dc0eff348cf708d90e803c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: A new kind of hard-restart

**Raw Source File**: `data/docs/codebase_c64_org/base/a_new_kind_of_hard-restart.md`
**SHA256**: `4f3ef82d1a82e20cac6b5758f78252af917010a596dc0eff348cf708d90e803c`

## Summary



# A new kind of hard-restart

# A new kind of hard-restart

By shrydar, with contributions from lft.

This article explains how to perform a stable hard-restart; i.e. it not only zeros the envelope and captures the envelope rate counter, but it sets RC to a known value.

Back in 2011 I wanted to get the SID envelope generator into a known state to the cycle level, so I could then take some measurements of envelope behaviour. At the time, the best routine I could manage took well over three fra...
