---
id: src-rant9
type: source
title: 'Source Summary: Frameskipping, interpolation and re-entrant IRQ code by Cadaver'
aliases:
- Frameskipping, interpolation and re-entrant IRQ code by Cadaver
- rant9.md
tags:
- sprite programming
- basic
- graphics
- assembly
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/rant9.md
  sha256: 06f92e82a4350cb26ec05410ba7ec84c764fc75a32dea9b171f3fa691dc77b7a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Frameskipping, interpolation and re-entrant IRQ code by Cadaver

**Raw Source File**: `data/docs/codebase_c64_org/base/rant9.md`
**SHA256**: `06f92e82a4350cb26ec05410ba7ec84c764fc75a32dea9b171f3fa691dc77b7a`

## Summary



# Frameskipping, interpolation and re-entrant IRQ code by Cadaver

### Table of Contents

# Frameskipping, interpolation and re-entrant IRQ code by Cadaver

(This rant is mirrored from [Cadaver's site](http://cadaver.homeftp.net/))

This is a theoretical rant about what you can possibly do when it seems you run out of rastertime and your program starts to slow down. Of course, the obvious solution is to optimize code or leave routines out entirely, but this is not about that…

# 0. Running out...
