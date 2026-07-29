---
title: set tape vector
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
- fcbd-set-irq-vector-depending-on-x
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $FCBD
  address_end: $FCC9
  symbol: set-tape-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FCBD**: get tape IRQ vector low byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FCBD — set tape vector

## Disassemblatura
```assembly
.FCBD  BD 93 FD LDA $FD93,X   ; get tape IRQ vector low byte
.FCC0  8D 14 03 STA $0314   ; set IRQ vector low byte
.FCC3  BD 94 FD LDA $FD94,X   ; get tape IRQ vector high byte
.FCC6  8D 15 03 STA $0315   ; set IRQ vector high byte
.FCC9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCBD**: get tape IRQ vector low byte
- **$FCC0**: set IRQ vector low byte
- **$FCC3**: get tape IRQ vector high byte
- **$FCC6**: set IRQ vector high byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*