---
title: flush BASIC stack and clear the continue pointer
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a67a-reset-stack-and-program-pointers
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $A67A
  address_end: $A68D
  symbol: flush-basic-stack-and-clear-the-continue-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A67A**: get the descriptor stack start'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $A67A — flush BASIC stack and clear the continue pointer

## Disassemblatura
```assembly
.A67A  A2 19    LDX #$19   ; get the descriptor stack start
.A67C  86 16    STX $16   ; set the descriptor stack pointer
.A67E  68       PLA   ; pull the return address low byte
.A67F  A8       TAY   ; copy it
.A680  68       PLA   ; pull the return address high byte
.A681  A2 FA    LDX #$FA   ; set the cleared stack pointer
.A683  9A       TXS   ; set the stack
.A684  48       PHA   ; push the return address high byte
.A685  98       TYA   ; restore the return address low byte
.A686  48       PHA   ; push the return address low byte
.A687  A9 00    LDA #$00   ; clear A
.A689  85 3E    STA $3E   ; clear the continue pointer high byte
.A68B  85 10    STA $10   ; clear the subscript/FNX flag
.A68D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A67A**: get the descriptor stack start
- **$A67C**: set the descriptor stack pointer
- **$A67E**: pull the return address low byte
- **$A67F**: copy it
- **$A680**: pull the return address high byte
- **$A681**: set the cleared stack pointer
- **$A683**: set the stack
- **$A684**: push the return address high byte
- **$A685**: restore the return address low byte
- **$A686**: push the return address low byte
- **$A687**: clear A
- **$A689**: clear the continue pointer high byte
- **$A68B**: clear the subscript/FNX flag

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*