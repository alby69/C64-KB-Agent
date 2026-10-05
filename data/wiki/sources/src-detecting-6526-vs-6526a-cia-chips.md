---
id: src-detecting-6526-vs-6526a-cia-chips
type: source
title: 'Source Summary: Detecting 6526 vs 6526A CIA Chips'
aliases:
- Detecting 6526 vs 6526A CIA Chips
- detecting_6526_vs_6526a_cia_chips.md
tags:
- sprite programming
- basic
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/detecting_6526_vs_6526a_cia_chips.md
  sha256: 3156fcda88e0636464bb4fb745c0af7e348edb78b46f305eedaa69e11ee68083
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Detecting 6526 vs 6526A CIA Chips

**Raw Source File**: `data/docs/codebase_c64_org/base/detecting_6526_vs_6526a_cia_chips.md`
**SHA256**: `3156fcda88e0636464bb4fb745c0af7e348edb78b46f305eedaa69e11ee68083`

## Summary



# Detecting 6526 vs 6526A CIA Chips

# Detecting 6526 vs 6526A CIA Chips

by White Flame

This sets off a single-shot NMI to interrupt immediately before an INC statement. The older 6526 triggers one cycle later, so it will run the INC while the newer one won't.

Make sure the screen & sprites are off first.

oldCia should be in zeropage, and will have a 0 or 1 after this routine.

testCIAVersion:
 ; Set NMI vector
 lda #<continue
 sta $fffa
 lda #>continue
 sta $fffb
 lda #$81  ;also don't fo...
