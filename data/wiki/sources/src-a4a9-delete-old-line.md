---
id: src-a4a9-delete-old-line
type: source
title: 'Source Summary: delete old line'
aliases:
- delete old line
- a4a9-delete-old-line.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a4a9-delete-old-line.md
  sha256: cc8ecb7a93de15ebb7596c98402dab57bbd1b8408072939a420d25fb9a3c48a1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: delete old line

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a4a9-delete-old-line.md`
**SHA256**: `cc8ecb7a93de15ebb7596c98402dab57bbd1b8408072939a420d25fb9a3c48a1`

## Summary



# $A4A9 — delete old line

## Disassemblatura
```assembly
.A4A9  A0 01    LDY #$01
.A4AB  B1 5F    LDA ($5F),Y
.A4AD  85 23    STA $23
.A4AF  A5 2D    LDA $2D
.A4B1  85 22    STA $22
.A4B3  A5 60    LDA $60
.A4B5  85 25    STA $25
.A4B7  A5 5F    LDA $5F
.A4B9  88       DEY
.A4BA  F1 5F    SBC ($5F),Y
.A4BC  18       CLC
.A4BD  65 2D    ADC $2D
.A4BF  85 2D    STA $2D
.A4C1  85 24    STA $24
.A4C3  A5 2E    LDA $2E
.A4C5  69 FF    ADC #$FF
.A4C7  85 2E    STA $2E
.A4C9  E5 60    SBC $60
.A4CB ...
