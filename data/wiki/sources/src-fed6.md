---
id: src-fed6
type: source
title: 'Source Summary: ??'
aliases:
- ??
- fed6.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fed6.md
  sha256: 310d6edd2d66f48c1941dada04aae27a5446aa0342c288d57290ea443b31fbd2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ??

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fed6.md`
**SHA256**: `310d6edd2d66f48c1941dada04aae27a5446aa0342c288d57290ea443b31fbd2`

## Summary



# $FED6 — ??

## Disassemblatura
```assembly
.FED6  AD 01 DD LDA $DD01   ; read VIA 2 DRB, RS232 port
.FED9  29 01    AND #$01   ; mask 0000 000x, RS232 Rx DATA
.FEDB  85 A7    STA $A7   ; save the RS232 received data bit
.FEDD  AD 06 DD LDA $DD06   ; get VIA 2 timer B low byte
.FEE0  E9 1C    SBC #$1C
.FEE2  6D 99 02 ADC $0299
.FEE5  8D 06 DD STA $DD06   ; save VIA 2 timer B low byte
.FEE8  AD 07 DD LDA $DD07   ; get VIA 2 timer B high byte
.FEEB  6D 9A 02 ADC $029A
.FEEE  8D 07 DD STA $DD07 ...
