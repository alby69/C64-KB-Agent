---
id: src-nmi-lock
type: source
title: 'Source Summary: NMI lock'
aliases:
- NMI lock
- nmi_lock.md
tags:
- raster interrupts
- assembly
- graphics
- input handling
sources:
- path: data/docs/codebase_c64_org/base/nmi_lock.md
  sha256: 3f27478cbca31b804a88d4316100e51697a1823dc4521453c5c865ed9a2d3b01
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NMI lock

**Raw Source File**: `data/docs/codebase_c64_org/base/nmi_lock.md`
**SHA256**: `3f27478cbca31b804a88d4316100e51697a1823dc4521453c5c865ed9a2d3b01`

## Summary




# NMI lock

### Table of Contents

# NMI lock

From Go64!/CW-issue 09/1999

By Wolfram Sang (Ninja/The Dreams - [www.the-dreams.de](http://www.the-dreams.de))
Final section added by Frantic/HT after some confused discussions on the CSDb forum.

Don't rely on names!

NMI is short for “Non-Maskable Interrupt” what means, you can't disable it. But as we talk about C64, there is of course a way to do so.

Some demo-effects or transmission routines have a very critical timing. Hit RESTORE once and...
