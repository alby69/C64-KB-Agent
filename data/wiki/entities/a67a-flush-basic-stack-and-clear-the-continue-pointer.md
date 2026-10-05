---
id: a67a-flush-basic-stack-and-clear-the-continue-pointer
type: entity
title: flush BASIC stack and clear the continue pointer
aliases:
- flush BASIC stack and clear the continue pointer
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a67a-flush-basic-stack-and-clear-the-continue-pointer.md
  sha256: dacc740118dd84f2e76b076b145d2a33ca24c4a8c3ed2d16b5407578c41f2178
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a67a-flush-basic-stack-and-clear-the-continue-pointer
---

# flush BASIC stack and clear the continue pointer



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

## References
- Source: [[src-a67a-flush-basic-stack-and-clear-the-continue-pointer]]
