---
title: disable timer A interrupt
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
- ef39-disable-timer
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $EF39
  address_end: $EF39
  symbol: disable-timer-a-interrupt
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF39**: disable timer A interrupt'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EF39**: ; CIA#2 interrupt control register'
---

# $EF39 — disable timer A interrupt

## Disassemblatura
```assembly
.EF39  A9 01    LDA #$01   ; disable timer A interrupt
```


## Commenti

### Original Disassembly (—)
- **$EF39**: disable timer A interrupt

### Magnus Nyman (Magnus Nyman)
- **$EF39**: ; CIA#2 interrupt control register
- **$EF3B**: ; ENABL, RS232 enables
- **$EF41**: ; ENABL
- **$EF43**: ; CIA#2 interrupt control register

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*