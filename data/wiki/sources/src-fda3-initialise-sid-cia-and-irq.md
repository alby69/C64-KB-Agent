---
id: src-fda3-initialise-sid-cia-and-irq
type: source
title: 'Source Summary: initialise SID, CIA and IRQ'
aliases:
- initialise SID, CIA and IRQ
- fda3-initialise-sid-cia-and-irq.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fda3-initialise-sid-cia-and-irq.md
  sha256: 3de86934e8618cdac1914becd395c6ad62f7be1ecf995999b4557174711f6134
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise SID, CIA and IRQ

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fda3-initialise-sid-cia-and-irq.md`
**SHA256**: `3de86934e8618cdac1914becd395c6ad62f7be1ecf995999b4557174711f6134`

## Summary



# $FDA3 — initialise SID, CIA and IRQ

## Disassemblatura
```assembly
.FDA3  A9 7F    LDA #$7F   ; disable all interrupts
.FDA5  8D 0D DC STA $DC0D   ; save VIA 1 ICR
.FDA8  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.FDAB  8D 00 DC STA $DC00   ; save VIA 1 DRA, keyboard column drive
.FDAE  A9 08    LDA #$08   ; set timer single shot
.FDB0  8D 0E DC STA $DC0E   ; save VIA 1 CRA
.FDB3  8D 0E DD STA $DD0E   ; save VIA 2 CRA
.FDB6  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.FDB9  8D 0F DD STA $DD0F   ; sa...
