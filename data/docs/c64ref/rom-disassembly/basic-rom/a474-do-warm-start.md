---
title: do warm start
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a474-do-warm-start
- a480-eingabe-warteschleife
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $A474
  address_end: $A480
  symbol: do-warm-start
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A474**: set "READY." pointer low byte'
---

# $A474 — do warm start

## Disassemblatura
```assembly
.A474  A9 76    LDA #$76   ; set "READY." pointer low byte
.A476  A0 A3    LDY #$A3   ; set "READY." pointer high byte
.A478  20 1E AB JSR $AB1E   ; print null terminated string
.A47B  A9 80    LDA #$80   ; set for control messages only
.A47D  20 90 FF JSR $FF90   ; control kernal messages
.A480  6C 02 03 JMP ($0302)   ; do BASIC warm start
```


## Commenti

### Original Disassembly (—)
- **$A474**: set "READY." pointer low byte
- **$A476**: set "READY." pointer high byte
- **$A478**: print null terminated string
- **$A47B**: set for control messages only
- **$A47D**: control kernal messages
- **$A480**: do BASIC warm start

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*