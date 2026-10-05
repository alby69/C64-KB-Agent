---
id: src-f12b-display-control-io-message-if-in-direct-mode
type: source
title: 'Source Summary: display control I/O message if in direct mode'
aliases:
- display control I/O message if in direct mode
- f12b-display-control-io-message-if-in-direct-mode.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f12b-display-control-io-message-if-in-direct-mode.md
  sha256: dd63f1641ecda87e341d94e98b9b9fef6604189c66d207da1eb21d165ec791f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: display control I/O message if in direct mode

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f12b-display-control-io-message-if-in-direct-mode.md`
**SHA256**: `dd63f1641ecda87e341d94e98b9b9fef6604189c66d207da1eb21d165ec791f3`

## Summary



# $F12B — display control I/O message if in direct mode

## Disassemblatura
```assembly
.F12B  24 9D    BIT $9D   ; test message mode flag
.F12D  10 0D    BPL $F13C   ; exit if control messages off display kernel I/O message
.F12F  B9 BD F0 LDA $F0BD,Y   ; get byte from message table
.F132  08       PHP   ; save status
.F133  29 7F    AND #$7F   ; clear b7
.F135  20 D2 FF JSR $FFD2   ; output character to channel
.F138  C8       INY   ; increment index
.F139  28       PLP   ; restore status
.F...
