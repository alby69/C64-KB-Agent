---
title: set VIA 2 ICR from A
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
- ef3b-set-via-2-icr-from-a
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $EF3B
  address_end: $EF49
  symbol: set-via-2-icr-from-a
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF3B**: save VIA 2 ICR'
---

# $EF3B — set VIA 2 ICR from A

## Disassemblatura
```assembly
.EF3B  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.EF3E  4D A1 02 EOR $02A1   ; EOR with the RS-232 interrupt enable byte
.EF41  09 80    ORA #$80   ; set the interrupts enable bit
.EF43  8D A1 02 STA $02A1   ; save the RS-232 interrupt enable byte
.EF46  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.EF49  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EF3B**: save VIA 2 ICR
- **$EF3E**: EOR with the RS-232 interrupt enable byte
- **$EF41**: set the interrupts enable bit
- **$EF43**: save the RS-232 interrupt enable byte
- **$EF46**: save VIA 2 ICR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*