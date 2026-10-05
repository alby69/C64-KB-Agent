---
id: src-f8e2-set-timing
type: source
title: 'Source Summary: # set timing'
aliases:
- '# set timing'
- f8e2-set-timing.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f8e2-set-timing.md
  sha256: 5229cc4bd440310656e64642227e7483e1afab648861d69d0874b27936ee6015
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: # set timing

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f8e2-set-timing.md`
**SHA256**: `5229cc4bd440310656e64642227e7483e1afab648861d69d0874b27936ee6015`

## Summary



# $F8E2 — # set timing

## Disassemblatura
```assembly
.F8E2  86 B1    STX $B1   ; save tape timing constant max byte
.F8E4  A5 B0    LDA $B0   ; get tape timing constant min byte
.F8E6  0A       ASL   ; *2
.F8E7  0A       ASL   ; *4
.F8E8  18       CLC   ; clear carry for add
.F8E9  65 B0    ADC $B0   ; add tape timing constant min byte *5
.F8EB  18       CLC   ; clear carry for add
.F8EC  65 B1    ADC $B1   ; add tape timing constant max byte
.F8EE  85 B1    STA $B1   ; save tape timing cons...
