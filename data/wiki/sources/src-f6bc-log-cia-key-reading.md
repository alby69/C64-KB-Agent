---
id: src-f6bc-log-cia-key-reading
type: source
title: 'Source Summary: LOG CIA KEY READING'
aliases:
- LOG CIA KEY READING
- f6bc-log-cia-key-reading.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f6bc-log-cia-key-reading.md
  sha256: a1c68d3f1c7decedbd58338001b0c6b244a2b9756761e4247f0a140cdce6e297
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LOG CIA KEY READING

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f6bc-log-cia-key-reading.md`
**SHA256**: `a1c68d3f1c7decedbd58338001b0c6b244a2b9756761e4247f0a140cdce6e297`

## Summary



# $F6BC — LOG CIA KEY READING

## Disassemblatura
```assembly
.F6BC  AD 01 DC LDA $DC01   ; keyboard read register
.F6BF  CD 01 DC CMP $DC01
.F6C2  D0 F8    BNE $F6BC   ; wait for value to settle
.F6C4  AA       TAX
.F6C5  30 13    BMI $F6DA
.F6C7  A2 BD    LDX #$BD
.F6C9  8E 00 DC STX $DC00   ; keyboard write register
.F6CC  AE 01 DC LDX $DC01   ; keyboard read register
.F6CF  EC 01 DC CPX $DC01
.F6D2  D0 F8    BNE $F6CC   ; wait for value to settle
.F6D4  8D 00 DC STA $DC00
.F6D7  E8       I...
