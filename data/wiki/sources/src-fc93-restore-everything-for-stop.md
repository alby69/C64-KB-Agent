---
id: src-fc93-restore-everything-for-stop
type: source
title: 'Source Summary: restore everything for STOP'
aliases:
- restore everything for STOP
- fc93-restore-everything-for-stop.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fc93-restore-everything-for-stop.md
  sha256: 68c00e90f0685bfe13b30414e5111edc1154ce101f8e8a892cf7e6f8df036ac6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: restore everything for STOP

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fc93-restore-everything-for-stop.md`
**SHA256**: `68c00e90f0685bfe13b30414e5111edc1154ce101f8e8a892cf7e6f8df036ac6`

## Summary



# $FC93 — restore everything for STOP

## Disassemblatura
```assembly
.FC93  08       PHP   ; save status
.FC94  78       SEI   ; disable the interrupts
.FC95  AD 11 D0 LDA $D011   ; read the vertical fine scroll and control register
.FC98  09 10    ORA #$10   ; mask xxx1 xxxx, unblank the screen
.FC9A  8D 11 D0 STA $D011   ; save the vertical fine scroll and control register
.FC9D  20 CA FC JSR $FCCA   ; stop the cassette motor
.FCA0  A9 7F    LDA #$7F   ; disable all interrupts
.FCA2  8D 0D ...
