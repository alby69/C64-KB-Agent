---
title: save the status and do the IRQ routine
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ff43-einsprung-aus-bandroutine
- ff47
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FF43
  address_end: $FF47
  symbol: save-the-status-and-do-the-irq-routine
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF43**: save the processor status'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FF43**: Statusregister auf Stapel'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FF43**: store processor reg.'
---

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