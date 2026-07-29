---
title: move string with length A, pointer in XY
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $B688
  address_end: $B6A2
  symbol: move-string-with-length-a-pointer-in-xy
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B688 — move string with length A, pointer in XY

## Disassemblatura
```assembly
.B688  86 22    STX $22
.B68A  84 23    STY $23
.B68C  A8       TAY
.B68D  F0 0A    BEQ $B699
.B68F  48       PHA
.B690  88       DEY
.B691  B1 22    LDA ($22),Y
.B693  91 35    STA ($35),Y
.B695  98       TYA
.B696  D0 F8    BNE $B690
.B698  68       PLA
.B699  18       CLC
.B69A  65 35    ADC $35
.B69C  85 35    STA $35
.B69E  90 02    BCC $B6A2
.B6A0  E6 36    INC $36
.B6A2  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*