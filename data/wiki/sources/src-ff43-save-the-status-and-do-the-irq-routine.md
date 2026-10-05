---
id: src-ff43-save-the-status-and-do-the-irq-routine
type: source
title: 'Source Summary: save the status and do the IRQ routine'
aliases:
- save the status and do the IRQ routine
- ff43-save-the-status-and-do-the-irq-routine.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff43-save-the-status-and-do-the-irq-routine.md
  sha256: bfc54071b2ad6c42a2754dc83198c412c68cfad2c5f7a81ab39523d68450c2ff
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save the status and do the IRQ routine

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ff43-save-the-status-and-do-the-irq-routine.md`
**SHA256**: `bfc54071b2ad6c42a2754dc83198c412c68cfad2c5f7a81ab39523d68450c2ff`

## Summary



# $FF43 — save the status and do the IRQ routine

## Disassemblatura
```assembly
.FF43  08       PHP   ; save the processor status
.FF44  68       PLA   ; pull the processor status
.FF45  29 EF    AND #$EF   ; mask xxx0 xxxx, clear the break bit
.FF47  48       PHA   ; save the modified processor status
```


## Commenti

### Original Disassembly (—)
- **$FF43**: save the processor status
- **$FF44**: pull the processor status
- **$FF45**: mask xxx0 xxxx, clear the break bit
- **$FF47**: save ...
