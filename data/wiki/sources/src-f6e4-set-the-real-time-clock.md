---
id: src-f6e4-set-the-real-time-clock
type: source
title: 'Source Summary: set the real time clock'
aliases:
- set the real time clock
- f6e4-set-the-real-time-clock.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f6e4-set-the-real-time-clock.md
  sha256: 39483f0c93fc7be3fa98b5fb63e2c46c953fa777bd09350d5469d19729ea377e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the real time clock

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f6e4-set-the-real-time-clock.md`
**SHA256**: `39483f0c93fc7be3fa98b5fb63e2c46c953fa777bd09350d5469d19729ea377e`

## Summary



# $F6E4 — set the real time clock

## Disassemblatura
```assembly
.F6E4  78       SEI   ; disable the interrupts
.F6E5  85 A2    STA $A2   ; save the jiffy clock low byte
.F6E7  86 A1    STX $A1   ; save the jiffy clock mid byte
.F6E9  84 A0    STY $A0   ; save the jiffy clock high byte
.F6EB  58       CLI   ; enable the interrupts
.F6EC  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F6E4**: disable the interrupts
- **$F6E5**: save the jiffy clock low byte
- **$F6E7**: save...
