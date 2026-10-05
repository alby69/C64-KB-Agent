---
id: src-ee8e-set-the-serial-clock-out-low
type: source
title: 'Source Summary: set the serial clock out low'
aliases:
- set the serial clock out low
- ee8e-set-the-serial-clock-out-low.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ee8e-set-the-serial-clock-out-low.md
  sha256: 06bb563caf58c988798364b01458bb7f83b64c1961788f8b2b1911875573d34f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the serial clock out low

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ee8e-set-the-serial-clock-out-low.md`
**SHA256**: `06bb563caf58c988798364b01458bb7f83b64c1961788f8b2b1911875573d34f`

## Summary



# $EE8E — set the serial clock out low

## Disassemblatura
```assembly
.EE8E  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE91  09 10    ORA #$10   ; mask xxx1 xxxx, set serial clock out low
.EE93  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE96  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE8E**: read VIA 2 DRA, serial port and video address
- **$EE91**: mask xxx1 xxxx, set serial clock out low
- **$EE93**: save VIA 2 ...
