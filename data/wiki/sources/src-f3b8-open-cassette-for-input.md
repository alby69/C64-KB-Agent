---
id: src-f3b8-open-cassette-for-input
type: source
title: 'Source Summary: open cassette for input'
aliases:
- open cassette for input
- f3b8-open-cassette-for-input.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f3b8-open-cassette-for-input.md
  sha256: 3ec27864f2c36ccfab7b4c12c29c3832b0e0222e19fcf374f1413ee52014af6a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open cassette for input

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f3b8-open-cassette-for-input.md`
**SHA256**: `3ec27864f2c36ccfab7b4c12c29c3832b0e0222e19fcf374f1413ee52014af6a`

## Summary



# $F3B8 — open cassette for input

## Disassemblatura
```assembly
.F3B8  20 38 F8 JSR $F838
.F3BB  B0 17    BCS $F3D4
.F3BD  A9 04    LDA #$04
.F3BF  20 6A F7 JSR $F76A
.F3C2  A9 BF    LDA #$BF
.F3C4  A4 B9    LDY $B9
.F3C6  C0 60    CPY #$60
.F3C8  F0 07    BEQ $F3D1
.F3CA  A0 00    LDY #$00
.F3CC  A9 02    LDA #$02
.F3CE  91 B2    STA ($B2),Y
.F3D0  98       TYA
.F3D1  85 A6    STA $A6
.F3D3  18       CLC
.F3D4  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento ...
