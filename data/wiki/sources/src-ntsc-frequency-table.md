---
id: src-ntsc-frequency-table
type: source
title: 'Source Summary: NTSC A440 frequency table'
aliases:
- NTSC A440 frequency table
- ntsc_frequency_table.md
tags:
- sound generation
sources:
- path: data/docs/codebase_c64_org/base/ntsc_frequency_table.md
  sha256: e3cd30ad0a0f8acff8766d1ee28d4f7f881649438db717e70950e5408487fdc9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NTSC A440 frequency table

**Raw Source File**: `data/docs/codebase_c64_org/base/ntsc_frequency_table.md`
**SHA256**: `e3cd30ad0a0f8acff8766d1ee28d4f7f881649438db717e70950e5408487fdc9`

## Summary



# NTSC A440 frequency table

base:ntsc_frequency_table

                # NTSC A440 frequency table

Note: Strictly speaking, this table corresponds to A440 tuning on C64s with the 6567R8 VIC, used in most NTSC machines. It is slightly incorrect on C64s with the 6567R56A VIC (which has 262 lines with 64 cycles per line instead of 263 lines with 65 cycles per line), but for most purposes it is still a relatively good approximation of A440 tuning.

FreqTableNtscLo:
	        ;      C   C#  D   D#...
