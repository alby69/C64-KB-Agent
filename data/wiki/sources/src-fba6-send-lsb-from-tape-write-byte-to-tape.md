---
id: src-fba6-send-lsb-from-tape-write-byte-to-tape
type: source
title: 'Source Summary: send lsb from tape write byte to tape'
aliases:
- send lsb from tape write byte to tape
- fba6-send-lsb-from-tape-write-byte-to-tape.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fba6-send-lsb-from-tape-write-byte-to-tape.md
  sha256: e5cbf17f97d8bbb33ddf494e10e737788685ea819186d79a322c75cb215d9e0f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: send lsb from tape write byte to tape

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fba6-send-lsb-from-tape-write-byte-to-tape.md`
**SHA256**: `e5cbf17f97d8bbb33ddf494e10e737788685ea819186d79a322c75cb215d9e0f`

## Summary



# $FBA6 — send lsb from tape write byte to tape

## Disassemblatura
```assembly
.FBA6  A5 BD    LDA $BD   ; get tape write byte
.FBA8  4A       LSR   ; shift lsb into Cb
.FBA9  A9 60    LDA #$60   ; set time constant low byte for bit = 0
.FBAB  90 02    BCC $FBAF   ; branch if bit was 0 set time constant for bit = 1 and toggle tape
.FBAD  A9 B0    LDA #$B0   ; set time constant low byte for bit = 1 write time constant and toggle tape
.FBAF  A2 00    LDX #$00   ; set time constant high byte wri...
