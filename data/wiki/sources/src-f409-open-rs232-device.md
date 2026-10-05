---
id: src-f409-open-rs232-device
type: source
title: 'Source Summary: open RS232 device'
aliases:
- open RS232 device
- f409-open-rs232-device.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f409-open-rs232-device.md
  sha256: e294c2604ff56b76dda185bf6f4f9a8b42da610a4be9a4e084012e8ca51187fb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open RS232 device

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f409-open-rs232-device.md`
**SHA256**: `e294c2604ff56b76dda185bf6f4f9a8b42da610a4be9a4e084012e8ca51187fb`

## Summary



# $F409 — open RS232 device

## Disassemblatura
```assembly
.F409  20 83 F4 JSR $F483   ; initialise RS232 output
.F40C  8C 97 02 STY $0297   ; save the RS232 status register
.F40F  C4 B7    CPY $B7   ; compare with file name length
.F411  F0 0A    BEQ $F41D   ; exit loop if done
.F413  B1 BB    LDA ($BB),Y   ; get file name byte
.F415  99 93 02 STA $0293,Y   ; copy to 6551 register set
.F418  C8       INY   ; increment index
.F419  C0 04    CPY #$04   ; compare with $04
.F41B  D0 F2    BNE $F...
