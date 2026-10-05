---
id: src-eea0-set-the-serial-data-out-low
type: source
title: 'Source Summary: set the serial data out low'
aliases:
- set the serial data out low
- eea0-set-the-serial-data-out-low.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eea0-set-the-serial-data-out-low.md
  sha256: 42c06ea0aa2a2964133493bd53098e3d130672289896a7f66413a25aa7525324
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the serial data out low

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eea0-set-the-serial-data-out-low.md`
**SHA256**: `42c06ea0aa2a2964133493bd53098e3d130672289896a7f66413a25aa7525324`

## Summary



# $EEA0 — set the serial data out low

## Disassemblatura
```assembly
.EEA0  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EEA3  09 20    ORA #$20   ; mask xx1x xxxx, set serial data out low
.EEA5  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EEA8  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEA0**: read VIA 2 DRA, serial port and video address
- **$EEA3**: mask xx1x xxxx, set serial data out low
- **$EEA5**: save VIA 2 DRA...
