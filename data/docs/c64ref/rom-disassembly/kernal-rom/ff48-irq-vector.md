---
title: IRQ vector
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
- brk
- ff48-irq-einsprung
- ff4a
- ff4d
- ff53
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FF48
  address_end: $FF58
  symbol: irq-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF48**: save A'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FF48**: Akku auf Stapel retten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FF55**: normally FE66'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FF48**: Store Acc'
---

# $FF48 — IRQ vector

## Disassemblatura
```assembly
.FF48  48       PHA   ; save A
.FF49  8A       TXA   ; copy X
.FF4A  48       PHA   ; save X
.FF4B  98       TYA   ; copy Y
.FF4C  48       PHA   ; save Y
.FF4D  BA       TSX   ; copy stack pointer
.FF4E  BD 04 01 LDA $0104,X   ; get stacked status register
.FF51  29 10    AND #$10   ; mask BRK flag
.FF53  F0 03    BEQ $FF58   ; branch if not BRK
.FF55  6C 16 03 JMP ($0316)   ; else do BRK vector (iBRK)
.FF58  6C 14 03 JMP ($0314)   ; do IRQ vector (iIRQ)
```


## Commenti

### Original Disassembly (—)
- **$FF48**: save A
- **$FF49**: copy X
- **$FF4A**: save X
- **$FF4B**: copy Y
- **$FF4C**: save Y
- **$FF4D**: copy stack pointer
- **$FF4E**: get stacked status register
- **$FF51**: mask BRK flag
- **$FF53**: branch if not BRK
- **$FF55**: else do BRK vector (iBRK)
- **$FF58**: do IRQ vector (iIRQ)

### Commodore-64-intern-Buch (Commodore)
- **$FF48**: Akku auf Stapel retten
- **$FF49**: X nach Akku
- **$FF4A**: X-Register retten
- **$FF4B**: Y nach Akku
- **$FF4C**: Y-Register retten
- **$FF4D**: Stapelzeiger als Zähler in X
- **$FF4E**: Break-Flag vom Stapel holen
- **$FF51**: und testen
- **$FF53**: nicht gesetzt
- **$FF55**: BREAK - Routine
- **$FF58**: Interrupt - Routine

### Marko Mäkelä (Marko Mäkelä)
- **$FF55**: normally FE66
- **$FF58**: normally EA31

### Magnus Nyman (Magnus Nyman)
- **$FF48**: Store Acc
- **$FF4A**: Store X-reg
- **$FF4C**: Store Y-reg
- **$FF4E**: Read byte on stack written by processor?
- **$FF51**: check bit 4 to determine HW or SW interrupt
- **$FF55**: jump to CBINV. Points to FE66, basic warm start
- **$FF58**: jump to CINV. Points to EA31, main IRQ entry point

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*