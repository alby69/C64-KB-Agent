---
id: src-f875-tape-readwrite
type: source
title: 'Source Summary: tape read/write'
aliases:
- tape read/write
- f875-tape-readwrite.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f875-tape-readwrite.md
  sha256: 9ba4f35f89831d430ed9b01c758560733f9326bd90b91f18aa5d92d3f1af4d95
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: tape read/write

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f875-tape-readwrite.md`
**SHA256**: `9ba4f35f89831d430ed9b01c758560733f9326bd90b91f18aa5d92d3f1af4d95`

## Summary



# $F875 — tape read/write

## Disassemblatura
```assembly
.F875  A0 7F    LDY #$7F   ; disable all interrupts
.F877  8C 0D DC STY $DC0D   ; save VIA 1 ICR, disable all interrupts
.F87A  8D 0D DC STA $DC0D   ; save VIA 1 ICR, enable interrupts according to A check RS232 bus idle
.F87D  AD 0E DC LDA $DC0E   ; read VIA 1 CRA
.F880  09 19    ORA #$19   ; load timer B, timer B single shot, start timer B
.F882  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.F885  29 91    AND #$91   ; mask x00x 000x, TOD cl...
