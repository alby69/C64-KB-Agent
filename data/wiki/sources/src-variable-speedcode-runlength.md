---
id: src-variable-speedcode-runlength
type: source
title: 'Source Summary: Variable speedcode runlength'
aliases:
- Variable speedcode runlength
- variable_speedcode_runlength.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/variable_speedcode_runlength.md
  sha256: 9b7da3ab83284c1d8d39ce8c73ad98de4dce24bd567367e5c2e31c21cfd9ec66
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Variable speedcode runlength

**Raw Source File**: `data/docs/codebase_c64_org/base/variable_speedcode_runlength.md`
**SHA256**: `9b7da3ab83284c1d8d39ce8c73ad98de4dce24bd567367e5c2e31c21cfd9ec66`

## Summary



# Variable speedcode runlength

# Variable speedcode runlength

After you entered a segment of speed code at a certain spot by making use of some method discussed in the Article “[Dispatch on a byte](https://codebase.c64.org/doku.php?id=base:dispatch_on_a_byte)” we now want to exit that code at a certain spot.

Some code can be written that way, that we can also determine the runlength by the point where we enter and let it run until its end. But if we have explicit target addresses in our spe...
