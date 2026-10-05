---
id: src-register-selection-for-load-and-store
type: source
title: 'Source Summary: Register selection for load and store'
aliases:
- Register selection for load and store
- register_selection_for_load_and_store.md
tags:
- general
sources:
- path: data/docs/codebase_c64_org/base/register_selection_for_load_and_store.md
  sha256: 8661562732528b9c79aea4abf8b2ac71cb097af4ac21815ae26f37579eab775e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Register selection for load and store

**Raw Source File**: `data/docs/codebase_c64_org/base/register_selection_for_load_and_store.md`
**SHA256**: `8661562732528b9c79aea4abf8b2ac71cb097af4ac21815ae26f37579eab775e`

## Summary



# Register selection for load and store

base:register_selection_for_load_and_store

                # Register selection for load and store

```
   bit1 bit0     A  X  Y
    0    0             x
    0    1          x
    1    0       x
    1    1       x  x
So, A and X are selected by bits 1 and 0 respectively, while
 ~(bit1|bit0) enables Y.
Indexing is determined by bit4, even in relative addressing mode,
which is one kind of indexing.
Lines containing opcodes xxx000x1 (01 and 03) are treate...
