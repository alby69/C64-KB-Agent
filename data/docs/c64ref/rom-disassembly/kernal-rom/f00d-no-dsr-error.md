---
title: NO DSR ERROR
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0297-rsstat
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  address: $F00D
  address_end: $F013
  symbol: no-dsr-error
  sources:
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F00F**: RSSTAT, 6551 status register image'
---

# $F00D — NO DSR ERROR

## Disassemblatura
```assembly
.F00D  A9 40    LDA #$40
.F00F  8D 97 02 STA $0297   ; RSSTAT, 6551 status register image
.F012  18       CLC
.F013  60       RTS
```


## Commenti

### Magnus Nyman (Magnus Nyman)
- **$F00F**: RSSTAT, 6551 status register image

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*