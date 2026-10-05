---
id: src-f2c8-close-cassette-device
type: source
title: 'Source Summary: close cassette device'
aliases:
- close cassette device
- f2c8-close-cassette-device.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f2c8-close-cassette-device.md
  sha256: c54734cc0620b88b9a0022d56432e89f4dd6ee1c057620bca077911474049c6d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: close cassette device

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f2c8-close-cassette-device.md`
**SHA256**: `c54734cc0620b88b9a0022d56432e89f4dd6ee1c057620bca077911474049c6d`

## Summary



# $F2C8 — close cassette device

## Disassemblatura
```assembly
.F2C8  A5 B9    LDA $B9
.F2CA  29 0F    AND #$0F
.F2CC  F0 23    BEQ $F2F1
.F2CE  20 D0 F7 JSR $F7D0
.F2D1  A9 00    LDA #$00
.F2D3  38       SEC
.F2D4  20 DD F1 JSR $F1DD
.F2D7  20 64 F8 JSR $F864
.F2DA  90 04    BCC $F2E0
.F2DC  68       PLA
.F2DD  A9 00    LDA #$00
.F2DF  60       RTS
.F2E0  A5 B9    LDA $B9
.F2E2  C9 62    CMP #$62
.F2E4  D0 0B    BNE $F2F1
.F2E6  A9 05    LDA #$05
.F2E8  20 6A F7 JSR $F76A
.F2EB  4C F1 F2 JMP...
