---
id: a3bf-move-bytes-routine
type: entity
title: move bytes routine
aliases:
- move bytes routine
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a3bf-move-bytes-routine.md
  sha256: 7a338c11a3ed6f3f69245f94c61d614e3750e62387591af52f039842f92abed4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a3bf-move-bytes-routine
---

# move bytes routine



# $A3BF — move bytes routine

## Disassemblatura
```assembly
.A3BF  38       SEC
.A3C0  A5 5A    LDA $5A
.A3C2  E5 5F    SBC $5F
.A3C4  85 22    STA $22
.A3C6  A8       TAY
.A3C7  A5 5B    LDA $5B
.A3C9  E5 60    SBC $60
.A3CB  AA       TAX
.A3CC  E8       INX
.A3CD  98       TYA
.A3CE  F0 23    BEQ $A3F3
.A3D0  A5 5A    LDA $5A
.A3D2  38       SEC
.A3D3  E5 22    SBC $22
.A3D5  85 5A    STA $5A
.A3D7  B0 03    BCS $A3DC
.A3D9  C6 5B    DEC $5B
.A3DB  38       SEC
.A3DC  A5 58    LDA $58
.A3DE  E5 22    SBC $22
.A3E0  85 58    STA $58
.A3E2  B0 08    BCS $A3EC
.A3E4  C6 59    DEC $59
.A3E6  90 04    BCC $A3EC
.A3E8  B1 5A    LDA ($5A),Y
.A3EA  91 58    STA ($58),Y
.A3EC  88       DEY
.A3ED  D0 F9    BNE $A3E8
.A3EF  B1 5A    LDA ($5A),Y
.A3F1  91 58    STA ($58),Y
.A3F3  C6 5B    DEC $5B
.A3F5  C6 59    DEC $59
.A3F7  CA       DEX
.A3F8  D0 F2    BNE $A3EC
.A3FA  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a3bf-move-bytes-routine]]
