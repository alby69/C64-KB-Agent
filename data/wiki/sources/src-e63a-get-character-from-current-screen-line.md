---
id: src-e63a-get-character-from-current-screen-line
type: source
title: 'Source Summary: get character from current screen line'
aliases:
- get character from current screen line
- e63a-get-character-from-current-screen-line.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e63a-get-character-from-current-screen-line.md
  sha256: 8ca6ab529ca416a42e7c58f543b2ccbca9c14ebdde49c6fea7a345f5d0a513c8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get character from current screen line

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e63a-get-character-from-current-screen-line.md`
**SHA256**: `8ca6ab529ca416a42e7c58f543b2ccbca9c14ebdde49c6fea7a345f5d0a513c8`

## Summary



# $E63A — get character from current screen line

## Disassemblatura
```assembly
.E63A  A4 D3    LDY $D3
.E63C  B1 D1    LDA ($D1),Y
.E63E  85 D7    STA $D7
.E640  29 3F    AND #$3F
.E642  06 D7    ASL $D7
.E644  24 D7    BIT $D7
.E646  10 02    BPL $E64A
.E648  09 80    ORA #$80
.E64A  90 04    BCC $E650
.E64C  A6 D4    LDX $D4
.E64E  D0 04    BNE $E654
.E650  70 02    BVS $E654
.E652  09 40    ORA #$40
.E654  E6 D3    INC $D3
.E656  20 84 E6 JSR $E684
.E659  C4 C8    CPY $C8
.E65B  D0 17    ...
