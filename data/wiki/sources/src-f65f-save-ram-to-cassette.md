---
id: src-f65f-save-ram-to-cassette
type: source
title: 'Source Summary: save ram to cassette'
aliases:
- save ram to cassette
- f65f-save-ram-to-cassette.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f65f-save-ram-to-cassette.md
  sha256: 9c2f615d7f76f5913ffd30afaaa6e8d08031f499d3b79ab3c1cc24b61ecb6ff0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save ram to cassette

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f65f-save-ram-to-cassette.md`
**SHA256**: `9c2f615d7f76f5913ffd30afaaa6e8d08031f499d3b79ab3c1cc24b61ecb6ff0`

## Summary



# $F65F — save ram to cassette

## Disassemblatura
```assembly
.F65F  20 D0 F7 JSR $F7D0
.F662  90 8D    BCC $F5F1
.F664  20 38 F8 JSR $F838
.F667  B0 25    BCS $F68E
.F669  20 8F F6 JSR $F68F
.F66C  A2 03    LDX #$03
.F66E  A5 B9    LDA $B9
.F670  29 01    AND #$01
.F672  D0 02    BNE $F676
.F674  A2 01    LDX #$01
.F676  8A       TXA
.F677  20 6A F7 JSR $F76A
.F67A  B0 12    BCS $F68E
.F67C  20 67 F8 JSR $F867
.F67F  B0 0D    BCS $F68E
.F681  A5 B9    LDA $B9
.F683  29 02    AND #$02
.F685  ...
