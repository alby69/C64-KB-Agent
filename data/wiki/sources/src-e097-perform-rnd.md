---
id: src-e097-perform-rnd
type: source
title: 'Source Summary: perform RND()'
aliases:
- perform RND()
- e097-perform-rnd.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e097-perform-rnd.md
  sha256: 5b632ff4f45f9e4d69a63d77d2e7d196ffc4f38858282fda797a3c7e964f6a79
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform RND()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e097-perform-rnd.md`
**SHA256**: `5b632ff4f45f9e4d69a63d77d2e7d196ffc4f38858282fda797a3c7e964f6a79`

## Summary



# $E097 — perform RND()

## Disassemblatura
```assembly
.E097  20 2B BC JSR $BC2B   ; get FAC1 sign return A = $FF -ve, A = $01 +ve
.E09A  30 37    BMI $E0D3   ; if n<0 copy byte swapped FAC1 into RND() seed
.E09C  D0 20    BNE $E0BE   ; if n>0 get next number in RND() sequence else n=0 so get the RND() number from VIA 1 timers
.E09E  20 F3 FF JSR $FFF3   ; return base address of I/O devices
.E0A1  86 22    STX $22   ; save pointer low byte
.E0A3  84 23    STY $23   ; save pointer high byte
.E...
