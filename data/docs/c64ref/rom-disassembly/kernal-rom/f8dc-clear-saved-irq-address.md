---
title: clear saved IRQ address
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
- f8dc-clear-saved-irq-address
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $F8DC
  address_end: $F8E1
  symbol: clear-saved-irq-address
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F8DC**: clear A'
---

# $F8DC — clear saved IRQ address

## Disassemblatura
```assembly
.F8DC  A9 00    LDA #$00   ; clear A
.F8DE  8D A0 02 STA $02A0   ; clear saved IRQ address high byte
.F8E1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F8DC**: clear A
- **$F8DE**: clear saved IRQ address high byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*