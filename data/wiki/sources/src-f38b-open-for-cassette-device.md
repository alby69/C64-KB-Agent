---
id: src-f38b-open-for-cassette-device
type: source
title: 'Source Summary: open for cassette device'
aliases:
- open for cassette device
- f38b-open-for-cassette-device.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f38b-open-for-cassette-device.md
  sha256: 96b6b49d52943a36cfe15f10c039e3434d51a6df6654f7241a18d0ac97266223
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open for cassette device

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f38b-open-for-cassette-device.md`
**SHA256**: `96b6b49d52943a36cfe15f10c039e3434d51a6df6654f7241a18d0ac97266223`

## Summary



# $F38B — open for cassette device

## Disassemblatura
```assembly
.F38B  20 D0 F7 JSR $F7D0
.F38E  B0 03    BCS $F393
.F390  4C 13 F7 JMP $F713
.F393  A5 B9    LDA $B9
.F395  29 0F    AND #$0F
.F397  D0 1F    BNE $F3B8
.F399  20 17 F8 JSR $F817
.F39C  B0 36    BCS $F3D4
.F39E  20 AF F5 JSR $F5AF
.F3A1  A5 B7    LDA $B7
.F3A3  F0 0A    BEQ $F3AF
.F3A5  20 EA F7 JSR $F7EA
.F3A8  90 18    BCC $F3C2
.F3AA  F0 28    BEQ $F3D4
.F3AC  4C 04 F7 JMP $F704
.F3AF  20 2C F7 JSR $F72C
.F3B2  F0 20    BEQ ...
