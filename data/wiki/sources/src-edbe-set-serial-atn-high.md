---
id: src-edbe-set-serial-atn-high
type: source
title: 'Source Summary: set serial ATN high'
aliases:
- set serial ATN high
- edbe-set-serial-atn-high.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edbe-set-serial-atn-high.md
  sha256: f65e35d89c15287f219630ddc9b94e814140c82270d804670a38be0a99122bfb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set serial ATN high

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/edbe-set-serial-atn-high.md`
**SHA256**: `f65e35d89c15287f219630ddc9b94e814140c82270d804670a38be0a99122bfb`

## Summary



# $EDBE — set serial ATN high

## Disassemblatura
```assembly
.EDBE  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EDC1  29 F7    AND #$F7   ; mask xxxx 0xxx, set serial ATN high
.EDC3  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EDC6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EDBE**: read VIA 2 DRA, serial port and video address
- **$EDC1**: mask xxxx 0xxx, set serial ATN high
- **$EDC3**: save VIA 2 DRA, serial port an...
