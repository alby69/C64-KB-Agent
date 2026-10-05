---
id: src-fc6a-write-tape-leader-irq-routine
type: source
title: 'Source Summary: write tape leader IRQ routine'
aliases:
- write tape leader IRQ routine
- fc6a-write-tape-leader-irq-routine.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fc6a-write-tape-leader-irq-routine.md
  sha256: 10d6aae5a450e63bc5e4e1ebded1e39a2847474776de12a6f14a112d8c994534
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: write tape leader IRQ routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fc6a-write-tape-leader-irq-routine.md`
**SHA256**: `10d6aae5a450e63bc5e4e1ebded1e39a2847474776de12a6f14a112d8c994534`

## Summary



# $FC6A — write tape leader IRQ routine

## Disassemblatura
```assembly
.FC6A  A9 78    LDA #$78   ; set time constant low byte for bit = leader
.FC6C  20 AF FB JSR $FBAF   ; write time constant and toggle tape
.FC6F  D0 E3    BNE $FC54   ; if tape bit high restore registers and exit interrupt
.FC71  C6 A7    DEC $A7   ; decrement cycle count
.FC73  D0 DF    BNE $FC54   ; if not all done restore registers and exit interrupt
.FC75  20 97 FB JSR $FB97   ; new tape byte setup
.FC78  C6 AB    DEC ...
