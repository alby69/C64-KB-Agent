---
id: src-f72c-find-the-tape-header-exit-with-header-in-buffer
type: source
title: 'Source Summary: find the tape header, exit with header in buffer'
aliases:
- find the tape header, exit with header in buffer
- f72c-find-the-tape-header-exit-with-header-in-buffer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f72c-find-the-tape-header-exit-with-header-in-buffer.md
  sha256: 77df6ec21e374fa122e5b7f25a6fdfd174df25060734db9c6ba01b7b89206905
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: find the tape header, exit with header in buffer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f72c-find-the-tape-header-exit-with-header-in-buffer.md`
**SHA256**: `77df6ec21e374fa122e5b7f25a6fdfd174df25060734db9c6ba01b7b89206905`

## Summary



# $F72C — find the tape header, exit with header in buffer

## Disassemblatura
```assembly
.F72C  A5 93    LDA $93   ; get load/verify flag
.F72E  48       PHA   ; save load/verify flag
.F72F  20 41 F8 JSR $F841   ; initiate tape read
.F732  68       PLA   ; restore load/verify flag
.F733  85 93    STA $93   ; save load/verify flag
.F735  B0 32    BCS $F769   ; exit if error
.F737  A0 00    LDY #$00   ; clear the index
.F739  B1 B2    LDA ($B2),Y   ; read first byte from tape buffer
.F73B  C9 ...
