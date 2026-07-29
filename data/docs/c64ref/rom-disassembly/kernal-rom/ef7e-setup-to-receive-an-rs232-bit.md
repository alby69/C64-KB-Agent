---
title: setup to receive an RS232 bit
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ef7e-set-up-to-receive
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $EF7E
  address_end: $EF8D
  symbol: setup-to-receive-an-rs232-bit
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF7E**: enable FLAG interrupt'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EF80**: CIA#2 I.C.R.'
---

# $EF7E — setup to receive an RS232 bit

## Disassemblatura
```assembly
.EF7E  A9 90    LDA #$90   ; enable FLAG interrupt
.EF80  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.EF83  0D A1 02 ORA $02A1   ; OR with the RS-232 interrupt enable byte
.EF86  8D A1 02 STA $02A1   ; save the RS-232 interrupt enable byte
.EF89  85 A9    STA $A9   ; set start bit check flag, set no start bit received
.EF8B  A9 02    LDA #$02   ; disable timer B interrupt
.EF8D  4C 3B EF JMP $EF3B   ; set VIA 2 ICR from A and return
```


## Commenti

### Original Disassembly (—)
- **$EF7E**: enable FLAG interrupt
- **$EF80**: save VIA 2 ICR
- **$EF83**: OR with the RS-232 interrupt enable byte
- **$EF86**: save the RS-232 interrupt enable byte
- **$EF89**: set start bit check flag, set no start bit received
- **$EF8B**: disable timer B interrupt
- **$EF8D**: set VIA 2 ICR from A and return

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EF80**: CIA#2 I.C.R.
- **$EF83**: ENABL, RS232 enables
- **$EF89**: RINONE, check for start bit
- **$EF8D**: disable timer and exit

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*