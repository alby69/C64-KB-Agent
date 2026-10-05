---
id: src-pal-frequency-table
type: source
title: 'Source Summary: PAL A440 frequency table'
aliases:
- PAL A440 frequency table
- pal_frequency_table.md
tags:
- sound generation
sources:
- path: data/docs/codebase_c64_org/base/pal_frequency_table.md
  sha256: a45b933f7619643949997fa6b7343dad3d6af359b3208e86b9cfad4b8854ec44
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PAL A440 frequency table

**Raw Source File**: `data/docs/codebase_c64_org/base/pal_frequency_table.md`
**SHA256**: `a45b933f7619643949997fa6b7343dad3d6af359b3208e86b9cfad4b8854ec44`

## Summary



# PAL A440 frequency table

base:pal_frequency_table

                # PAL A440 frequency table

Note: This table does not correspond to A440 tuning on the PAL-N “Drean” C64 models, which have a slightly faster clock.

```
FreqTablePalLo:
	        ;      C   C#  D   D#  E   F   F#  G   G#  A   A#  B
                .byte $16,$27,$39,$4b,$5f,$74,$8a,$a1,$ba,$d4,$f0,$0e  ; 0
                .byte $2d,$4e,$71,$96,$be,$e7,$14,$42,$74,$a9,$e0,$1b  ; 1
                .byte $5a,$9c,$e2,$2d,$7b,$cf,...
