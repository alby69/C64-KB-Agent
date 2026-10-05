---
id: src-f0a4-check-rs232-bus-idle
type: source
title: 'Source Summary: check RS232 bus idle'
aliases:
- check RS232 bus idle
- f0a4-check-rs232-bus-idle.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f0a4-check-rs232-bus-idle.md
  sha256: ec7b244c0e1a45fd900e7d5b8321f4a7a6f43a97c076ad1607f835c2c02cc8f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check RS232 bus idle

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f0a4-check-rs232-bus-idle.md`
**SHA256**: `ec7b244c0e1a45fd900e7d5b8321f4a7a6f43a97c076ad1607f835c2c02cc8f3`

## Summary



# $F0A4 — check RS232 bus idle

## Disassemblatura
```assembly
.F0A4  48       PHA   ; save A
.F0A5  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F0A8  F0 11    BEQ $F0BB   ; if no interrupts enabled just exit
.F0AA  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F0AD  29 03    AND #$03   ; mask 0000 00xx, the error bits
.F0AF  D0 F9    BNE $F0AA   ; if there are errors loop
.F0B1  A9 10    LDA #$10   ; disable FLAG interrupt
.F0B3  8D 0D DD STA $DD0D   ; save VIA...
