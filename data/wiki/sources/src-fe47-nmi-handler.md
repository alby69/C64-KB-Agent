---
id: src-fe47-nmi-handler
type: source
title: 'Source Summary: NMI handler'
aliases:
- NMI handler
- fe47-nmi-handler.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe47-nmi-handler.md
  sha256: ea337855f03664a41374d207874615688f17f2fb1208264f750c335485b3c6ca
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NMI handler

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fe47-nmi-handler.md`
**SHA256**: `ea337855f03664a41374d207874615688f17f2fb1208264f750c335485b3c6ca`

## Summary



# $FE47 — NMI handler

## Disassemblatura
```assembly
.FE47  48       PHA   ; save A
.FE48  8A       TXA   ; copy X
.FE49  48       PHA   ; save X
.FE4A  98       TYA   ; copy Y
.FE4B  48       PHA   ; save Y
.FE4C  A9 7F    LDA #$7F   ; disable all interrupts
.FE4E  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.FE51  AC 0D DD LDY $DD0D   ; save VIA 2 ICR
.FE54  30 1C    BMI $FE72
.FE56  20 02 FD JSR $FD02   ; scan for autostart ROM at $8000
.FE59  D0 03    BNE $FE5E   ; branch if no autostart ROM
.F...
