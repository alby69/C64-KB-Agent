---
id: src-a4ed-insert-new-line
type: source
title: 'Source Summary: insert new line'
aliases:
- insert new line
- a4ed-insert-new-line.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a4ed-insert-new-line.md
  sha256: 344c9fe224bae3bc382c74580b534c1e127fe86e94f8452cf127db247b9bd89c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: insert new line

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a4ed-insert-new-line.md`
**SHA256**: `344c9fe224bae3bc382c74580b534c1e127fe86e94f8452cf127db247b9bd89c`

## Summary



# $A4ED — insert new line

## Disassemblatura
```assembly
.A4ED  20 59 A6 JSR $A659
.A4F0  20 33 A5 JSR $A533
.A4F3  AD 00 02 LDA $0200
.A4F6  F0 88    BEQ $A480
.A4F8  18       CLC
.A4F9  A5 2D    LDA $2D
.A4FB  85 5A    STA $5A
.A4FD  65 0B    ADC $0B
.A4FF  85 58    STA $58
.A501  A4 2E    LDY $2E
.A503  84 5B    STY $5B
.A505  90 01    BCC $A508
.A507  C8       INY
.A508  84 59    STY $59
.A50A  20 B8 A3 JSR $A3B8
.A50D  A5 14    LDA $14
.A50F  A4 15    LDY $15
.A511  8D FE 01 STA $01FE
.A...
