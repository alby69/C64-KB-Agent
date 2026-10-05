---
id: src-e8ea-scroll-the-screen
type: source
title: 'Source Summary: scroll the screen'
aliases:
- scroll the screen
- e8ea-scroll-the-screen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e8ea-scroll-the-screen.md
  sha256: 5cc0449ee737e5087b98077ab8aa4379e95e08cac266221b1c9302bc603efb9f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scroll the screen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e8ea-scroll-the-screen.md`
**SHA256**: `5cc0449ee737e5087b98077ab8aa4379e95e08cac266221b1c9302bc603efb9f`

## Summary



# $E8EA — scroll the screen

## Disassemblatura
```assembly
.E8EA  A5 AC    LDA $AC   ; copy the tape buffer start pointer
.E8EC  48       PHA   ; save it
.E8ED  A5 AD    LDA $AD   ; copy the tape buffer start pointer
.E8EF  48       PHA   ; save it
.E8F0  A5 AE    LDA $AE   ; copy the tape buffer end pointer
.E8F2  48       PHA   ; save it
.E8F3  A5 AF    LDA $AF   ; copy the tape buffer end pointer
.E8F5  48       PHA   ; save it
.E8F6  A2 FF    LDX #$FF   ; set to -1 for pre increment loop
...
