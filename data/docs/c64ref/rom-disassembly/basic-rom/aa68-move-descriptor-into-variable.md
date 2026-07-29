---
title: move descriptor into variable
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
  address: $AA68
  address_end: $AA7F
  symbol: move-descriptor-into-variable
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AA68 — move descriptor into variable

## Disassemblatura
```assembly
.AA68  85 50    STA $50
.AA6A  84 51    STY $51
.AA6C  20 DB B6 JSR $B6DB
.AA6F  A0 00    LDY #$00
.AA71  B1 50    LDA ($50),Y
.AA73  91 49    STA ($49),Y
.AA75  C8       INY
.AA76  B1 50    LDA ($50),Y
.AA78  91 49    STA ($49),Y
.AA7A  C8       INY
.AA7B  B1 50    LDA ($50),Y
.AA7D  91 49    STA ($49),Y
.AA7F  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*