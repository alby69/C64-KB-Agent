---
id: src-f8d0-scan-stop-key-and-flag-abort-if-pressed
type: source
title: 'Source Summary: scan stop key and flag abort if pressed'
aliases:
- scan stop key and flag abort if pressed
- f8d0-scan-stop-key-and-flag-abort-if-pressed.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f8d0-scan-stop-key-and-flag-abort-if-pressed.md
  sha256: bb352d8b5a991bd22a5e1a396efacae0e5d012d5dad84aa78f04fed3926f3fd4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan stop key and flag abort if pressed

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f8d0-scan-stop-key-and-flag-abort-if-pressed.md`
**SHA256**: `bb352d8b5a991bd22a5e1a396efacae0e5d012d5dad84aa78f04fed3926f3fd4`

## Summary



# $F8D0 — scan stop key and flag abort if pressed

## Disassemblatura
```assembly
.F8D0  20 E1 FF JSR $FFE1   ; scan stop key
.F8D3  18       CLC   ; flag no stop
.F8D4  D0 0B    BNE $F8E1   ; exit if no stop
.F8D6  20 93 FC JSR $FC93   ; restore everything for STOP
.F8D9  38       SEC   ; flag stopped
.F8DA  68       PLA   ; dump return address low byte
.F8DB  68       PLA   ; dump return address high byte
```


## Commenti

### Original Disassembly (—)
- **$F8D0**: scan stop key
- **$F8D3**:...
