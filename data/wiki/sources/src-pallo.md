---
id: src-pallo
type: source
title: 'Source Summary: base:pallo [Codebase64 wiki]'
aliases:
- base:pallo [Codebase64 wiki]
- pallo.md
tags:
- sprite programming
- input handling
- basic
- graphics
- assembly
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/pallo.md
  sha256: e7cb94a8de00af2e30c17c5adc9cca31712cd1f30e807454ffb83f3dec578961
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:pallo [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/pallo.md`
**SHA256**: `e7cb94a8de00af2e30c17c5adc9cca31712cd1f30e807454ffb83f3dec578961`

## Summary




# base:pallo [Codebase64 wiki]

base:pallo

                ```
; Pallo
; -----
; 2006 Hannu Nuotio
; Pallo is a remake of the crap QBasic game of the same name (and author).
; Start of project: 26.8.2006
; v.1.1 - 20.10.2006 - added joyport constants
; v.1.0 - 16.9.2006 - seems to work
; Compiles with ACME 0.91
; # acme --cpu 6502 -f cbm -o pallo.prg pallo.a
; Type SYS 4096 to start or use crunched version.
; Known bugs:
;  - If warning collides with pallo and food, pallo does not get food.
...
