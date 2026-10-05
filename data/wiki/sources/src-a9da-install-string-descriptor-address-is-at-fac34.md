---
id: src-a9da-install-string-descriptor-address-is-at-fac34
type: source
title: 'Source Summary: INSTALL STRING, DESCRIPTOR ADDRESS IS AT FAC+3,4'
aliases:
- INSTALL STRING, DESCRIPTOR ADDRESS IS AT FAC+3,4
- a9da-install-string-descriptor-address-is-at-fac34.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a9da-install-string-descriptor-address-is-at-fac34.md
  sha256: 827309c9800920a190df0f6c0a3d62475808f5992a671a7b5ebc16b284213b62
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: INSTALL STRING, DESCRIPTOR ADDRESS IS AT FAC+3,4

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a9da-install-string-descriptor-address-is-at-fac34.md`
**SHA256**: `827309c9800920a190df0f6c0a3d62475808f5992a671a7b5ebc16b284213b62`

## Summary



# $A9DA — INSTALL STRING, DESCRIPTOR ADDRESS IS AT FAC+3,4

## Disassemblatura
```assembly
.A9DA  A4 4A    LDY $4A   ; STRING DATA ALREADY IN STRING AREA?
.A9DC  C0 BF    CPY #$BF
.A9DE  D0 4C    BNE $AA2C
.A9E0  20 A6 B6 JSR $B6A6
.A9E3  C9 06    CMP #$06
.A9E5  D0 3D    BNE $AA24
.A9E7  A0 00    LDY #$00
.A9E9  84 61    STY $61
.A9EB  84 66    STY $66
.A9ED  84 71    STY $71
.A9EF  20 1D AA JSR $AA1D
.A9F2  20 E2 BA JSR $BAE2
.A9F5  E6 71    INC $71
.A9F7  A4 71    LDY $71
.A9F9  20 1D AA JS...
