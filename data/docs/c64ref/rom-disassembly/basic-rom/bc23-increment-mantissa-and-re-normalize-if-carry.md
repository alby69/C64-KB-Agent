---
title: INCREMENT MANTISSA AND RE-NORMALIZE IF CARRY
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0068-bits
- bc23-increment-mantissa-and-re-normalize-if-carry
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BC23
  address_end: $BC28
  symbol: increment-mantissa-and-re-normalize-if-carry
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC23**: YES, INCREMENT FAC'
---

# $BC23 — INCREMENT MANTISSA AND RE-NORMALIZE IF CARRY

## Disassemblatura
```assembly
.BC23  20 6F B9 JSR $B96F   ; YES, INCREMENT FAC
.BC26  D0 F2    BNE $BC1A   ; HIGH BYTE HAS BITS, FINISHED
.BC28  4C 38 B9 JMP $B938   ; HI-BYTE=0, SO SHIFT LEFT
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC23**: YES, INCREMENT FAC
- **$BC26**: HIGH BYTE HAS BITS, FINISHED
- **$BC28**: HI-BYTE=0, SO SHIFT LEFT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*