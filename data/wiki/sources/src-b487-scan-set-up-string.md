---
id: src-b487-scan-set-up-string
type: source
title: 'Source Summary: scan, set up string'
aliases:
- scan, set up string
- b487-scan-set-up-string.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b487-scan-set-up-string.md
  sha256: b49bc30822a7cb1b13f642ef792c4b2ba9bb4a99a159c96ff6f4c0025b731391
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan, set up string

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b487-scan-set-up-string.md`
**SHA256**: `b49bc30822a7cb1b13f642ef792c4b2ba9bb4a99a159c96ff6f4c0025b731391`

## Summary



# $B487 — scan, set up string

## Disassemblatura
```assembly
.B487  A2 22    LDX #$22   ; set terminator to "
.B489  86 07    STX $07   ; set search character, terminator 1
.B48B  86 08    STX $08   ; set terminator 2 print search or alternate terminated string to utility pointer source is AY
.B48D  85 6F    STA $6F   ; store string start low byte
.B48F  84 70    STY $70   ; store string start high byte
.B491  85 62    STA $62   ; save string pointer low byte
.B493  84 63    STY $63   ; save ...
