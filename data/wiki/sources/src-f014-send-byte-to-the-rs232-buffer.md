---
id: src-f014-send-byte-to-the-rs232-buffer
type: source
title: 'Source Summary: send byte to the RS232 buffer'
aliases:
- send byte to the RS232 buffer
- f014-send-byte-to-the-rs232-buffer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f014-send-byte-to-the-rs232-buffer.md
  sha256: 33415c36bf11e8bb9af77b5f39c682641830a7d1b7292812644ede22507209db
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: send byte to the RS232 buffer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f014-send-byte-to-the-rs232-buffer.md`
**SHA256**: `33415c36bf11e8bb9af77b5f39c682641830a7d1b7292812644ede22507209db`

## Summary



# $F014 — send byte to the RS232 buffer

## Disassemblatura
```assembly
.F014  20 28 F0 JSR $F028   ; setup for RS232 transmit send byte to the RS232 buffer, no setup
.F017  AC 9E 02 LDY $029E   ; get index to Tx buffer end
.F01A  C8       INY   ; + 1
.F01B  CC 9D 02 CPY $029D   ; compare with index to Tx buffer start
.F01E  F0 F4    BEQ $F014   ; loop while buffer full
.F020  8C 9E 02 STY $029E   ; set index to Tx buffer end
.F023  88       DEY   ; index to available buffer byte
.F024  A5 9E ...
