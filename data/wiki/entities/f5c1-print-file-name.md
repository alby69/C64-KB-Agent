---
id: f5c1-print-file-name
type: entity
title: print file name
aliases:
- print file name
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5c1-print-file-name.md
  sha256: f3d483d35d7f0e605ed844cb18249c5ba91a4f7f9a1e7d1adeae17ad2d1e4a03
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f5c1-print-file-name
---

# print file name



# $F5C1 — print file name

## Disassemblatura
```assembly
.F5C1  A4 B7    LDY $B7   ; get file name length
.F5C3  F0 0C    BEQ $F5D1   ; exit if null file name
.F5C5  A0 00    LDY #$00   ; clear index
.F5C7  B1 BB    LDA ($BB),Y   ; get file name byte
.F5C9  20 D2 FF JSR $FFD2   ; output character to channel
.F5CC  C8       INY   ; increment index
.F5CD  C4 B7    CPY $B7   ; compare with file name length
.F5CF  D0 F6    BNE $F5C7   ; loop if more to do
.F5D1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F5C1**: get file name length
- **$F5C3**: exit if null file name
- **$F5C5**: clear index
- **$F5C7**: get file name byte
- **$F5C9**: output character to channel
- **$F5CC**: increment index
- **$F5CD**: compare with file name length
- **$F5CF**: loop if more to do

### Magnus Nyman (Magnus Nyman)
- **$F5C1**: FNLEN, length of current filename
- **$F5C3**: exit
- **$F5C7**: get character in filename
- **$F5C9**: output
- **$F5CC**: next character
- **$F5CD**: ready?
- **$F5D1**: back

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f5c1-print-file-name]]
