---
id: e4d3-flag-the-rs232-start-bit-and-set-the-parity
type: entity
title: flag the RS232 start bit and set the parity
aliases:
- flag the RS232 start bit and set the parity
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4d3-flag-the-rs232-start-bit-and-set-the-parity.md
  sha256: b6a641af765d6f422edeada4fda3b2fb19be3b703ea7368e97e5251ba7d1c3f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e4d3-flag-the-rs232-start-bit-and-set-the-parity
---

# flag the RS232 start bit and set the parity



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
- **$E4D7**: save the receiver parity bit

### Magnus Nyman (Magnus Nyman)
- **$E4D3**: RINONE, check for start bit
- **$E4D7**: RIPRTY, RS232 input parity

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e4d3-flag-the-rs232-start-bit-and-set-the-parity]]
