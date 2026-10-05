---
id: src-b688-move-string-with-length-a-pointer-in-xy
type: source
title: 'Source Summary: move string with length A, pointer in XY'
aliases:
- move string with length A, pointer in XY
- b688-move-string-with-length-a-pointer-in-xy.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b688-move-string-with-length-a-pointer-in-xy.md
  sha256: 63467753bc564e1af9677d271dcaf1381c08cb02e18fd8703ddc7f7e9529ef5e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: move string with length A, pointer in XY

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b688-move-string-with-length-a-pointer-in-xy.md`
**SHA256**: `63467753bc564e1af9677d271dcaf1381c08cb02e18fd8703ddc7f7e9529ef5e`

## Summary



# $B688 — move string with length A, pointer in XY

## Disassemblatura
```assembly
.B688  86 22    STX $22
.B68A  84 23    STY $23
.B68C  A8       TAY
.B68D  F0 0A    BEQ $B699
.B68F  48       PHA
.B690  88       DEY
.B691  B1 22    LDA ($22),Y
.B693  91 35    STA ($35),Y
.B695  98       TYA
.B696  D0 F8    BNE $B690
.B698  68       PLA
.B699  18       CLC
.B69A  65 35    ADC $35
.B69C  85 35    STA $35
.B69E  90 02    BCC $B6A2
.B6A0  E6 36    INC $36
.B6A2  60       RTS
```


## Commenti

##...
