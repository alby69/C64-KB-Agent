---
id: src-eea9-get-the-serial-data-status-in-cb
type: source
title: 'Source Summary: get the serial data status in Cb'
aliases:
- get the serial data status in Cb
- eea9-get-the-serial-data-status-in-cb.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eea9-get-the-serial-data-status-in-cb.md
  sha256: e80f5e9a7a516a3d440b44dd7b41f8c9668d6f2529b9ab0b83c095940f14856c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get the serial data status in Cb

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eea9-get-the-serial-data-status-in-cb.md`
**SHA256**: `e80f5e9a7a516a3d440b44dd7b41f8c9668d6f2529b9ab0b83c095940f14856c`

## Summary



# $EEA9 — get the serial data status in Cb

## Disassemblatura
```assembly
.EEA9  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EEAC  CD 00 DD CMP $DD00   ; compare it with itself
.EEAF  D0 F8    BNE $EEA9   ; if changing got try again
.EEB1  0A       ASL   ; shift the serial data into Cb
.EEB2  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEA9**: read VIA 2 DRA, serial port and video address
- **$EEAC**: compare it with itself
- **$EEAF**: if chang...
