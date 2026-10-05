---
id: src-ee97-set-the-serial-data-out-high
type: source
title: 'Source Summary: set the serial data out high'
aliases:
- set the serial data out high
- ee97-set-the-serial-data-out-high.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ee97-set-the-serial-data-out-high.md
  sha256: f902f40494f9d04b33744eb4aa30866441a4f3021d1df6eb62abad8408a3c2cc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the serial data out high

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ee97-set-the-serial-data-out-high.md`
**SHA256**: `f902f40494f9d04b33744eb4aa30866441a4f3021d1df6eb62abad8408a3c2cc`

## Summary



# $EE97 — set the serial data out high

## Disassemblatura
```assembly
.EE97  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE9A  29 DF    AND #$DF   ; mask xx0x xxxx, set serial data out high
.EE9C  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE9F  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE97**: read VIA 2 DRA, serial port and video address
- **$EE9A**: mask xx0x xxxx, set serial data out high
- **$EE9C**: save VIA 2 ...
