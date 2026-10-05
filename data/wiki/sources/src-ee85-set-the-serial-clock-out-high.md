---
id: src-ee85-set-the-serial-clock-out-high
type: source
title: 'Source Summary: set the serial clock out high'
aliases:
- set the serial clock out high
- ee85-set-the-serial-clock-out-high.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ee85-set-the-serial-clock-out-high.md
  sha256: 1e84979838b0b0a3e605ad8f28cc5270297a28b691cedf3d08b7fde952b93c50
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the serial clock out high

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ee85-set-the-serial-clock-out-high.md`
**SHA256**: `1e84979838b0b0a3e605ad8f28cc5270297a28b691cedf3d08b7fde952b93c50`

## Summary



# $EE85 — set the serial clock out high

## Disassemblatura
```assembly
.EE85  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE88  29 EF    AND #$EF   ; mask xxx0 xxxx, set serial clock out high
.EE8A  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EE8D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE85**: read VIA 2 DRA, serial port and video address
- **$EE88**: mask xxx0 xxxx, set serial clock out high
- **$EE8A**: save VIA...
