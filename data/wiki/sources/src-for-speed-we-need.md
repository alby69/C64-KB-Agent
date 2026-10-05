---
id: src-for-speed-we-need
type: source
title: 'Source Summary: base:for_speed_we_need [Codebase64 wiki]'
aliases:
- base:for_speed_we_need [Codebase64 wiki]
- for_speed_we_need.md
tags:
- sprite programming
- input handling
- graphics
- assembly
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/for_speed_we_need.md
  sha256: c01722e347cc7144cafbadbe4b9e757eb97d05314d95be510e46246d9181a9a0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:for_speed_we_need [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/for_speed_we_need.md`
**SHA256**: `c01722e347cc7144cafbadbe4b9e757eb97d05314d95be510e46246d9181a9a0`

## Summary




# base:for_speed_we_need [Codebase64 wiki]

base:for_speed_we_need

                ## For Speed We Need

All code is Turbo Assembler, but it should also work in TASS (Crossplatform turbo assembler). You will need to draw some car sprites, background, get some music etc and then enter the following code (Or just rip the stuff from FSWN V1 on the TND web site or CSDB).

Music at $1000-$1fff ,Charset at $2000-$2800 ,Sprites at $2800-$3000 ,Screen map is at $4000-$5000

```
;--------------------...
