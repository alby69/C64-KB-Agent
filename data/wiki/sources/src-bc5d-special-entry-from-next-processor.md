---
id: src-bc5d-special-entry-from-next-processor
type: source
title: 'Source Summary: SPECIAL ENTRY FROM "NEXT" PROCESSOR'
aliases:
- SPECIAL ENTRY FROM "NEXT" PROCESSOR
- bc5d-special-entry-from-next-processor.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc5d-special-entry-from-next-processor.md
  sha256: bee38f1730c86172693e2222e8fc800e6697916d371df78fe9aa6cf9ec192aa7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SPECIAL ENTRY FROM "NEXT" PROCESSOR

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc5d-special-entry-from-next-processor.md`
**SHA256**: `bee38f1730c86172693e2222e8fc800e6697916d371df78fe9aa6cf9ec192aa7`

## Summary



# $BC5D — SPECIAL ENTRY FROM "NEXT" PROCESSOR

## Disassemblatura
```assembly
.BC5D  84 25    STY $25
.BC5F  A0 00    LDY #$00   ; GET EXPONENT OF COMPARAND
.BC61  B1 24    LDA ($24),Y
.BC63  C8       INY   ; POINT AT NEXT BYTE
.BC64  AA       TAX   ; EXPONENT TO X-REG
.BC65  F0 C4    BEQ $BC2B   ; IF COMPARAND=0, "SIGN" COMPARES FAC
.BC67  B1 24    LDA ($24),Y   ; GET HI-BYTE OF MANTISSA
.BC69  45 66    EOR $66   ; COMPARE WITH FAC SIGN
.BC6B  30 C2    BMI $BC2F   ; DIFFERENT SIGNS, "SIGN" GI...
