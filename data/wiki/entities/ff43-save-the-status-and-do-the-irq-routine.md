---
id: ff43-save-the-status-and-do-the-irq-routine
type: entity
title: save the status and do the IRQ routine
aliases:
- save the status and do the IRQ routine
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff43-save-the-status-and-do-the-irq-routine.md
  sha256: bfc54071b2ad6c42a2754dc83198c412c68cfad2c5f7a81ab39523d68450c2ff
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ff43-save-the-status-and-do-the-irq-routine
---

# save the status and do the IRQ routine



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
- **$FF47**: save the modified processor status

### Commodore-64-intern-Buch (Commodore)
- **$FF43**: Statusregister auf Stapel
- **$FF44**: Statusregister in Akku
- **$FF45**: Break-Flag löschen
- **$FF47**: und wieder auf Stapel legen

### Magnus Nyman (Magnus Nyman)
- **$FF43**: store processor reg.
- **$FF44**: get reg
- **$FF45**: clear bit4
- **$FF47**: store reg

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ff43-save-the-status-and-do-the-irq-routine]]
