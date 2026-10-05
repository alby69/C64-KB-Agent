---
id: bc23-increment-mantissa-and-re-normalize-if-carry
type: entity
title: INCREMENT MANTISSA AND RE-NORMALIZE IF CARRY
aliases:
- INCREMENT MANTISSA AND RE-NORMALIZE IF CARRY
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc23-increment-mantissa-and-re-normalize-if-carry.md
  sha256: 619e714ed44052c1c2574b92df2b2744bad00c12266b0128635fccb62919ec6d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bc23-increment-mantissa-and-re-normalize-if-carry
---

# INCREMENT MANTISSA AND RE-NORMALIZE IF CARRY



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

## References
- Source: [[src-bc23-increment-mantissa-and-re-normalize-if-carry]]
