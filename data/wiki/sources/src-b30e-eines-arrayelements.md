---
id: src-b30e-eines-arrayelements
type: source
title: 'Source Summary: eines Arrayelements'
aliases:
- eines Arrayelements
- b30e-eines-arrayelements.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b30e-eines-arrayelements.md
  sha256: 0c331813937ba3d23237472901c0cd9176897ebfe1e5138c0cf7a00e9a860a24
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: eines Arrayelements

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b30e-eines-arrayelements.md`
**SHA256**: `0c331813937ba3d23237472901c0cd9176897ebfe1e5138c0cf7a00e9a860a24`

## Summary



# $B30E — eines Arrayelements

## Disassemblatura
```assembly
.B30E  C8       INY   ; Zeiger erhöhen
.B30F  A5 72    LDA $72   ; Zeiger auf Polynomausw.(HIGH)
.B311  05 71    ORA $71   ; Zeiger auf Polynomausw.(LOW)
.B313  18       CLC   ; Carry löschen
.B314  F0 0A    BEQ $B320   ; Multiplikation umgehen
.B316  20 4C B3 JSR $B34C   ; Multiplikation
.B319  8A       TXA   ; (X/Y)=($71/72)*(($5F/60),Y)
.B31A  65 64    ADC $64
.B31C  AA       TAX   ; Akku zurück ins X-Reg.
.B31D  98       TYA
.B3...
