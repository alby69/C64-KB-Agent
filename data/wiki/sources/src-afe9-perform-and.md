---
id: src-afe9-perform-and
type: source
title: 'Source Summary: perform AND'
aliases:
- perform AND
- afe9-perform-and.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/afe9-perform-and.md
  sha256: 1984ad4f91bbbaeb69410dfce8ef7f9447d78146c18df58282be8e579506101f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform AND

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/afe9-perform-and.md`
**SHA256**: `1984ad4f91bbbaeb69410dfce8ef7f9447d78146c18df58282be8e579506101f`

## Summary



# $AFE9 — perform AND

## Disassemblatura
```assembly
.AFE9  A0 00    LDY #$00   ; clear Y for AND
.AFEB  84 0B    STY $0B   ; set AND/OR invert value
.AFED  20 BF B1 JSR $B1BF   ; evaluate integer expression, no sign check
.AFF0  A5 64    LDA $64   ; get FAC1 mantissa 3
.AFF2  45 0B    EOR $0B   ; EOR low byte
.AFF4  85 07    STA $07   ; save it
.AFF6  A5 65    LDA $65   ; get FAC1 mantissa 4
.AFF8  45 0B    EOR $0B   ; EOR high byte
.AFFA  85 08    STA $08   ; save it
.AFFC  20 FC BB JSR $BB...
