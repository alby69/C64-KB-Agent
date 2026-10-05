---
id: src-e4d3-flag-the-rs232-start-bit-and-set-the-parity
type: source
title: 'Source Summary: flag the RS232 start bit and set the parity'
aliases:
- flag the RS232 start bit and set the parity
- e4d3-flag-the-rs232-start-bit-and-set-the-parity.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4d3-flag-the-rs232-start-bit-and-set-the-parity.md
  sha256: b6a641af765d6f422edeada4fda3b2fb19be3b703ea7368e97e5251ba7d1c3f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: flag the RS232 start bit and set the parity

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e4d3-flag-the-rs232-start-bit-and-set-the-parity.md`
**SHA256**: `b6a641af765d6f422edeada4fda3b2fb19be3b703ea7368e97e5251ba7d1c3f3`

## Summary



# $E4D3 — flag the RS232 start bit and set the parity

## Disassemblatura
```assembly
.E4D3  85 A9    STA $A9   ; save the start bit check flag, set start bit received
.E4D5  A9 01    LDA #$01   ; set the initial parity state
.E4D7  85 AB    STA $AB   ; save the receiver parity bit
.E4D9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E4D3**: save the start bit check flag, set start bit received
- **$E4D5**: set the initial parity state
- **$E4D7**: save the receiver parity ...
