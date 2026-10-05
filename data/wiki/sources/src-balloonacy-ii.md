---
id: src-balloonacy-ii
type: source
title: 'Source Summary: base:balloonacy_ii [Codebase64 wiki]'
aliases:
- base:balloonacy_ii [Codebase64 wiki]
- balloonacy_ii.md
tags:
- sprite programming
- input handling
- graphics
- assembly
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/balloonacy_ii.md
  sha256: 23e02d115158f914cb010dcd7810ce890dcbc56c44806975f03469a2132d3d50
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:balloonacy_ii [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/balloonacy_ii.md`
**SHA256**: `23e02d115158f914cb010dcd7810ce890dcbc56c44806975f03469a2132d3d50`

## Summary




# base:balloonacy_ii [Codebase64 wiki]

base:balloonacy_ii

                Here is the whole source code to the game Balloonacy 2. Please note, you will need to extract the source objects from the original game. :)

```
===================================================
;			ballonacy 2 - by tnd projects
;the gamecode
;===================================================
;declare variables
sync = $02			;Synchronize the area
charpointer = $03	;The timer for the animation
delaypointer = $04	;De...
