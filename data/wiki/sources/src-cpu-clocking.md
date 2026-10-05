---
id: src-cpu-clocking
type: source
title: 'Source Summary: Clock Frequency'
aliases:
- Clock Frequency
- cpu_clocking.md
tags:
- sound generation
- assembly
sources:
- path: data/docs/codebase_c64_org/base/cpu_clocking.md
  sha256: c4bda70f07d373515389fc6e65f2e9676db51ab55c48efe82ae7810670792fa6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Clock Frequency

**Raw Source File**: `data/docs/codebase_c64_org/base/cpu_clocking.md`
**SHA256**: `c4bda70f07d373515389fc6e65f2e9676db51ab55c48efe82ae7810670792fa6`

## Summary



# Clock Frequency

# Clock Frequency

All clock frequencies in the C64 are derived from a single clock quartz which has the frequency of 4 times the frequency of the color carrier used for PAL or NTSC.

PAL C64 master clock: 17.734475 MHz

NTSC C64 master clock: 14.31818 MHz

The CPU frequency is then calculated from that by simply dividing the frequency by 18 (PAL) or 14 (NTSC). The VIC-II runs at a frequency which is exactly 8 times that of the CPU. This is the so called “dot clock” which ha...
